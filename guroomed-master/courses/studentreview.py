from django.shortcuts import render, redirect, get_object_or_404
from .models import Course, StudentReview as SR
from django.contrib.auth.models import User


def index(request):
    srs = SR.objects.all()
    context = {'srs': srs}
    return render(request, 'studentreview/srlisting.html', context)

def create(request):
    context = {'request': request}
    return render(request, 'studentreview/addsr.html', context)

def store(request):
    course = Course.objects.get(id=request.POST['course_id'])
    user = User.objects.get(id=request.POST['user_id'])
    sr = SR(course_id=course, user_id=user, no_of_stars=request.POST['no_of_stars'], about_the_course=request.POST['about_the_course'], about_the_instructor=request.POST['about_the_instructor'], how_course_can_improved=request.POST['how_course_can_improved'], review=request.POST['review'])
    sr.save()
    return redirect('/courses/studentreview')

def edit(request, id):
    sr = SR.objects.get(id=id)
    context = {'sr': sr}
    return render(request, 'studentreview/editsr.html', context)

def update(request, id):
    course = Course.objects.get(id=request.POST['course_id'])
    user = User.objects.get(id=request.POST['user_id'])
    sr = SR.objects.get(id=id)
    sr.course_id = course
    sr.user_id = user
    sr.no_of_stars=request.POST['no_of_stars']
    sr.about_the_course=request.POST['about_the_course']
    sr.about_the_instructor=request.POST['about_the_instructor']
    sr.how_course_can_improved=request.POST['how_course_can_improved']
    sr.review=request.POST['review']
    sr.save()
    return redirect('/courses/studentreview')

def delete(request, id):
    sr = SR.objects.get(id=id)
    sr.delete()
    return redirect('/courses/studentreview')