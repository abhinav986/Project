from django.shortcuts import render, redirect, get_object_or_404
from .models import Tag


def index(request):
    tags = Tag.objects.all()
    context = {'tags': tags}
    return render(request, 'tags/taglisting.html', context)

def create(request):
    context = {'request': request}
    return render(request, 'tags/addtag.html', context)

def store(request):
    if request.POST['name'] == '':
        context = {'error':'Please Enter Name'}
        return render(request, 'tags/addtag.html', context)
    try:
        tag = Tag.objects.get(name=request.POST['name'])
    except Tag.DoesNotExist:
        tag = Tag(name=request.POST['name'])
        tag.save()
        return redirect('/api/courses/tag')
    if tag:
        context = {'error':request.POST['name']+' Tag already exists'}
        return render(request, 'tags/addtag.html', context)

def edit(request, id):
    tag = Tag.objects.get(id=id)
    context = {'tag': tag}
    return render(request, 'tags/edittag.html', context)

def update(request, id):
    tag = Tag.objects.get(id=id)
    if request.POST['name'] == '':
        context = {'tag':tag,'error':'Please Enter Name'}
        return render(request, 'tags/edittag.html', context)
    try:
        newtag = Tag.objects.get(name=request.POST['name'])
    except Tag.DoesNotExist:
        tag.name = request.POST['name']
        tag.save()
        return redirect('/api/courses/tag')
    if newtag:
        context = {'tag':tag,'error':request.POST['name']+' Tag already exists'}
        return render(request, 'tags/edittag.html', context)

def delete(request, id):
    tag = Tag.objects.get(id=id)
    tag.delete()
    return redirect('/api/courses/tag')