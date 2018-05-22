from django.shortcuts import render, redirect, get_object_or_404
from .models import UserInfo, UserPrivacy
from courses.models import Language
from django.contrib.auth.models import User, Group
from random import randint
from django.conf import settings
import simplejson as json
from django.http import HttpResponse, HttpResponseRedirect
from django.views.decorators.csrf import csrf_exempt


def index(request):
    users = User.objects.all()
    context = {'users': users}
    return render(request, 'users/userslisting.html', context)


def create(request):
    languages = Language.objects.all()
    groups = Group.objects.all()
    context = {'languages': languages, 'groups': groups}
    return render(request, 'users/adduser.html', context)


def storeInfo(request, user):

    if request.POST['headline'] == '':
        headline = ''
    else :
        headline = request.POST['headline']

    if request.POST['biography'] == '':
        biography = ''
    else :
        biography = request.POST['biography']

    if 'language' not in request.POST:
        language = None
    else :
        language = Language.objects.get(id=request.POST['language'])

    if request.POST['website_link'] == '':
        website_link = ''
    else :
        website_link = request.POST['website_link']

    if request.POST['gplus_link'] == '':
        gplus_link = ''
    else :
        gplus_link = request.POST['gplus_link']

    if request.POST['twitter_link'] == '':
        twitter_link = ''
    else :
        twitter_link = request.POST['twitter_link']

    if request.POST['facebook_link'] == '':
        facebook_link = ''
    else :
        facebook_link = request.POST['facebook_link']

    if request.POST['linkedin_link'] == '':
        linkedin_link = ''
    else :
        linkedin_link = request.POST['linkedin_link']

    if request.POST['youtube_link'] == '':
        youtube_link = ''
    else :
        youtube_link = request.POST['youtube_link']

    if 'photo_link' not in request.FILES:
        photo_link = ''
    else :
        photo_link = fupload(request.FILES['photo_link'])


    userInfo = UserInfo(user_id=user, headline=headline, biography=biography, language=language, website_link=website_link, gplus_link=gplus_link, twitter_link=twitter_link, facebook_link=facebook_link, linkedin_link=linkedin_link, youtube_link=youtube_link, photo_link=photo_link)
    userInfo.save()



def store(request):
    languages = Language.objects.all()
    groups = Group.objects.all()
    
    if request.POST.getlist('groups[]') == '':
        pass
    else:
        selectedgroups = []
        for g in request.POST.getlist('groups[]'):
            selectedgroups.append(Group.objects.get(id=g))

    if request.POST['email'] == '':
        context = {'groups':groups, 'selectedgroups':selectedgroups, 'languages': languages, 'error':'Please Enter Email'}
        return render(request, 'users/adduser.html', context)
    try:
        userexists = User.objects.get(email=request.POST['email'])
        if userexists:
            context = {'groups':groups, 'selectedgroups':selectedgroups, 'languages': languages, 'error':'Email exists'}
            return render(request, 'users/adduser.html', context)
    except User.DoesNotExist:
        email = request.POST['email']

    if request.POST['username'] != '':
        try:
            userexists = User.objects.get(username=request.POST['username'])
            if userexists:
                context = {'groups':groups, 'selectedgroups':selectedgroups, 'languages': languages, 'error':'Username exists'}
                return render(request, 'users/adduser.html', context)
        except User.DoesNotExist:
            username = request.POST['username']
    else:
        while True:
            username = request.POST['email'].split("@")[0] + str(randint(10000,99999))
            try:
                User.objects.get(username=username)
            except User.DoesNotExist:
                break

    if request.POST['password'] == '':
        context = {'groups':groups, 'selectedgroups':selectedgroups, 'languages': languages, 'error':'Please Enter Password'}
        return render(request, 'users/adduser.html', context)
    else :
        password = request.POST['password']

    if request.POST['first_name'] == '':
        first_name = ''
    else :
        first_name = request.POST['first_name']

    if request.POST['last_name'] == '':
        last_name = ''
    else :
        last_name = request.POST['last_name']

    user = User.objects.create_user(username, email, password)
    user.first_name = first_name
    user.last_name = last_name
    user.save()

    storeInfo(request, user)

    group_assign(user, selectedgroups)
    
    return redirect('/api/users')


def show(request, id):
    user = User.objects.get(id=id)
    try:
        userinfo = UserInfo.objects.get(user_id=user)
    except UserInfo.DoesNotExist:
        userinfo = ''
    groups = user.groups.all()
    # try:
    # except Exception, e:
    context = {'groups':groups, 'user': user, 'userinfo':userinfo}
    return render(request, 'users/singleuser.html', context)


