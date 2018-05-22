from django.shortcuts import render
from django.http import HttpResponseRedirect, HttpResponse
from django.template import loader
import vimeo
from django.conf import settings
from .models import Item
from .models import Item
from django.contrib.auth.models import Group


def login_oauth(request):
	v = vimeo.VimeoClient(
		key=settings.VIMEO_CLIENT_ID,
		secret=settings.VIMEO_CLIENT_SECRET)
	vimeo_authorization_url = v.auth_url(['public', 'private'], '/api/videos/success' , 200)
	return HttpResponseRedirect(vimeo_authorization_url)


def vimeo_success(request):
	v = vimeo.VimeoClient(
		key=settings.VIMEO_CLIENT_ID,
		secret=settings.VIMEO_CLIENT_SECRET)
	CODE_FROM_URL = request.GET["code"]
	try:
		token, user, scope = v.exchange_code(CODE_FROM_URL, '/api/videos/success')

		user_info = [
			('uri', user['uri']),
			('name', user['name']),
			('link', user['link']),
			('location', user['location']),
			('bio', user['bio']),
			('created_time', user['created_time']),
			('account', user['account']),
			('pictures', user['pictures']),
			('websites', user['websites']),
			('metadata', user['metadata']),
			('preferences', user['preferences']),
			('content_filter', user['content_filter']),
			('resource_key', user['resource_key']),
			('token', token)
		]

		template = loader.get_template('zenvimeo/user.html')
		context = {'user_info' : user_info}
		return HttpResponse(template.render(context, request))

		# response = v.get('/221252200')
		# return HttpResponseRedirect('/upload_form')
		# return HttpResponse(user[])
	except vimeo.auth.GrantFailed:
		return HttpResponse("failed")


def vimeo_upload(request):
	v = vimeo.VimeoClient(
		key=settings.VIMEO_CLIENT_ID,
        token=settings.VIMEO_ACCESS_TOKEN,
		secret=settings.VIMEO_CLIENT_SECRET)
	video_url = settings.MEDIA_ROOT
	video_name = '/videos/1.mp4'
	video_uri = v.upload(video_url + video_name)
	v.patch(video_uri, data={'name': 'Video title', 'description': '...'})
	return HttpResponse(video_uri)


def vimeo_delete(request):
	v = vimeo.VimeoClient(
		key=settings.VIMEO_CLIENT_ID,
		token=settings.VIMEO_ACCESS_TOKEN,
		secret=settings.VIMEO_CLIENT_SECRET)
	response = v.delete('/videos/228941899')
	return HttpResponse(response)


def group_list(request):
	groups = request.user.groups.all()
	output = []
	for group in groups:
		if group.name == 'zen_student':
			var = 'false'
		elif group.name == 'faculty':
			var = 'false'
		else:
			output.append(group)
	template = loader.get_template('zenvimeo/viewgroup.html')
	context = {'output' : output}
	return HttpResponse(template.render(context, request))

	
def autodesk(request):
	template = loader.get_template('autodesk/autodesk360.html')
	context = {'request' : request}
	return HttpResponse(template.render(context, request))	

def autodesk_forge(request):
	template = loader.get_template('autodesk/index.html')
	context = {'request' : request}
	return HttpResponse(template.render(context, request))


def vim_list(request,group):
	output = Item.objects.filter(video_group = group).order_by('-video')
	template = loader.get_template('zenvimeo/viewvideo.html')
	context = {'output' : output}
	return HttpResponse(template.render(context, request))


def fupload(request):
	if request.method == 'POST':
		v = vimeo.VimeoClient(
			key=settings.VIMEO_CLIENT_ID,
			token=settings.VIMEO_ACCESS_TOKEN,
			secret=settings.VIMEO_CLIENT_SECRET)
		video_uri = v.upload(request.FILES['video'].temporary_file_path())
		v.patch(video_uri, data={'name': request.FILES['video'].name})
		video_uri = video_uri[8:]
		video_uri = 'https://vimeo.com/'+video_uri
		g = Group.objects.get(pk=request.POST['video_group'])
		
		i = Item(title=request.POST['title'],description=request.POST['description'],video=video_uri,video_group=g)
		i.save()
		groups = request.user.groups.all()
		context = {'item' : i,'message':'Added Successfuly','groups' : groups}
		return render(request, 'zenvimeo/upload.html', context)

	else:
		groups = request.user.groups.all()
		context = {'groups' : groups}
		return render(request, 'zenvimeo/upload.html', context)