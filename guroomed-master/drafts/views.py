from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.models import User, Group
from django.http import HttpResponse
import simplejson as json
from .models import DraftCourse, CoursesRoles, ReviewedCourses, ReasonsRejected, ApprovedCourses
from .draft_courses import getDraft
from courses.models import Course
from django.core.mail import send_mail
from users.views import has_group
from users.views import get_id_by_name


# To check draft_course is assigned to user or not
# Parameters - ids of user, draft, group
# Response - True is draft is assigned or False if no relation
def is_assigned(user_id, draft_id, group_id):
	try:
		if CoursesRoles.objects.filter(user_id=user_id, course_draft_id=draft_id, role_type=group_id).exists():
			return True
		else:
			return False
	except Exception as e:
		return False


# to view draft_course details
# Parameters - draft_course id
# Response - draft details and managers and reviewers reviews
@csrf_exempt
def view_draft(request, id):
	if request.method == 'GET':
		try:
			draft_course = getDraft(request, id)
		except Exception as e:
			return HttpResponse(json.dumps({'status':0, 'error':str(e)}))

		reviews	= []
		if request.user.groups.filter(name='Course Manager').exists(): #only if the user is course manager
			for reviewed in ReviewedCourses.objects.all().filter(course_draft_id=id):
				if reviewed.status == 0:
					status = 'Rejected'
				if reviewed.status == 1:
					status = 'Accepted'
				if reviewed.reason_rejected == None:
					reason = None
				else:
					reason = reviewed.reason_rejected.text
				reviews.append({
					'user_id' : reviewed.user_id.first_name +' '+ reviewed.user_id.last_name,
					# 'course_draft_id' = reviewed.draft
					'comments' : reviewed.comments,
					'status' : status,
					'reason_rejected' : reason,
				})

		return HttpResponse(json.dumps({
			'status':1,
			'draft_course':draft_course,
			'reviews': reviews,
		}))

	else:
		return HttpResponse(json.dumps({'status':0, 'error':'Wrong method'}))


#to let manager to approve or reject the draft_course
#Parameters - None
#response - Success or Failure
@csrf_exempt
def manager_action(request):
	#if request method is get then response will be a list of reasons to be rejected
	if request.method == 'GET':
		try:
			reasons = []
			for rr in ReasonsRejected.objects.all().filter(type='Course Manager'):
				reasons.append({
					'value':rr.id,
					'label':rr.text,
				})
		except Exception as e:
			return HttpResponse(json.dumps({'status':0, 'error':str(e)}))

	#if method is post then managers decision will be saved in database
	if request.method == 'POST':
		if not request.user.is_authenticated: #if user is not logged in
			return HttpResponse(json.dumps({'status':0, 'error':'Please Login'}))
		if not has_group(request, 'Course Manager'): # if user is not manager
			return HttpResponse(json.dumps({'status':0, 'error':'You are not authorized person'}))
		if 'course_id' not in request.POST:
			return HttpResponse(json.dumps({'status':0, 'error':'please send course id'}))
		try:
			draft = DraftCourse.objects.get(id=request.POST['course_id'])
		except DraftCourse.DoesNotExist:
			return HttpResponse(json.dumps({'status':0, 'error':'Course does not exist'}))
		if 'status' not in request.POST:
			return HttpResponse(json.dumps({'status':0, 'error':'Please enter a status'}))
		group_id = get_id_by_name('Course Manager')
		return HttpResponse(json.dumps({'status':0, 'error':CoursesRoles.objects.filter(user_id=request.user.id, course_draft_id=draft.id, role_type=group_id).exists()}))
		if not CoursesRoles.objects.filter(user_id=request.user.id, course_draft_id=draft.id, role_type=group_id).exists():
			return HttpResponse(json.dumps({'status':0, 'error':'You are not authorized person'}))
		if 'comments' not in request.POST:
			comments = ''
		else:
			comments = request.POST['comments']
		if request.POST['status'] == str(0):
			if 'reason_rejected' not in request.POST:
				return HttpResponse(json.dumps({'status':0, 'error':'Please select the Reason to reject'}))
			try:
				reason_rejected = ReasonsRejected.objects.get(id=request.POST['reason_rejected'])
			except ReasonsRejected.DoesNotExist:
				return HttpResponse(json.dumps({'status':0, 'error':'Reason does not exist'}))
		else:
			reason_rejected = None
		try:
			ac = ApprovedCourses()
			ac.user_id = request.user
			ac.course_draft_id = draft
			ac.comments = comments
			ac.status = request.POST['status']
			ac.reason_rejected = reason_rejected
			ac.save()
			if request.POST['status'] == str(0):
				draft.status = 0
			if request.POST['status'] == str(1):
				draft.status = 1
			draft.save()
			course_id = 0
			if draft.status == 1:
				course_id = live_course(request, draft)
				if not isinstance(course_id, int):
					draft.status = None
					draft.save()
					ac.delete()
					return HttpResponse(json.dumps({'status':0, 'error':'Not able to make course live', 'msg':course_id}))
		except Exception as e:
			return HttpResponse(json.dumps({'status':0, 'error':str(e)}))
		return HttpResponse(json.dumps({'status':1, 'course_id':course_id, 'msg':'Your action has been saved'}))
	else:
		return HttpResponse(json.dumps({'status':0, 'error':'Wrong method'}))


