from django.shortcuts import render, redirect, get_object_or_404
from .models import UserInfo
from Courses.models import Language


def index(request):
    languages = Language.objects.all()
    context = {'languages': languages}
    return render(request, 'languages/languagelisting.html', context)

def create(request):
    context = {'request': request}
    return render(request, 'languages/addlanguage.html', context)

def store(request):
    if request.POST['name'] == '':
        context = {'error':'Please Enter Name'}
        return render(request, 'languages/addlanguage.html', context)
    try:
        lang = Language.objects.get(name=request.POST['name'])
    except Language.DoesNotExist:
        language = Language(name=request.POST['name'])
        language.save()
        return redirect('/courses/lang')
    if lang:
        context = {'error':request.POST['name']+' Language already exists'}
        return render(request, 'languages/addlanguage.html', context)

def edit(request, id):
    language = Language.objects.get(id=id)
    context = {'language': language}
    return render(request, 'languages/editlanguage.html', context)

def update(request, id):
    language = Language.objects.get(id=id)
    if request.POST['name'] == '':
        context = {'error':'Please Enter Name','language':language}
        return render(request, 'languages/editlanguage.html', context)
    try:
        lang = Language.objects.get(name=request.POST['name'])
    except Language.DoesNotExist:
        language.name = request.POST['name']
        language.save()
        return redirect('/courses/lang')
    if lang:
        context = {'error':request.POST['name']+' Language already exists','language':language}
        return render(request, 'languages/editlanguage.html', context)

def delete(request, id):
    language = Language.objects.get(id=id)
    language.delete()
    return redirect('/courses/lang')