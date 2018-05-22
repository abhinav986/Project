from django.http import HttpResponse
import simplejson as json
from courses.models import Subcategory
from guroomed.models import UserInfo
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.models import User, Group
from .forms import RegistrationForm
from django.contrib.auth import authenticate
from .models import SubcategoryRoles


# this function will list reviewers
@csrf_exempt
def listing(request, manager_id=0, sub_cat_id=0):
	if request.method == 'GET':
		if not request.user.is_authenticated: #if user is not logged in
			return HttpResponse(json.dumps({'status':0, 'error':'Please Login'}))
		if not (request.user.groups.filter(id=5).exists() or request.user.groups.filter(id=6).exists() or request.user.groups.filter(id=7).exists()): # if user is not manager, site admin or admin
			return HttpResponse(json.dumps({'status':0, 'error':'You are not authorized person'}))
		try:
			reviewers = []
			if manager_id != str(0):
				# info of users created by manager with id manager_id
				reviewers_info = UserInfo.objects.filter(created_by=manager_id)
				for reviewer_info in reviewers_info: 
					reviewers.append(reviewer_info.user_id)
			if sub_cat_id != str(0):
				pass
			if sub_cat_id == str(0) and manager_id == str(0):
				reviewers = User.objects.filter(groups__name='Course Reviewer')
			reviewers_data = []
			for reviewer in reviewers:
				if sub_cat_id == str(0) and manager_id == str(0):
					sub_cat = None
				else:
					sub_cat = SubcategoryRoles.objects.get(user_id=reviewer.id)
				reviewers_data.append({
					'id' : reviewer.id,
					'name' : reviewer.first_name +' '+ reviewer.last_name,
					'email' : reviewer.email,
					# 'username' : reviewer.username,
					# 'date_joined' : str(reviewer.date_joined),
					# 'subcategory' : sub_cat.subcategory_id.name
				})
		except Exception as e:
			return HttpResponse(json.dumps({'status':0, 'error':str(e)}))
		return HttpResponse(json.dumps({'status':1, 'reviewers':reviewers_data}))
	else:
		return HttpResponse(json.dumps({'status':0, 'error':'Wrong method'}))


@csrf_exempt
def create(request):
	if request.method == 'GET':
		sub_cats = []
		for sub_cat in Subcategory.objects.all():
			sub_cats.append({
			'value' : sub_cat.id,
			'label' : sub_cat.name,
			})
		return HttpResponse(json.dumps({
			'sub_cats': sub_cats,
		}))
	if request.method == 'POST':
		try:
			if not request.user.is_authenticated: #if user is not logged in
				return HttpResponse(json.dumps({'status':0, 'error':'Please Login'}))
			if not (request.user.groups.filter(id=5).exists() or request.user.groups.filter(id=6).exists() or request.user.groups.filter(id=7).exists()): # if user is not manager, site admin or admin
				return HttpResponse(json.dumps({'status':0, 'error':'You are not authorized person'}))
			if 'first_name' not in request.POST:
				return HttpResponse(json.dumps({'status':0, 'error':'Please enter First Name'}))
			if 'last_name' not in request.POST:
				return HttpResponse(json.dumps({'status':0, 'error':'Please enter Last Name'}))
			if 'email' not in request.POST:
				return HttpResponse(json.dumps({'status':0, 'error':'Please enter Email'}))
			if 'password1' not in request.POST:
				return HttpResponse(json.dumps({'status':0, 'error':'Please enter passsword'}))
			if 'password2' not in request.POST:
				return HttpResponse(json.dumps({'status':0, 'error':'Please confirm password'}))
			if 'sub_cat_id' not in request.POST:
				return HttpResponse(json.dumps({'status':0, 'error':'Please select Subcategory'}))
			if request.POST['password1'] != request.POST['password2']:
				return HttpResponse(json.dumps({'status': 0, 'error': 'Passwords are not same.'}))
			form = RegistrationForm(request.POST)
			user = User.objects.filter(email=request.POST['email'])
			if user:
				return HttpResponse(json.dumps({'status': 0, 'error': 'Email Id already exists'}))
			if form.is_valid():
				form.save()
				user = authenticate(username=request.POST['email'], password=request.POST['password1'])
				user_info = UserInfo(user_id=user, created_by=request.user)
				user_info.save()
				group = Group.objects.get(id=8)
				group.user_set.add(user) # assign instructor group
				# assign subcategory
				sub = Subcategory.objects.get(id = request.POST['sub_cat_id'])
				cr = SubcategoryRoles(user_id=user, subcategory_id=sub, role_type=group)
				cr.save()
			else:
				return HttpResponse(json.dumps({'status': 0, 'error': 'Invalid Form'}))
		except Exception as e:
			return HttpResponse(json.dumps({'status': 0, 'error': str(e)}))
		return HttpResponse(json.dumps({'status': 1, 'msg': 'Reviewer has been created'}))
	else:
		return HttpResponse(json.dumps({'status':0, 'error':'Wrong method'}))


# this function will edit reviewer
@csrf_exempt
def edit(request, id):
	if request.method == 'GET':
		if not request.user.is_authenticated: #if user is not logged in
			return HttpResponse(json.dumps({'status':0, 'error':'Please Login'}))
		if not (request.user.groups.filter(id=5).exists() or request.user.groups.filter(id=6).exists() or request.user.groups.filter(id=7).exists()): # if user is not manager, site admin or admin
			return HttpResponse(json.dumps({'status':0, 'error':'You are not authorized person'}))
		sub_cats = []
		for sub_cat in Subcategory.objects.all():
			sub_cats.append({
			'value' : sub_cat.id,
			'label' : sub_cat.name,
			})
		try:
			user = User.objects.get(id = id)
		except User.DoesNotExist:
			return HttpResponse(json.dumps({'status':0, 'error':'User Does not Exist'}))
		try:
			sub = SubcategoryRoles.objects.get(user_id=user.id)
			subcategory = sub.subcategory_id.name
		except SubcategoryRoles.DoesNotExist:
			subcategory = None
		user_info = {
			'id' : user.id,
			'first_name' : user.first_name,
			'last_name' : user.last_name,
			'email' : user.email,
			'username' : user.username,
			'subcategory' : subcategory
		}
		return HttpResponse(json.dumps({
			'sub_cats': sub_cats,
			'user': user_info
		}))
	else:
		return HttpResponse(json.dumps({'status':0, 'error':'Wrong method'}))


# this function will edit reviewer
@csrf_exempt
def delete(request, id):
	if request.method == 'DELETE':
		if not request.user.is_authenticated: #if user is not logged in
			return HttpResponse(json.dumps({'status':0, 'error':'Please Login'}))
		if not (request.user.groups.filter(id=5).exists() or request.user.groups.filter(id=6).exists() or request.user.groups.filter(id=7).exists()): # if user is not manager, site admin or admin
			return HttpResponse(json.dumps({'status':0, 'error':'You are not authorized person'}))
		try:
			user = User.objects.get(id = id)
		except User.DoesNotExist:
			return HttpResponse(json.dumps({'status':0, 'error':'User Does not Exist'}))
		try:
			user.delete()
		except Exception as e:
			return HttpResponse(json.dumps({'status':0, 'error':str(e)}))
		return HttpResponse(json.dumps({'status':1, 'msg':'Reviewer Deleted Successfully'}))
	else:
		return HttpResponse(json.dumps({'status':0, 'error':'Wrong method'}))