from django.http import HttpResponse
import simplejson as json
from drafts.models import DraftCourse, CoursesRoles
from courses.models import Subcategory
from guroomed.models import UserInfo
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.models import User, Group
from .forms import RegistrationForm, EditForm
from django.contrib.auth import authenticate
from .models import SubcategoryRoles
from django.shortcuts import render, redirect


# this function will list managers
def listing(request):
    template = 'managers/list_managers.html'
    managers = {}
    if not request.user.is_authenticated: #if user is not logged in
        return render(request, template, {'managers': managers, 'error': 'Please Login'})
    if not (request.user.groups.filter(id=5).exists() or request.user.groups.filter(id=6).exists()): # if user is not site admin or admin
        return render(request, template, {'managers': managers, 'error': 'You are not authorized person'})

    managers = User.objects.filter(groups__name='Course Manager')
    managers = managers.filter(is_active=True)

    if 'error' in request.GET:
        return render(request, template, {'managers': managers, 'error': request.GET['error']})
    if 'msg' in request.GET:
        return render(request, template, {'managers': managers, 'message': request.GET['msg']})
    return render(request, template, {'managers': managers})


# this function will create manager
def create(request):
    template = 'managers/create_manager.html'
    if request.method == 'GET':
        if not request.user.is_authenticated: #if user is not logged in
            return render(request, template, {'error': 'Please Login'})
        if not (request.user.groups.filter(id=5).exists() or request.user.groups.filter(id=6).exists()): # if user is not site admin or admin
            return render(request, template, {'error': 'You are not authorized person'})
        return render(request, template, {})
    if request.method == 'POST':
        try:
            if not request.user.is_authenticated: #if user is not logged in
                return render(request, template, {'error':'Please Login'})
            if not (request.user.groups.filter(id=5).exists() or request.user.groups.filter(id=6).exists()): # if user is not site admin or admin
                return render(request, template, {'error':'You are not authorized person'})
            if 'first_name' not in request.POST or request.POST['first_name'] == '':
                return render(request, template, {'error':'Please enter First Name'})
            if 'last_name' not in request.POST or request.POST['last_name'] == '':
                return render(request, template, {'error':'Please enter Last Name'})
            if 'email' not in request.POST or request.POST['email'] == '':
                return render(request, template, {'error':'Please enter Email'})
            if 'password1' not in request.POST or request.POST['password1'] == '':
                return render(request, template, {'error':'Please enter passsword'})
            if 'password2' not in request.POST or request.POST['password2'] == '':
                return render(request, template, {'error':'Please confirm password'})
            if request.POST['password1'] != request.POST['password2']:
                return render(request, template, {'error': 'Passwords are not same.'})
            form = RegistrationForm(request.POST)
            user = User.objects.filter(email=request.POST['email'])
            if user:
                return render(request, template, {'error': 'Email Id already exists'})
            if form.is_valid():
                form.save()
                user = authenticate(username=request.POST['email'], password=request.POST['password1'])
                group = Group.objects.get(id=7)
                group.user_set.add(user) # assign manager group
                user_info = UserInfo(user_id = user, created_by = request.user)
            else:
                return render(request, template, {'error': 'Invalid Form'})
        except Exception as e:
            return render(request, template, {'error': str(e)})
        return redirect('/api/user/manager/listing/?msg=Manager Added Successfully')
    else:
        return render(request, template, {'error':'Wrong method'})


# this function will edit manager
@csrf_exempt
def edit(request, id):
    template = 'managers/edit_manager.html'
    manager = User.objects.get(id=id)
    if request.method == 'GET':
        if not request.user.is_authenticated: #if user is not logged in
            return render(request, template, {'error': 'Please Login'})
        if not (request.user.groups.filter(id=5).exists() or request.user.groups.filter(id=6).exists()): # if user is not site admin or admin
            return render(request, template, {'error': 'You are not authorized person'})
        return render(request, template, {'manager' : manager})
    if request.method == 'POST':
        manager = User.objects.get(id=id)
        try:
            if not request.user.is_authenticated: #if user is not logged in
                return render(request, template, {'manager' : manager, 'error':'Please Login'})
            if not (request.user.groups.filter(id=5).exists() or request.user.groups.filter(id=6).exists()): # if user is not site admin or admin
                return render(request, template, {'manager' : manager, 'error':'You are not authorized person'})
            if 'first_name' not in request.POST or request.POST['first_name'] == '':
                return render(request, template, {'manager' : manager, 'error':'Please enter First Name'})
            manager.first_name = request.POST['first_name']
            if 'last_name' not in request.POST or request.POST['last_name'] == '':
                return render(request, template, {'manager' : manager, 'error':'Please enter Last Name'})
            manager.last_name = request.POST['last_name']
            if 'email' not in request.POST or request.POST['email'] == '':
                return render(request, template, {'manager' : manager, 'error':'Please enter Email'})
            if manager.email != request.POST['email']:
                user = User.objects.filter(email=request.POST['email'])
                if user:
                    return render(request, template, {'manager' : manager, 'error': 'Email Id already exists'})
            manager.email = request.POST['email']
            form = EditForm(request.POST)
            if form.is_valid():
                manager.save()
            else:
                return render(request, template, {'manager' : manager, 'error': 'Invalid Form'})
        except Exception as e:
            return render(request, template, {'manager' : manager, 'error': str(e)})
        return redirect('/api/user/manager/listing/?msg=Manager Edited Successfully')
    else:
        return render(request, template, {'manager' : manager, 'error':'Wrong method'})


