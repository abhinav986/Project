# from django.db import DoesNotExist
from django.shortcuts import render, redirect, get_object_or_404, Http404
from .models import Instructor
from django.contrib.auth.models import User, Group
import simplejson as json
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse
from django.contrib.auth import login, authenticate
from .forms import SignupForm
from django.contrib.sites.shortcuts import get_current_site
from django.utils.encoding import force_bytes, force_text
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.template.loader import render_to_string
from .tokens import account_activation_token
from django.core.mail import EmailMessage
from hashlib import sha1


def index(request):
    instructors = Instructor.objects.all()
    context = {'instructors': instructors}
    return render(request, 'instructors/instructorlisting.html', context)


def create(request):
    users = User.objects.filter(groups__name='faculty')
    context = {'request': request, 'users':users}
    return render(request, 'instructors/addinstructor.html', context)


def store(request):
	users = User.objects.filter(groups__name='faculty')
	if request.POST['rating'] == '':
		rating = 0
	else :
		rating = request.POST['rating']
	if request.POST['students'] == '':
		students = 0
	else :
		students = request.POST['students']
	if request.POST['reviews'] == '':
		reviews = 0
	else :
		reviews = request.POST['reviews']
	if request.POST['courses'] == '':
		courses = 0
	else :
		courses = request.POST['courses']
	if 'user_id' not in request.POST:
		context = {'users':users, 'error':'Please Select User'}
		return render(request, 'instructors/addinstructor.html', context)
	try:
		inst = Instructor.objects.get(user_id=request.POST['user_id'])
	except Instructor.DoesNotExist:
		try:
			userid = User.objects.get(id=request.POST['user_id'])
		except User.DoesNotExist:
			context = {'users':users, 'error':'User doesnt exists'}
			return render(request, 'instructors/addinstructor.html', context)
		if userid:
			instruct = Instructor(user_id=userid, rating=rating, students=students, reviews=reviews, courses=courses)
			instruct.save()
			return redirect('/api/courses/instruct')
	if inst:
		context = {'users':users, 'error':'Instructor already exists'}
		return render(request, 'instructors/addinstructor.html', context)


def show(request, id):
    instructor = Instructor.objects.get(id=id)
    context = {'instructor': instructor}
    return render(request, 'instructors/singleinstructor.html', context)


def edit(request, id):
    instructor = Instructor.objects.get(id=id)
    users = User.objects.filter(groups__name='faculty')
    context = {'instructor': instructor, 'users':users}
    return render(request, 'instructors/editinstructor.html', context)


def update(request, id):
	users = User.objects.filter(groups__name='faculty')
	instructor = Instructor.objects.get(id=id)
	if request.POST['rating'] == '':
		rating = 0
	else :
		rating = request.POST['rating']
	if request.POST['students'] == '':
		students = 0
	else :
		students = request.POST['students']
	if request.POST['reviews'] == '':
		reviews = 0
	else :
		reviews = request.POST['reviews']
	if request.POST['courses'] == '':
		courses = 0
	else :
		courses = request.POST['courses']
	if 'user_id' not in request.POST:
		context = {'instructor':instructor, 'users':users, 'error':'Please Select User'}
		return render(request, 'instructors/editinstructor.html', context)
	try:
		inst = Instructor.objects.get(user_id=request.POST['user_id'])
		if inst:
			try:
				inst = Instructor.objects.get(id=id, user_id=request.POST['user_id'])
			except Instructor.DoesNotExist:
				context = {'instructor':instructor, 'users':users, 'error':'Instructor already exists'}
				return render(request, 'instructors/editinstructor.html', context)
	except Instructor.DoesNotExist:
		try:
			userid = User.objects.get(id=request.POST['user_id'])
		except User.DoesNotExist:
			context = {'instructor':instructor, 'users':users, 'error':'User doesnt exists'}
			return render(request, 'instructors/editinstructor.html', context)
		if userid:
			instructor.user_id = userid
	instructor.rating = rating
	instructor.students = students
	instructor.reviews = reviews
	instructor.courses = courses
	instructor.save()
	return redirect('/api/courses/instruct')


def delete(request, id):
    instructor = Instructor.objects.get(id=id)
    instructor.delete()
    return redirect('/api/courses/instruct')

