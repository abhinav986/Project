# from django.db import DoesNotExist
from django.shortcuts import render, redirect, get_object_or_404
from .models import Infostrip


def index(request):
    infostrips = Infostrip.objects.all()
    context = {'infostrips': infostrips}
    return render(request, 'infostrip/infostriplisting.html', context)

def create(request):
    context = {'request': request}
    return render(request, 'infostrip/addinfostrip.html', context)

def store(request):
    infostrips = Infostrip.objects.all()
    for info in infostrips:
        if info.title == request.POST['title']:
            context = {'error':request.POST['title']+' Infostrip already exists'}
            return render(request, 'infostrip/addinfostrip.html', context)
        if info.subtitle == request.POST['subtitle']:
            context = {'error':request.POST['subtitle']+' Infostrip already exists'}
            return render(request, 'infostrip/addinfostrip.html', context)
    infostrip = Infostrip(icon=request.POST['icon'], title=request.POST['title'], subtitle=request.POST['subtitle'], )
    infostrip.save()
    return redirect('/api/homepage/infostrip')

def edit(request, id):
    infostrip = Infostrip.objects.get(id=id)
    context = {'infostrip': infostrip}
    return render(request, 'infostrip/editinfostrip.html', context)

def update(request, id):
    infostrip = Infostrip.objects.get(id=id)
    infostrips = Infostrip.objects.all().exclude(id=id)
    for info in infostrips:
        if info.title == request.POST['title']:
            context = {'error':request.POST['title']+' Infostrip already exists','infostrip':infostrip}
            return render(request, 'infostrip/editinfostrip.html', context)
        if info.subtitle == request.POST['subtitle']:
            context = {'error':request.POST['subtitle']+' Infostrip already exists','infostrip':infostrip}
            return render(request, 'infostrip/editinfostrip.html', context)
    infostrip.icon = request.POST['icon']
    infostrip.title = request.POST['title']
    infostrip.subtitle = request.POST['subtitle']
    infostrip.save()
    return redirect('/api/homepage/infostrip')

def delete(request, id):
    infostrip = Infostrip.objects.get(id=id)
    infostrip.delete()
    return redirect('/api/homepage/infostrip')