def edit(request, id):
    languages = Language.objects.all()
    groups = Group.objects.all()
    user = User.objects.get(id=id)
    selectedgroups = user.groups.all()
    try:
        userinfo = UserInfo.objects.get(user_id=user)
    except UserInfo.DoesNotExist:
        userinfo = ''
    context = {'user': user, 'groups': groups, 'selectedgroups': selectedgroups, 'languages': languages, 'userinfo':userinfo}
    return render(request, 'users/edituser.html', context)


def updateInfo(request, user, userinfo):
    if 'headline' not in request.POST:
        headline = ''
    else :
        headline = request.POST['headline']

    if 'biography' not in request.POST:
        biography = ''
    else :
        biography = request.POST['biography']

    if 'language' not in request.POST:
        language = None
    else :
        language = Language.objects.get(id=int(request.POST['language']))

    if 'website_link' not in request.POST:
        website_link = ''
    else :
        website_link = request.POST['website_link']

    if 'gplus_link' not in request.POST:
        gplus_link = ''
    else :
        gplus_link = request.POST['gplus_link']

    if 'twitter_link' not in request.POST:
        twitter_link = ''
    else :
        twitter_link = request.POST['twitter_link']

    if 'facebook_link' not in request.POST:
        facebook_link = ''
    else :
        facebook_link = request.POST['facebook_link']

    if 'linkedin_link' not in request.POST:
        linkedin_link = ''
    else :
        linkedin_link = request.POST['linkedin_link']

    if 'youtube_link' not in request.POST:
        youtube_link = ''
    else :
        youtube_link = request.POST['youtube_link']

    # if 'photo_link' not in request.FILES:
    #     photo_link = userinfo.photo_link
    # else :
    #     photo_link = fupload(request.FILES['photo_link'])

    if userinfo == '':
        userInfo = UserInfo(user_id=user, headline=headline, biography=biography, language=language, website_link=website_link, gplus_link=gplus_link, twitter_link=twitter_link, facebook_link=facebook_link, linkedin_link=linkedin_link, youtube_link=youtube_link, photo_link='')
        userInfo.save()

    else:
        userinfo.headline=headline
        userinfo.biography=biography
        userinfo.language=language
        userinfo.website_link=website_link
        userinfo.gplus_link=gplus_link
        userinfo.twitter_link=twitter_link
        userinfo.facebook_link=facebook_link
        userinfo.linkedin_link=linkedin_link
        userinfo.youtube_link=youtube_link
        # userinfo.photo_link=photo_link
        userinfo.save()

def update(request, id):
    groups = Group.objects.all()
    languages = Language.objects.all()
    user = User.objects.get(id=id)
    
    if request.POST.getlist('groups[]') == '':
        pass
    else:
        selectedgroups = []
        for g in request.POST.getlist('groups[]'):
            selectedgroups.append(Group.objects.get(id=g))

    try :
        userinfo = UserInfo.objects.get(user_id=user)
    except UserInfo.DoesNotExist:
        userinfo = ''
    if request.POST['email'] == '':
        context = {'groups':groups, 'selectedgroups':selectedgroups, 'user':user, 'userinfo':userinfo, 'languages': languages, 'error':'Please Enter Email'}
        return render(request, 'users/edituser.html', context)
    try:
        userexists = User.objects.get(email=request.POST['email'])
        if userexists:
            try:
                email = request.POST['email']
                userexists = User.objects.get(id=id, email=email)
            except User.DoesNotExist:
                context = {'groups':groups, 'selectedgroups':selectedgroups, 'user':user, 'userinfo':userinfo, 'languages': languages, 'error':'Email exists'}
                return render(request, 'users/edituser.html', context)
    except User.DoesNotExist:
        email = request.POST['email']

    if request.POST['username'] != '':
        try:
            userexists = User.objects.get(username=request.POST['username'])
            if userexists:
                try:
                    username = request.POST['username']
                    userexists = User.objects.get(id=id, username=username)
                except User.DoesNotExist:
                    context = {'groups':groups, 'selectedgroups':selectedgroups, 'user':user, 'userinfo':userinfo, 'languages': languages, 'error':'Username exists'}
                    return render(request, 'users/edituser.html', context)
        except User.DoesNotExist:
            username = request.POST['username']
    else:
        while True:
            username = request.POST['email'].split("@")[0] + str(randint(10000,99999))
            try:
                User.objects.get(username=username)
            except User.DoesNotExist:
                break

    if request.POST['first_name'] == '':
        first_name = ''
    else :
        first_name = request.POST['first_name']

    if request.POST['last_name'] == '':
        last_name = ''
    else :
        last_name = request.POST['last_name']

    user.email = email
    user.username = username
    user.first_name = first_name
    user.last_name = last_name
    user.save()

    updateInfo(request, user, userinfo)

    group_assign(user, selectedgroups)
    
    return redirect('/api/users')


