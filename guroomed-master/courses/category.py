from django.shortcuts import render, redirect, get_object_or_404
from .models import Category


def index(request):
    categories = Category.objects.all()
    context = {'categories': categories}
    return render(request, 'categories/categorylisting.html', context)

def create(request):
    context = {'request': request}
    return render(request, 'categories/addcategory.html', context)

def store(request):
    if request.POST['name'] == '':
        context = {'error':'Please Enter Name'}
        return render(request, 'categories/addcategory.html', context)
    try:
        cat = Category.objects.get(name=request.POST['name'])
    except Category.DoesNotExist:
        category = Category(name=request.POST['name'])
        category.save()
        return redirect('/api/courses/cat')
    if cat:
        context = {'error':request.POST['name']+' Category already exists'}
        return render(request, 'categories/addcategory.html', context)

def edit(request, id):
    category = Category.objects.get(id=id)
    context = {'category': category}
    return render(request, 'categories/editcategory.html', context)

def update(request, id):
    category = Category.objects.get(id=id)
    if request.POST['name'] == '':
        context = {'category':category,'error':'Please Enter Name'}
        return render(request, 'categories/editcategory.html', context)
    try:
        cat = Category.objects.get(name=request.POST['name'])
    except Category.DoesNotExist:
        category.name = request.POST['name']
        category.save()
        return redirect('/api/courses/cat')
    if cat:
        context = {'category':category,'error':request.POST['name']+' Category already exists'}
        return render(request, 'categories/editcategory.html', context)

def delete(request, id):
    category = Category.objects.get(id=id)
    category.delete()
    return redirect('/api/courses/cat')