from django.shortcuts import render, redirect, get_object_or_404
from .models import Course, InProgress, UserCourses as UC
from django.contrib.auth.models import User


def index(request):
    ucs = UC.objects.all()
    context = {'ucs': ucs}
    return render(request, 'usercourses/uclisting.html', context)

def create(request):
    context = {'request': request}
    return render(request, 'usercourses/adduc.html', context)

def store(request):
    course = Course.objects.get(id=request.POST['course_id'])
    user = User.objects.get(id=request.POST['user_id'])
    # inprogress = InProgress.objects.get(id=request.POST['in_progress'])
    uc = UC(course_id=course, user_id=user, taught_learned=request.POST['taught_learned'], is_favourite=request.POST['is_favourite'])
    uc.save()
    return redirect('/api/usercourses')

def store_frontend(course_id, user_id, purpose, isFav):
    course = Course.objects.get(course_id)
    user = User.objects.get(user_id)
    uc = UC(course_id=course, user_id=user, taught_learned=purpose, is_favourite=isFav)
    uc.save()


def edit(request, id):
    uc = UC.objects.get(id=id)
    context = {'uc': uc}
    return render(request, 'usercourses/edituc.html', context)

def update(request, id):
    course = Course.objects.get(id=request.POST['course_id'])
    user = User.objects.get(id=request.POST['user_id'])
    inprogress = InProgress.objects.get(id=request.POST['in_progress'])
    uc = UC.objects.get(id=id)
    uc.course_id = course
    uc.user_id = user
    uc.taught_learned=request.POST['taught_learned']
    uc.is_favourite=request.POST['is_favourite']
    uc.in_progress=inprogress
    uc.save()
    return redirect('/api/usercourses')

def delete(request, id):
    uc = UC.objects.get(id=id)
    uc.delete()
    return redirect('/api/usercourses')