def delete(request, id):
    user = User.objects.get(id=id)
    try:
        userinfo = UserInfo.objects.get(user_id=user)
        userinfo.delete()
    except UserInfo.DoesNotExist:
        pass
    user.delete()
    return redirect('/api/users')

def fupload(photo_link):
    with open(settings.MEDIA_ROOT+'/'+photo_link.name, 'wb+') as destination:
        for chunk in photo_link.chunks():
            destination.write(chunk)
    return settings.MEDIA_URL+photo_link.name

def group_assign(user, groups):
    user.groups.clear()

    for group in groups:
        group.user_set.add(user)

def getProfile(request):
    if not request.user.is_authenticated:
        return HttpResponse(json.dumps({'status': 0, 'error': 'You are not loggedin'}))

    #user table information
    u = request.user
    user = {}
    user['id'] = u.id
    user['firstName'] = u.first_name
    user['lastName'] = u.last_name
    user['email'] = u.email

    #user info table
    try:
        userInfo = UserInfo.objects.get(user_id=u)
    except UserInfo.DoesNotExist:
        user['info'] = None
    if 'userInfo' in locals():
        try:
            lan = userInfo.language
            if lan == None:
                language = 0
            else:
                language = lan.id
        except Exception as e:
            return HttpResponse(json.dumps({'status':0, 'error':str(e)}))
        user['headline'] = userInfo.headline
        user['biography'] = userInfo.biography
        user['language'] = language
        user['websiteLink'] = userInfo.website_link
        user['gplusLink'] = userInfo.gplus_link
        user['twitterLink'] = userInfo.twitter_link
        user['facebookLink'] = userInfo.facebook_link
        user['linkedinLink'] = userInfo.linkedin_link
        user['youtubeLink'] = userInfo.youtube_link
        user['photoLink'] = userInfo.photo_link

    # user privacy info
    try:
        userPrivacy = UserPrivacy.objects.get(user_id=u)
    except UserPrivacy.DoesNotExist:
        user['privacy'] = None
    if 'userPrivacy' in locals():
        user['hide_search_engine'] = userPrivacy.hide_search_engine
        user['hide_courses'] = userPrivacy.hide_courses

    langs = Language.objects.all()
    languages = []
    for lan in langs:
        languages.append({
            'value' : str(lan.id),
            'label' : lan.name,
        })
    
    return HttpResponse(json.dumps({'status': 1, 'user': user, 'languages': languages}))


@csrf_exempt
def storeProfile(request):
    if not request.user.is_authenticated:
        return HttpResponse(json.dumps({'status': 0, 'error': 'You are not loggedin'}))
    u = request.user
    # u = User.objects.get(id=4)
    if 'first_name' not in request.POST:
        first_name = ''
    else :
        first_name = request.POST['first_name']

    if 'last_name' not in request.POST:
        last_name = ''
    else :
        last_name = request.POST['last_name']

    u.first_name = first_name
    u.last_name = last_name
    u.save()

    try :
        userinfo = UserInfo.objects.get(user_id=u)
    except UserInfo.DoesNotExist:
        userinfo = ''
    # return HttpResponse(userinfo)
    try:
        updateInfo(request, u, userinfo)
    except Exception as e:
        return HttpResponse(json.dumps({'status': 0, 'error': str(e)}))
    
    return HttpResponse(json.dumps({'status': 1, 'msg': 'Profile Changes are Saved'}))

@csrf_exempt
def storeProfilePicture(request):
    if 'photo_link' not in request.FILES:
        return HttpResponse(json.dumps({'status': 0, 'error': 'File Not Found'}))
    else :
        photo_link = request.FILES['photo_link']
    with open(settings.MEDIA_ROOT+'/'+photo_link.name, 'wb+') as destination:
        for chunk in photo_link.chunks():
            destination.write(chunk)
    userinfo = UserInfo.objects.get(user_id=request.user.id)
    userinfo.photo_link=photo_link
    userinfo.save()

    return HttpResponse(json.dumps({'status': 1, 'link': settings.MEDIA_URL+photo_link.name}))