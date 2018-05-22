from .models import Tax
from django.http import HttpResponse
import simplejson as json
from django.shortcuts import render, redirect

def index(request):
    taxes = Tax.objects.all()
    context = {'taxes': taxes}
    return render(request, 'taxes/taxlisting.html', context)

def create(request):
    context = {'request': request}
    return render(request, 'taxes/createtax.html', context)

def store(request):
    if 'name' not in request.POST:
        context = {'error':'Please Enter Name'}
        return render(request, 'taxes/createtax.html', context)
    if 'description' not in request.POST:
        context = {'error':'Please Enter Description'}
        return render(request, 'taxes/createtax.html', context)
    if 'value' not in request.POST:
        context = {'error':'Please Enter Value'}
        return render(request, 'taxes/createtax.html', context)
    try:
        t = Tax.objects.get(name=request.POST['name'])
    except Tax.DoesNotExist:
        tax = Tax(name=request.POST['name'],description=request.POST['description'],value=request.POST['value'])
        tax.save()
        return redirect('/api/paypal/taxes')
    if t:
        context = {'error':request.POST['name']+' Tax already exists'}
        return render(request, 'taxes/createtax.html', context)

def delete(request, id):
    tax = Tax.objects.get(id=id)
    tax.delete()
    return redirect('/api/paypal/taxes')