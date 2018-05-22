from django.http import HttpResponse
from drafts.models import CurriculumSection as CS
from .models import Quizzes
from django.views.decorators.csrf import csrf_exempt
import simplejson as json
from django.contrib.auth.models import User, Group


# def index(request):

# def create(request):

@csrf_exempt
def store(request):
    if request.method == 'POST':
        if not request.user.is_authenticated:
            return HttpResponse(json.dumps({'status': 0, 'error': 'You are not loggedin'}))
        if 'course_section_id' not in request.POST:
            return HttpResponse(json.dumps({'status': 0, 'error':'Section Id is not valid'}))
        try:
            section = CS.objects.get(id=request.POST['course_section_id'])
        except CS.DoesNotExist:
            return HttpResponse(json.dumps({'status': 0, 'error':'Section Id is not valid'}))
        if 'title' not in request.POST:
            return HttpResponse(json.dumps({'status': 0, 'error':'Please enter Title for quiz'}))
        
        try:
            quiz = Quizzes()
            quiz.course_section_id = section
            quiz.user_id = request.user
            quiz.title = request.POST['title']
            if 'description' in request.POST:
                quiz.description = request.POST['description']
            quiz.save()
            return HttpResponse(json.dumps({'status': 1, 'msg': 'Quiz title added successfully'}))
        except Exception as e:
            return HttpResponse(json.dumps({'status': 0, 'error': str(e)}))
    else:
        return HttpResponse(json.dumps({'status':0, 'error':'Please use POST method'}))            

# def show(request, id):

# def edit(request, id):

@csrf_exempt
def update(request, id):
    try:
        quiz = Quizzes.objects.get(id=id)
    except Quizzes.DoesNotExist:
        return HttpResponse(json.dumps({'status': 0, 'error': 'Quiz does not exists'}))
    if not request.user.is_authenticated:
        return HttpResponse(json.dumps({'status': 0, 'error': 'You are not loggedin'}))
    if request.user.id != quiz.user_id :
        return HttpResponse(json.dumps({'status': 0, 'error': 'You are not authorized user'}))
    if 'course_section_id' not in request.POST:
        return HttpResponse(json.dumps({'status': 0, 'error':'Section Id is not valid'}))
    try:
        section = CS.objects.get(id=request.POST['course_section_id'])
    except CS.DoesNotExist:
        return HttpResponse(json.dumps({'status': 0, 'error':'Section Id is not valid'}))
    if 'title' not in request.POST:
        return HttpResponse(json.dumps({'status': 0, 'error':'Please enter Title for quiz'}))
    
    try:
        quiz.course_section_id = section
        quiz.user_id = request.user
        quiz.title = request.POST['title']
        if 'description' in request.POST:
            quiz.description = request.POST['description']
        quiz.save()
        return HttpResponse(json.dumps({'status': 1, 'msg': 'Quiz Updated Successfully'}))
    except Exception as e:
        return HttpResponse(json.dumps({'status': 0, 'error': str(e)}))

@csrf_exempt
def delete(request, id):
    try:
        quiz = Quizzes.objects.get(id=id)
    except Quizzes.DoesNotExist:
        return HttpResponse(json.dumps({'status': 0, 'error': 'Quiz does not exists'}))
    quiz.delete()
    return HttpResponse(json.dumps({'status': 1, 'msg': 'Quiz Deleted Successfully'}))