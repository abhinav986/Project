from django.shortcuts import render, redirect, get_object_or_404
from .models import InProgress
from courses.models import CurriculumLecture
from django.contrib.auth.models import User


def index(request):
    ips = InProgress.objects.all()
    context = {'ips': ips}
    return render(request, 'inprogress/iplisting.html', context)

def create(request):
    context = {'request': request}
    return render(request, 'inprogress/addip.html', context)

def store(request):
    courses_lecture = CurriculumLecture.objects.get(id=request.POST['courses_lecture_id'])
    inprogress = InProgress(courses_lecture_id=courses_lecture, watching_video_duration=request.POST['watching_video_duration'])
    inprogress.save()
    return redirect('/inprogress')

def edit(request, id):
    inprogress = InProgress.objects.get(id=id)
    context = {'inprogress': inprogress}
    return render(request, 'inprogress/editip.html', context)

def update(request, id):
    courses_lecture = CurriculumLecture.objects.get(id=request.POST['courses_lecture_id'])
    inprogress = InProgress.objects.get(id=id)
    inprogress.courses_lecture_id = courses_lecture
    inprogress.watching_video_duration=request.POST['watching_video_duration']
    inprogress.save()
    return redirect('/inprogress')

def delete(request, id):
    inprogress = InProgress.objects.get(id=id)
    inprogress.delete()
    return redirect('/inprogress')