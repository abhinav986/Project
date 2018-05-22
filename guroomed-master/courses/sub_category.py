from django.shortcuts import render, redirect, get_object_or_404
from .models import Subcategory, Category


def index(request):
    sub_categories = Subcategory.objects.all()
    context = {'sub_categories': sub_categories}
    return render(request, 'subcategories/subcategorylisting.html', context)

def create(request):
    categories = Category.objects.all()
    context = {'categories': categories}
    return render(request, 'subcategories/addsubcategory.html', context)

def store(request):
    categories = Category.objects.all()
    if 'course_category_id' not in request.POST:
        context = {'categories':categories,'name':request.POST['name'],'error':'Please Select Category'}
        return render(request, 'subcategories/addsubcategory.html', context)
    else:
        category = get_object_or_404(Category, pk=request.POST['course_category_id'])
        if request.POST['name'] == '':
            context = {'categories':categories,'error':'Please Enter Name','category':category}
            return render(request, 'subcategories/addsubcategory.html', context)
        try:
            subcat = Subcategory.objects.get(name=request.POST['name'])
        except Subcategory.DoesNotExist:
            subcategory = Subcategory(course_category_id=category, name=request.POST['name'])
            subcategory.save()
            return redirect('/api/courses/subcat')
        if subcat:
            context = {'categories':categories,'category':category,'error':request.POST['name']+' SubCategory already exists'}
            return render(request, 'subcategories/addsubcategory.html', context)


def edit(request, id):
    subcategory = Subcategory.objects.get(id=id)
    categories = Category.objects.all()
    context = {'subcategory': subcategory, 'categories': categories}
    return render(request, 'subcategories/editsubcategory.html', context)

def update(request, id):
    categories = Category.objects.all()
    subcategory = Subcategory.objects.get(id=id)
    if 'course_category_id' not in request.POST:
        context = {'subcategory': subcategory, 'categories':categories,'error':'Please Select Category'}
        return render(request, 'subcategories/editsubcategory.html', context)
    else:
        category = get_object_or_404(Category, pk=request.POST['course_category_id'])
        if request.POST['name'] == '':
            context = {'subcategory': subcategory, 'categories':categories, 'error':'Please Enter Name', 'category':category}
            return render(request, 'subcategories/editsubcategory.html', context)
        try:
            subcat = Subcategory.objects.get(name=request.POST['name'],course_category_id=request.POST['course_category_id'])
        except Subcategory.DoesNotExist:
            subcategory.name = request.POST['name']
            subcategory.course_category_id = category
            subcategory.save()
            return redirect('/api/courses/subcat')
        if subcat:
            context = {'subcategory': subcategory, 'categories':categories,'category':category,'error':request.POST['name']+' SubCategory already exists'}
            return render(request, 'subcategories/editsubcategory.html', context)

def delete(request, id):
    subcategory = Subcategory.objects.get(id=id)
    subcategory.delete()
    return redirect('/api/courses/subcat')