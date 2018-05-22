from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from django.conf import settings
from django.contrib.auth import authenticate, login, logout, update_session_auth_hash
from django.contrib import messages
from .forms import RegistrationForm
from django.contrib.auth.forms import PasswordChangeForm
import json, requests
from django.urls import reverse
import jwt
import simplejson as json
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.models import User
from django.contrib.auth.forms import (
    AuthenticationForm, PasswordChangeForm, PasswordResetForm, SetPasswordForm,
)
from django.contrib.auth.tokens import default_token_generator


def frontendRoutes(request, path):
	template = loader.get_template('guroomed/frontend.html')
	context = {'request' : request, 'path':path}
	return HttpResponse(template.render(context))

@csrf_exempt
def password_reset(request,
                   template_name='registration/password_reset_form.html',
                   email_template_name='registration/password_reset_email.html',
                   subject_template_name='registration/password_reset_subject.txt',
                   password_reset_form=PasswordResetForm,
                   token_generator=default_token_generator,
                   post_reset_redirect=None,
                   from_email=None,
                   extra_context=None,
                   html_email_template_name=None,
                   extra_email_context=None):

    if post_reset_redirect is None:
        post_reset_redirect = reverse('password_reset_done')
    else:
        post_reset_redirect = resolve_url(post_reset_redirect)
    if request.method == "POST":
        form = password_reset_form(request.POST)
        if form.is_valid():
            opts = {
                'use_https': request.is_secure(),
                'token_generator': token_generator,
                'from_email': from_email,
                'email_template_name': email_template_name,
                'subject_template_name': subject_template_name,
                'request': request,
                'html_email_template_name': html_email_template_name,
                'extra_email_context': extra_email_context,
            }
            form.save(**opts)
            return HttpResponse(json.dumps({'status': 1, 'msg':'Check Email and click on reset link'}))
    else:
        form = password_reset_form()
    context = {
        'form': form,
        'title': 'Password reset',
    }
    if extra_context is not None:
        context.update(extra_context)

    return TemplateResponse(request, template_name, context)

@csrf_exempt
def password_reset_confirm(request, uidb64=None, token=None,
                           template_name='registration/password_reset_confirm.html',
                           token_generator=default_token_generator,
                           set_password_form=SetPasswordForm,
                           post_reset_redirect=None,
                           extra_context=None):
	assert uidb64 is not None and token is not None  # checked by URLconf
	if post_reset_redirect is None:
		post_reset_redirect = reverse('password_reset_complete')
	else:
		post_reset_redirect = resolve_url(post_reset_redirect)
	try:
	# urlsafe_base64_decode() decodes to bytestring on Python 3
		uid = force_text(urlsafe_base64_decode(uidb64))
		user = UserModel._default_manager.get(pk=uid)
	except (TypeError, ValueError, OverflowError, NameError):
		user = None

	if user is not None and token_generator.check_token(user, token):
		validlink = True
		title = _('Enter new password')
		if request.method == 'POST':
			form = set_password_form(user, request.POST)
			if form.is_valid():
				form.save()
				return HttpResponseRedirect(post_reset_redirect)
		else:
			form = set_password_form(user)
	else:
		validlink = False
		form = None
		title = 'Password reset unsuccessful'
    # context = {
    #     'form': form,
    #     'title': title,
    #     'validlink': validlink,
    # }
	if validlink == 'False':
		return HttpResponse(json.dumps({'status': 0, 'error':'Invalid Link'}))
	else:
		return HttpResponse(json.dumps({'status': 1}))
    # if extra_context is not None:
    #     context.update(extra_context)

    # return TemplateResponse(request, template_name, context)

@csrf_exempt
def password_change(request):
	if not request.user.is_authenticated:
		return HttpResponse(json.dumps({'status': 0, 'error': 'You are not loggedin'}))
	if 'password1' not in request.POST:
		return HttpResponse(json.dumps({'status': 0, 'error': 'Enter Old Password'}))
	if 'password2' not in request.POST:
		return HttpResponse(json.dumps({'status': 0, 'error': 'Enter New Password'}))
	u = request.user
	if u.check_password(request.POST['password1']):
		u.set_password(request.POST['password2'])
		u.save()
		return HttpResponse(json.dumps({'status': 1, 'msg': 'Password Changed'}))
	else:
		return HttpResponse(json.dumps({'status': 0, 'error': 'Wrong Old Password'}))

def verify_jwt(request):
    if 'access_token' in request:
        encoded = request.access_token
        decoded = jwt.decode(encoded, 'guroomed', algorithms=['HS256'])
        if decoded['username'] == request.user.username:
        	return HttpResponse(json.dumps({'status': 1}))
        else:
            return HttpResponse(json.dumps({'status': 0, 'error':'Wrong JWT Token Received'}))
    else :
        return HttpResponse(json.dumps({'status': 0, 'error':'No JWT Token Received'}))


@csrf_exempt
def frontend_login(request):
	if 'username' not in request.POST:
		return HttpResponse(json.dumps({'status': 0, 'error': 'Enter Username'}))
	else:
		username = request.POST['username']
	if 'password' not in request.POST:
		return HttpResponse(json.dumps({'status': 0, 'error': 'Enter Password'}))
	else:
		password = request.POST['password']

	user = authenticate(request, username=username, password=password)
	if user:
		group = None
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
		login(request, user)
		encoded = jwt.encode({'username': user.username,'user_id': user.id,'group_name': group}, 'guroomed', algorithm='HS256')
		return HttpResponse(json.dumps({'status': 1, 'access_token': encoded}))
	else:
		return HttpResponse(json.dumps({'status': 0, 'error': 'Wrong Credentials'}))


