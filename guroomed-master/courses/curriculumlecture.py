from django.shortcuts import render, redirect, get_object_or_404
from .models import CurriculumSection, CurriculumLecture as CL
from django.conf import settings
import vimeo
from django.http import HttpResponse


def index(request):
    cls = CL.objects.all()
    context = {'cls': cls}
    return render(request, 'curriculumlec/cllisting.html', context)


def create(request):
    context = {'request': request}
    return render(request, 'curriculumlec/addcl.html', context)


# to return all the lectures belonging to a section
# Parameters - section id, flag-0,1 to tell if the student/viewer has purchased the course(if he is authorised)
# Response - array of lectures belonging to section with all lecture information
def show(request, id, flag):
    cl = CL.objects.all().filter(curriculum_section_id=id)
    curriculumLec = []
    for curriculum in cl:
        if flag:
            videoURL = curriculum.video_url
        else:
            videoURL = None
        # return HttpResponse(videoURL)
        curriculumLec.append({
            'title':curriculum.title,
            'description':curriculum.description,
            'preview_url':curriculum.preview_url,
            'video_url':videoURL,
            'order_num':curriculum.order_num,
            'lecture_type':curriculum.lecture_type,
        })
    return curriculumLec


def store(request):
    v = vimeo.VimeoClient(
        key=settings.VIMEO_CLIENT_ID,
        token=settings.VIMEO_ACCESS_TOKEN,
        secret=settings.VIMEO_CLIENT_SECRET)
    video_uri = v.upload(request.FILES['video'].temporary_file_path())
    v.patch(video_uri, data={'name': request.FILES['video'].name})
    video_uri = video_uri[8:]

    section = CurriculumSection.objects.get(id=request.POST['curriculum_section_id'])
    cl = CL(curriculum_section_id=section, title=request.POST['title'], description=request.POST['description'], preview_url=video_uri, video_url=video_uri, order_num=request.POST['order_num'], lecture_type=request.POST['lecture_type'])
    cl.save()
    return redirect('/api/courses/curriculumlec')


def edit(request, id):
    cl = CL.objects.get(id=id)
    context = {'cl': cl}
    return render(request, 'curriculumlec/editcl.html', context)


def update(request, id):
    section = CurriculumSection.objects.get(id=request.POST['curriculum_section_id'])
    cl = CL.objects.get(id=id)
    cl.curriculum_section_id = section
    cl.title=request.POST['title']
    cl.description=request.POST['description']
    cl.preview_url=request.POST['preview_url']
    cl.video_url=request.POST['video_url']
    cl.order_num=request.POST['order_num']
    cl.lecture_type=request.POST['lecture_type']
    cl.save()
    return redirect('/api/courses/curriculumlec')


def delete(request, id):
    cl = CL.objects.get(id=id)
    cl.delete()
    return redirect('/api/courses/curriculumlec')