# Any user can be an instructor at any point. For that he needs to sign up instructor form. This function has two options, one for new user and another for existing user. After successfull submission of the form an user will receive an email with confirmation link. On clicking which user will be an instructor.
@csrf_exempt
def instructor_signup(request):
	if request.method == 'POST':
		#if user is loggedin then just confirm the password
		if request.user.is_authenticated: #if user is logged in
			if 'password' not in request.POST:
				return HttpResponse(json.dumps({'status': 0, 'error': 'Please enter Password'}))
			try: #check if password is matching
				user = authenticate(request, username=request.user.username, password=request.POST['password'])
			except Exception as e:
				return HttpResponse(json.dumps({'status': 0, 'error': str(e)}))
			if user == None: #if passowrd is not correct
				return HttpResponse(json.dumps({'status': 0, 'error': 'Password is not correct.'}))
		else: # if user is not loggedin then create a new user and keep him inactive
			if 'email' not in request.POST:
				return HttpResponse(json.dumps({'status': 0, 'error': 'Please enter Email'}))
			if 'password1' not in request.POST:
				return HttpResponse(json.dumps({'status': 0, 'error': 'Please enter Password'}))
			if 'password2' not in request.POST:
				return HttpResponse(json.dumps({'status': 0, 'error': 'Please confirm Password'}))
			if request.POST['password1'] != request.POST['password2']:
				return HttpResponse(json.dumps({'status': 0, 'error': 'Passwords are not matching.'}))
			user = User.objects.filter(email=request.POST['email'])
			if user:
				return HttpResponse(json.dumps({'status': 0, 'error': 'Email Id exists. Please login and try again'}))
			form = SignupForm(request.POST)
			if form.is_valid():
				try:
					user = form.save(commit=False)
					user.is_active = False
					user.save()
				except Exception as e:
					return HttpResponse(json.dumps({'status': 0, 'error':'Not able to create new user'}))
			else:
				return HttpResponse(json.dumps({'status': 0, 'error':'Invalid Form'}))
		try:
			#send confirm-email mail.
			current_site = get_current_site(request)
			mail_subject = 'Activate your Guroomed - Instructor Account.'

			# check where to redirect
			if '127.0.0.1' not in request.build_absolute_uri('/'):
				server_url = request.build_absolute_uri('/')
			else:
				server_url = 'http://localhost:4200/'

			#prepare the confirm email template
			message = render_to_string('instructors/confirm_email.html', {
				'user': user,
				'url': server_url+'#/instructor/login/instructor-login?uidb64='+urlsafe_base64_encode(force_bytes(user.pk)).decode()+'&token='+account_activation_token.make_token(user)
			})
			to_email = user.email
			email = EmailMessage( mail_subject, message, to=[to_email] )
			email.send()
		except Exception as e:
			return HttpResponse(json.dumps({'status': 0, 'error':str(e)}))
		return HttpResponse(json.dumps({'status': 1, 'msg':'Please check your email and confirm your email address to complete the registration'}))

	else:# if method is not post
		return HttpResponse(json.dumps({'status': 0, 'error':'Invalid Method'}))


# Once an user will receive confirmation mail on submitting form for an instructor, and he will click on the link in the mail, token will be validated and user will be confirmed. User will belong to Instructor group
@csrf_exempt
def activate(request, uidb64, token):
	try:
		uid = urlsafe_base64_decode(uidb64).decode()
		user = User.objects.get(pk=uid)
	except(TypeError, ValueError, OverflowError, User.DoesNotExist):
		user = None
	if user is not None and account_activation_token.check_token(user, token):
		try:
			user.is_active = True
			user.save()
			group = Group.objects.get(id=1)
			group.user_set.add(user) # assign instructor group
			# create instance of instructor for that user
			instruct = Instructor(user_id=user, rating=0, students=0, reviews=0, courses=0)
			instruct.save()
			login(request, user, 'django.contrib.auth.backends.ModelBackend')
		except Exception as e:
			return HttpResponse(json.dumps({'status': 0, 'error':str(e)}))
		return HttpResponse(json.dumps({'status': 1, 'msg':'Thank you for your email confirmation. Now you can login your account'}))
	else:
		return HttpResponse(json.dumps({'status': 0, 'error':'Activation link is invalid!'}))