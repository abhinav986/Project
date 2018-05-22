# #manager reasons
# Video Quality is blur
# Video Content is not appropriate
# Some of the topics are repeating
# Teaching Quality is not as per Guroomed standard


# #reviewer reasons
# Video Quality is blur
# Video Content is not appropriate
# Some of the topics are repeating
# Teaching Quality is not as per Guroomed standard 



# from drafts.models import ReasonsRejected
# r = ReasonsRejected.objects.get(id=5)
# r.text = 'Video Quality is blur'
# r.save()
# r = ReasonsRejected.objects.get(id=6)
# r.text = 'Video Content is not appropriate'
# r.save()
# r = ReasonsRejected.objects.get(id=7)
# r.text = 'Some of the topics are repeating'
# r.save()
# r = ReasonsRejected.objects.get(id=8)
# r.text = 'Teaching Quality is not as per Guroomed standard'
# r.save()

from django.shortcuts import render
from django.shortcuts import redirect
from .models import ReasonsRejected

def index(request):
    rr=ReasonsRejected.objects.all()
    return render(request,'drafts/reasonrejectlisting.html',{'rr': rr})

def create(request):
    return render(request,'drafts/addreasonreject.html')

def create_save(request):
    if request.POST['text']=='':
        context={
            'error':'please insert text here'
        }
        return render(request,'drafts/addreasonreject.html',context)
    elif request.POST['types']=='select':
        context = {
            'error': 'please  select  a choice'
        }
        return render(request, 'drafts/addreasonreject.html', context)

    try:
        rejecto=ReasonsRejected.objects.get(text=request.POST['text'],type=request.POST['types'])

    except ReasonsRejected.DoesNotExist:
        rr=ReasonsRejected(text=request.POST['text'],type=request.POST['types'])
        rr.save()
        return redirect('/api/draft/')
    if rejecto:
        context={
            'error':'object already exit'
        }
        return render(request,'drafts/addreasonreject.html',context)

def delete(request,id):
    rr=ReasonsRejected.objects.get(id=id)
    rr.delete()
    return redirect('/api/draft/')

def edit(request,id):
    rr=ReasonsRejected.objects.get(id=id)
    return render(request,'drafts/editreasonreject.html',{'rr': rr})

def edit_save(request,id):
    rr=ReasonsRejected.objects.get(id=id)
    if request.POST['text']=='':
        return render(request,'drafts/editreasonreject.html',{'error': 'please insert text'})
    try:
        rar=ReasonsRejected.objects.get(text=request.POST['text'],type=request.POST['types'])
    except ReasonsRejected.DoesNotExist:
        rr.text = request.POST['text']
        rr.type = request.POST['types']
        rr.save()
        return redirect('/api/draft/')
    if rar and rar.id!=rr.id:
        context={
            'error':'object already exists', 'rr': rr
        }
        return render(request,'drafts/editreasonreject.html',context)
    else:
        rr.text = request.POST['text']
        rr.type = request.POST['types']
        rr.save()
        return redirect('/api/draft/')




