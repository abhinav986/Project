from django.shortcuts import render, redirect, get_object_or_404
from .models import Course, CurriculumSection as CS
from . import curriculumlecture as curLec
from django.http import HttpResponse
from guroomed.models import UserCourses

def index(request):
    cs = CS.objects.all()
    context = {'css': cs}
    return render(request, 'curriculumsec/cslisting.html', context)

def create(request):
    courses = Course.objects.all().order_by('id')
    context = {'courses': courses}
    return render(request, 'curriculumsec/addcs.html', context)

def store(request):
    if request.POST['title'] == '':
        context = {'error':'Please Enter Title'}
        return render(request, 'includes/addcs.html', context)
    for cs in CS.objects.all().filter(course_id = request.POST['course_id']):
        if cs.order_num == request.POST['order_num']:
            context = {'error':'Order Number exists already'}
            return render(request, 'includes/addcs.html', context)
    if request.POST['order_num'] == '':
        context = {'error':'Please Enter Order Number'}
        return render(request, 'includes/addcs.html', context)
    if request.POST['course_id'] == '':
        context = {'error':'Please Enter Course Id'}
        return render(request, 'includes/addcs.html', context)
    if request.POST['no_lectures'] == '':
        context = {'error':'Please Enter Number of Lectures'}
        return render(request, 'includes/addcs.html', context)
    if request.POST['duration'] == '':
        context = {'error':'Please Enter Duration'}
        return render(request, 'includes/addcs.html', context)
    try:
        course = Course.objects.get(id=request.POST['course_id'])
    except Course.DoesNotExist:
        context = {'error':'Course Id is not valid'}
        return render(request, 'includes/addcs.html', context)
    if course:
        cs = CS(course_id=course, title=request.POST['title'], order_num=request.POST['order_num'], no_lectures=request.POST['no_lectures'], duration=request.POST['duration'])
        cs.save()
        return redirect('/api/courses/curriculumsec')

def show(request, id):
    cs = CS.objects.all().filter(course_id=id)
    curriculumSec = []
    myCourse = UserCourses.objects.all().filter(user_id=request.user.id, course_id=id)
    if myCourse:
        flag = 1
    else:
        flag = 0
    for curriculum in cs:
        curriculumLect = curLec.show(request, curriculum.id, flag)
        # return HttpResponse(curriculumLect)

        curriculumSec.append({
            'title':curriculum.title,
            'curriculumLect':curriculumLect,
            'order_num':curriculum.order_num,
            'no_lectures':curriculum.no_lectures,
            'duration':str(curriculum.duration),
        })
    return curriculumSec

def edit(request, id):
    cs = CS.objects.get(id=id)
    context = {'cs': cs}
    return render(request, 'curriculumsec/editcs.html', context)

def update(request, id):
    if request.POST['title'] == '':
        context = {'error':'Please Enter Title'}
        return render(request, 'includes/editcs.html', context)
    if request.POST['order_num'] == '':
        context = {'error':'Please Enter Order Number'}
        return render(request, 'includes/editcs.html', context)
    if request.POST['course_id'] == '':
        context = {'error':'Course Id is not sent'}
        return render(request, 'includes/editcs.html', context)
    try:
        course = Course.objects.get(id=request.POST['course_id'])
    except Course.DoesNotExist:
        context = {'error':'Course Id is not valid'}
        return render(request, 'includes/editcs.html', context)
    if course:
        cs = CS.objects.get(id=id)
        cs.course_id = course
        cs.title=request.POST['title']
        cs.order_num=request.POST['order_num']
        cs.save()
        return redirect('/api/courses/curriculumsec')

def delete(request, id):
    cs = CS.objects.get(id=id)
    cs.delete()
    return redirect('/api/courses/curriculumsec')