# this function will change manager password
@csrf_exempt
def password(request, id):
    template = 'managers/password_manager.html'
    manager = User.objects.get(id=id)
    if request.method == 'GET':
        if not request.user.is_authenticated: #if user is not logged in
            return render(request, template, {'error': 'Please Login'})
        if not (request.user.groups.filter(id=5).exists() or request.user.groups.filter(id=6).exists()): # if user is not site admin or admin
            return render(request, template, {'error': 'You are not authorized person'})
        return render(request, template, {'manager' : manager})
    if request.method == 'POST':
        try:
            if not request.user.is_authenticated: #if user is not logged in
                return render(request, template, {'error':'Please Login'})
            if not (request.user.groups.filter(id=5).exists() or request.user.groups.filter(id=6).exists()): # if user is not site admin or admin
                return render(request, template, {'manager':manager,'error':'You are not authorized person'})
            if 'password1' not in request.POST or request.POST['password1'] == '':
                return render(request, template, {'manager':manager,'error':'Please enter passsword'})
            if 'password2' not in request.POST or request.POST['password2'] == '':
                return render(request, template, {'manager':manager,'error':'Please confirm password'})
            if request.POST['password1'] != request.POST['password2']:
                return render(request, template, {'manager':manager,'error': 'Passwords are not same.'})
            manager.set_password(request.POST['password2'])
            manager.save()
        except Exception as e:
            return render(request, template, {'error': str(e)})
        return redirect('/api/user/manager/listing/?msg=Password Changed Successfully')
    else:
        return render(request, template, {'error':'Wrong method'})


# this function will delete manager
@csrf_exempt
def delete(request, id):
    template = 'managers/list_managers.html'
    if request.method == 'GET':
        if not request.user.is_authenticated: #if user is not logged in
            return redirect('/api/user/manager/listing/?error=Please Login')
        # if user is not site admin or admin
        if not (request.user.groups.filter(id=5).exists() or request.user.groups.filter(id=6).exists()):
            return redirect('/api/user/manager/listing/?error=You are not authorized person')
        try:
            user = User.objects.get(id = id)
        except User.DoesNotExist:
            return redirect('/api/user/manager/listing/?error=User Does not Exist')
        try:
            user.is_active = False
            user.save()
        except Exception as e:
            return redirect('/api/user/manager/listing/?error='+str(e))
        # return redirect('/api/user/manager/listing/')
        return redirect('/api/user/manager/listing/?msg=Manager Deleted Successfully')
    else:
        return redirect('/api/user/manager/listing/?error=Wrong method')


# this function will assign manager to subcategory
@csrf_exempt
def assign_sub(request, id):
    template = 'managers/assign_sub.html'
    subcategories = Subcategory.objects.all()
    try:
        manager = User.objects.get(id=id)
    except User.DoesNotExist:
        return redirect('/api/user/manager/listing/?error=Manager not Found')
    try:
        selected_sub = SubcategoryRoles.objects.get(user_id = manager.id)
        selected_sub = selected_sub.subcategory_id
    except SubcategoryRoles.DoesNotExist:
        selected_sub = None
    if request.method == 'GET':
        return render(request, template, {'selected_sub':selected_sub,'subcategories':subcategories, 'manager':manager})
            
    if request.method == 'POST':
        if not request.user.is_authenticated: #if user is not logged in
            return render(request, template, {'manager':manager,'error':'Please Login'})
        # if user is not site admin or admin
        if not (request.user.groups.filter(id=5).exists() or request.user.groups.filter(id=6).exists()):
            return render(request, template, {'manager':manager,'error':'You are not authorized person'})
        if 'sub_cat_id' not in request.POST or request.POST['sub_cat_id'] == '':
            return render(request, template, {'manager':manager,'error':'Please select Subcategory'})
        try:
            #assign subcategory
            sub = Subcategory.objects.get(id=request.POST['sub_cat_id'])
            group = Group.objects.get(id=7)
            try:
                cr = SubcategoryRoles.objects.get(user_id = manager.id)
                cr.subcategory_id = sub
            except SubcategoryRoles.DoesNotExist:
                cr = SubcategoryRoles(user_id=manager, subcategory_id=sub, role_type=group)
            cr.save()
        except Exception as e:
            return render(request, template, {'manager':manager,'error':str(e)})
        return redirect('/api/user/manager/listing/?msg=Subcategory assigned Successfully')
    else:
        return render(request, template, {'manager':manager,'error':'Wrong Method'})