def custom_signup(request):
	if request.method == 'POST':
		form = RegistrationForm(request.POST)
		if form.is_valid():
			form.save()
			username = form.cleaned_data.get('email')
			raw_password = form.cleaned_data.get('password1')
			user = authenticate(username=username, password=raw_password)
			login(request, user)
			return redirect('/api/')
		else:
			return HttpResponse('Something went wrong')
	else:
		form = RegistrationForm()
	return render(request, 'guroomed/signup.html', {'form': form})

@csrf_exempt
def frontend_signup(request):
	if request.method == 'POST':
		user = User.objects.filter(email=request.POST['email'])
		if user:
			return HttpResponse(json.dumps({'status': 0, 'error': 'Email Id existing'}))
		if request.POST['password1'] != request.POST['password2']:
			return HttpResponse(json.dumps({'status': 0, 'error': 'Passwords are not same.'}))
		form = RegistrationForm(request.POST)
		if form.is_valid():
			form.save()
			username = form.cleaned_data.get('email')
			raw_password = form.cleaned_data.get('password1')
			user = authenticate(username=username, password=raw_password)
			login(request, user)
			return HttpResponse(json.dumps({'status': 1, 'user_id': user.id}))
		else:
			return HttpResponse(json.dumps({'status': 0, 'error': 'Invalid'}))
	else:
		form = RegistrationForm()
	return render(request, 'guroomed/signup.html', {'form': form})


def custom_login(request):
	if 'username' not in request.POST:
		return redirect('/api/login?msg=failed&redirect='+request.POST['redirect'])
	else:
		username = request.POST['username']
	if 'password' not in request.POST:
		return redirect('/api/login?msg=failed&redirect='+request.POST['redirect'])
	else:
		password = request.POST['password']
	
	# url = request.scheme+'://'+request.get_host()+reverse('jwttoken')
	# data = {'username': username, 'password': password}
	# headers = {'Content-type': 'application/json', 'Accept': 'text/plain'}
	# r = (requests.post(url,data=data)).text

	# try:
	# 	jwt_token = json.loads(r)['token']
	# 	return HttpResponse(jwt_token)
	# except KeyError:
	# 	error = json.loads(r)['non_field_errors']
	# if error:
	# 	return HttpResponse(error)
	user = authenticate(request, username=username, password=password)
	if user is not None:
		# encoded = jwt.encode({'username': request.POST['username'],'user_id': user.id}, 'guroomed', algorithm='HS256')
		response = HttpResponseRedirect(request.POST['redirect'])
		# response.set_cookie('encoded_jwt', encoded)

		login(request, user)
		if 'redirect' not in request.POST:
			return redirect('/api/')
		else:
			# return redirect(request.POST['redirect'])
			return response
	else:
		return redirect('/api/login?msg=failed&redirect='+request.POST['redirect'])


def login_form(request):
	if request.GET.get('msg'):
		m = "Username or Password is incorrect"
		if request.GET.get('redirect'):
			redirect = request.GET['redirect']# get the previous url
	else:
		m = ''
		redirect = request.META.get('HTTP_REFERER') # get the previous url


	template = loader.get_template('guroomed/login.html')
	context = {'message' : m, 'redirect':redirect}
	return HttpResponse(template.render(context, request))


def custom_logout(request):
	logout(request)
	response = HttpResponseRedirect('/api/')
	return response


@csrf_exempt
def frontend_logout(request):
	if request.method == 'GET':
		try:
			logout(request)
		except Exception as e:
			context = {'status':0, 'error':str(e)}
		context = {'status':1, 'msg':'Loggedout scuccessfuly'}
		# response.delete_cookie('encoded_jwt', '')
	else:
		context = {'status':0, 'error':'Not correct method'}
	return HttpResponse(json.dumps(context))


def change_password(request):
    if request.method == 'POST':
        form = PasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request, user)  # Important!
            messages.success(request, 'Your password was successfully updated!')
            return redirect('/api/')
        else:
            messages.error(request, 'Please correct the error below.')
    else:
        form = PasswordChangeForm(request.user)
    return render(request, 'guroomed/changepd.html', {
        'form': form
    })


def frontend(request):
	template = loader.get_template('guroomed/frontend.html')
	context = {'request' : request}
	return HttpResponse(template.render(context))

def index(request):
	template = loader.get_template('guroomed/index.html')
	context = {'request' : request}
	return HttpResponse(template.render(context))


def notes_group(request):
	groups = request.user.groups.all()
	output = []
	for group in groups:
		if group.name == 'zen_student':
			var = 'false'
		elif group.name == 'faculty':
			var = 'false'
		else:
			output.append(group)
	template = loader.get_template('guroomed/viewgroup.html')
	context = {'output' : output}
	return HttpResponse(template.render(context, request)) 

	
def notes_list(request,group):
	output = Note.objects.filter(note_group = group).order_by('-pub_date')
	output = reversed(output)
	template = loader.get_template('guroomed/viewnotes.html')
	context = {'output' : output}
	return HttpResponse(template.render(context, request))