#to let reviewer to approve or reject the draft_course
#Parameters - None
#response - Success or Failure
@csrf_exempt
def reviewer_action(request):
	if request.method == 'GET':
		try:
			reasons = []
			for rr in ReasonsRejected.objects.all().filter(type='Course Reviewer'):
				reasons.append({
					'value':rr.id,
					'label':rr.text,
				})
		except Exception as e:
			return HttpResponse(json.dumps({'status':0, 'error':str(e)}))
		return HttpResponse(json.dumps({'reasons_rejected': reasons}))
			
	if request.method == 'POST':
		if not request.user.is_authenticated: #if user is not logged in
			return HttpResponse(json.dumps({'status':0, 'error':'Please Login'}))
		if not request.user.groups.filter(id=8).exists(): # if user is not reviewer
			return HttpResponse(json.dumps({'status':0, 'error':'You are not authorized person'}))
		if 'course_id' not in request.POST:
			return HttpResponse(json.dumps({'status':0, 'error':'Send course id'}))
		try:
			draft = DraftCourse.objects.get(id=request.POST['course_id'])
		except DraftCourse.DoesNotExist:
			return HttpResponse(json.dumps({'status':0, 'error':'Course does not exist'}))
		if 'status' not in request.POST:
			return HttpResponse(json.dumps({'status':0, 'error':'Please enter a status'}))
		if not CoursesRoles.objects.filter(user_id=request.user.id, course_draft_id=request.POST['course_id'], role_type=8).exists():
			return HttpResponse(json.dumps({'status':0, 'error':'You are not authorized person'}))
		if ReviewedCourses.objects.filter(user_id=request.user.id, course_draft_id=request.POST['course_id']).exists():
			return HttpResponse(json.dumps({'status':0, 'error':'You have taken the action already'}))
		if 'comments' not in request.POST:
			comments = ''
		else:
			comments = request.POST['comments']
		if request.POST['status'] == str(0):
			if 'reason_rejected' not in request.POST:
				return HttpResponse(json.dumps({'status':0, 'error':'Please select the Reason to reject'}))
			try:
				reason_rejected = ReasonsRejected.objects.get(id=request.POST['reason_rejected'])
			except ReasonsRejected.DoesNotExist:
				return HttpResponse(json.dumps({'status':0, 'error':'Reason does not exist'}))
		else:
			reason_rejected = None
		try:
			rv = ReviewedCourses()
			rv.user_id = request.user
			rv.course_draft_id = draft
			rv.comments = comments
			rv.status = request.POST['status']
			rv.reason_rejected = reason_rejected
			rv.save()
			draft.is_reviewed = 1
			draft.save()
			for manager in User.objects.filter(groups__name='Course Manager'):
				send_mail(
					'Guroomed - Review Submitted',
					'New Review Submitted for - '+ draft.title,
					'no-reply@guroomed.com',
					[manager.email],
					fail_silently=False,
				)
		except Exception as e:
			return HttpResponse(json.dumps({'status':0, 'error':str(e)}))
		return HttpResponse(json.dumps({'status':1, 'msg':'Your action has been saved'}))
	else:
		return HttpResponse(json.dumps({'status':0, 'error':'Wrong method'}))


# to make the draft_course live
# Parametes - instance of draft_course
# Response - on success - id , and error on failure
def live_course(request, draft):
	try:
		course = Course()
		course.course_subcategory_id = draft.course_subcategory
		course.course_language_id = draft.course_language
		# course.instructor_id = draft.instructor
		course.title = draft.title
		course.subtitle = draft.subtitle
		course.ratings = draft.ratings
		course.rating_count = draft.rating_count
		course.students_enrolled = draft.students_enrolled
		course.what_will_i_learn = draft.what_will_i_learn
		course.requirements = draft.requirements
		course.description = draft.description
		course.preview_video_url = draft.preview_video_url
		course.preview_image_url = draft.preview_image_url
		course.price = draft.price
		course.discount = draft.discount
		course.no_lectures = draft.no_lectures
		course.no_hours = draft.no_hours
		course.slug = draft.slug
		# course.tags = draft.tags
		course.level = draft.level
		course.save()
		for inst in draft.instructor.all():
			course.instructor_id.add(inst)
	except Exception as e:
		return str(e)
	return course.id