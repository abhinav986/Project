from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.models import User, Group
from django.http import HttpResponse
import simplejson as json
from drafts.models import DraftCourse, CoursesRoles
import jwt


# check the groups of loggedin user and return the highest priority group
def get_JWTtoken(request):
	group = None
	user = request.user
	while True:
		if user.groups.filter(name='Admin'):
			group = 'Admin'
			break
		if user.groups.filter(name='Site Admin'):
			group = 'Site Admin'
			break
		if user.groups.filter(name='Course Manager'):
			group = 'Course Manager'
			break
		if user.groups.filter(name='Course Reviewer'):
			group = 'Course Reviewer'
			break
		if user.groups.filter(name='Instructor'):
			group = 'Instructor'
			break
		if user.groups.filter(name='Student'):
			group = 'Student'
			break
		break	
	encoded = jwt.encode({'username': user.username,'user_id': user.id,'group_name': group}, 'guroomed', algorithm='HS256')
	return HttpResponse(json.dumps({'status': 1, 'access_token': encoded}))


# to check whether user belongs to perticular group
def has_group(request, group_name=None):
	if request.user.groups.filter(name=group_name).exists():
		return True
	else:
		return False


# to get name from id.
def get_id_by_name(request, group_name=None):
	try:
		group = Group.objects.get(name=group_name)
		group_id = group.id
	except Group.DoesNotExist:
		group_id = None
	return group_id


# to display dashboard as per the role of user
@csrf_exempt
def view_dashboard(request, role_id, status_id=None):
	if request.method == 'GET':
		#validations
		if not request.user.is_authenticated: #if user is not logged in
			return HttpResponse(json.dumps({'status':0, 'error':'Please Login'}))
		if not request.user.groups.filter(id=role_id).exists(): # if user doesn't have role same as role_id
			return HttpResponse(json.dumps({'status':0, 'error':'You are not authorized to view this page'}))
		try:
			role = Group.objects.get(id=role_id)
		except Group.DoesNotExist:
			return HttpResponse(json.dumps({'status':0, 'error':'Role does not exist'}))

		role_based_drafts = []
		if role.name == 'Instructor': # instructor can view all of the courses
			for draft in DraftCourse.objects.all(): # for each draft check whether the loggedin user is instructor or not
				for instructor in draft.instructor.all():
					if instructor.user_id.id == request.user.id:
						role_based_drafts.append(draft)
						break

		elif role.name == 'Course Manager': # manager can view all of the submitted courses
			# submitted_drafts = drafts.exclude(is_reviewed=None)
			for manager_draft in CoursesRoles.objects.filter(user_id=request.user.id, role_type=7):
				try:
					if manager_draft.course_draft_id.is_reviewed != None:
						role_based_drafts.append(manager_draft.course_draft_id)
				except DraftCourse.DoesNotExist:
					pass
			# for submitted_draft in submitted_drafts:
			# 	if CoursesRoles.objects.get(user_id=request.user.id, role_type=7, course_draft_id=submitted_draft.id):
			# 		role_based_drafts.append(submitted_draft)

		elif role.name == 'Course Reviewer': # reviewer can view only assigned courses
			role_based_drafts = []
			for reviewer_draft in CoursesRoles.objects.filter(user_id=request.user.id, role_type=8):
				try:
					if reviewer_draft.course_draft_id.is_reviewed != None:
						role_based_drafts.append(reviewer_draft.course_draft_id)
				except DraftCourse.DoesNotExist:
					pass
		filtered_drafts = []
		# get the pool of draft courses
		if status_id == str(3): # all the courses
			filtered_drafts = role_based_drafts
		if status_id == str(2): # yet to be submitted/reviewed
			for role_based_draft in role_based_drafts:
				if role_based_draft.status == None:
					filtered_drafts.append(role_based_draft)
		if status_id == str(1): # accepted
			for role_based_draft in role_based_drafts:
				if role_based_draft.status == True:
					filtered_drafts.append(role_based_draft)
		if status_id == str(0): # rejected
			for role_based_draft in role_based_drafts:
				if role_based_draft.status == False:
					filtered_drafts.append(role_based_draft)

		try:
			drafts = []
			for draft in filtered_drafts:
				if draft.course_subcategory:
					subcategory = {'value':draft.course_subcategory.id, 'label': draft.course_subcategory.name}
				else:
					subcategory = None
				if draft.course_language:
					language = {'value':draft.course_language.id, 'label': draft.course_language.name}
				else:
					language = None
				if draft.is_reviewed == True:
					if draft.status == None:
						status_text = 'Reviewing'
					if draft.status == True:
						status_text = 'Approved'
					if draft.status == False:
						status_text = 'Rejected'
				else:
					status_text = 'Not Reviewed'
				# if draft.is_reviewed == None:
				# 		status_text = 'Reviewing'
				try:
					drafts.append({
						'course_id' : str(draft.id),
						'course_title' : draft.title,
						'subcategory' : subcategory,
						'created_at' : str(draft.created_at),
						'status' : status_text,
						'instructor' : 'Instructor Guroomed',
						# 'is_reviewed' : draft.is_reviewed,
						# 'status' : draft.status,
						# 'language' : language,
						# 'course_subtitle' : draft.subtitle,
						# 'what_will_i_learn' : draft.what_will_i_learn,
						# 'knowledgeRequired' : draft.requirements,
						# 'targetStudent' : draft.description,
					})
				except Exception as e:
					context = {'status':0, 'error':'courseID:'+str(draft.id)+'  '+str(e)}
					drafts.append(context)
		except Exception as e:
			return HttpResponse(json.dumps({'status':0, 'error':str(e)}))
		return HttpResponse(json.dumps({'status':1, 'drafts':drafts}))
		if role.name == 'Admin':
			pass
		if role.name == 'Site Admin':
			pass
	else:
		return HttpResponse(json.dumps({'status':0, 'error':'Use GET method'}))