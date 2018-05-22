# from django.db import DoesNotExist
from django.shortcuts import render, redirect, get_object_or_404
from .models import FooterStrip


def index(request):
    fstrips = FooterStrip.objects.all()
    context = {'fstrips': fstrips}
    return render(request, 'fstrip/fstriplisting.html', context)

def create(request):
    context = {'request': request}
    return render(request, 'fstrip/addfstrip.html', context)

def store(request):
        fstrip = FooterStrip(title=request.POST['title'], description=request.POST['description'], url=request.POST['url'])
        fstrip.save()
        return redirect('/api/homepage/fstrip')

def edit(request, id):
    fstrip = FooterStrip.objects.get(id=id)
    context = {'fstrip': fstrip}
    return render(request, 'fstrip/editfstrip.html', context)

def update(request, id):
    fstrip = FooterStrip.objects.get(id=id)
    fstrip.title = request.POST['title']
    fstrip.description = request.POST['description']
    fstrip.url = request.POST['url']
    fstrip.save()
    return redirect('/api/homepage/fstrip')

def delete(request, id):
    fstrip = FooterStrip.objects.get(id=id)
    fstrip.delete()
    return redirect('/api/homepage/fstrip')