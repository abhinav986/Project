# Course can have some optional features like - hours_on_demand, supplemental_resources, lifetime_access, access_on_mobile, certificate.
# This file has CRUD for these features.
from django.shortcuts import render, redirect, get_object_or_404
from .models import Include, Course


def index(request):
    includes = Include.objects.all()
    context = {'includes': includes}
    return render(request, 'includes/includelisting.html', context)


def create(request):
    context = {'request': request}
    return render(request, 'includes/addinclude.html', context)


def store(request):
    if request.POST['hours_on_demand'] == '':
        hours_on_demand = 0
    if request.POST['supplemental_resources'] == '':
        supplemental_resources = 0
    if request.POST['lifetime_access'] == '':
        lifetime_access = 0
    if request.POST['access_on_mobile'] == '':
        access_on_mobile = 0
    if request.POST['certificate'] == '':
        certificate = 0
        
    if request.POST['course_id'] == '':
        context = {'error':'Course Id is not sent'}
        return render(request, 'includes/addinclude.html', context)
    try:
        course = Course.objects.get(id=request.POST['course_id'])
    except Course.DoesNotExist:
        context = {'error':'Course Id is not valid'}
        return render(request, 'includes/addinclude.html', context)
    if course:
        include = Include(course_id=course, hours_on_demand=request.POST['hours_on_demand'], supplemental_resources=request.POST['supplemental_resources'], lifetime_access=request.POST['lifetime_access'], access_on_mobile=request.POST['access_on_mobile'], certificate=request.POST['certificate'], )
        include.save()
        return redirect('/courses/includes')


def edit(request, id):
    include = Include.objects.get(id=id)
    context = {'include': include}
    return render(request, 'includes/editinclude.html', context)


def update(request, id):
    if request.POST['hours_on_demand'] == '':
        hours_on_demand = 0
    if request.POST['supplemental_resources'] == '':
        supplemental_resources = 0
    if request.POST['lifetime_access'] == '':
        lifetime_access = 0
    if request.POST['access_on_mobile'] == '':
        access_on_mobile = 0
    if request.POST['certificate'] == '':
        certificate = 0
        
    include = Include.objects.get(id=id)
    if request.POST['course_id'] == '':
        context = {'error':'Course Id is not sent', 'include':include}
        return render(request, 'includes/editinclude.html', context)
    try:
        course = Course.objects.get(id=request.POST['course_id'])
    except Course.DoesNotExist:
        context = {'error':'Course Id is not valid', 'include':include}
        return render(request, 'includes/editinclude.html', context)
    if course:
        include.course_id=course
        include.hours_on_demand=request.POST['hours_on_demand']
        include.supplemental_resources=request.POST['supplemental_resources']
        include.lifetime_access=request.POST['lifetime_access']
        include.access_on_mobile=request.POST['access_on_mobile']
        include.certificate=request.POST['certificate']
        include.save()
        return redirect('/courses/includes')


def delete(request, id):
    include = Include.objects.get(id=id)
    include.delete()
    return redirect('/courses/includes')