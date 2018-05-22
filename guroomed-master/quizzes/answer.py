from django.http import HttpResponse
from .models import Answers, Questions
from django.views.decorators.csrf import csrf_exempt
import simplejson as json


@csrf_exempt
def store(request):
    if not request.user.is_authenticated:
        return HttpResponse(json.dumps({'status': 0, 'error': 'You are not loggedin'}))
    if 'question_id' not in request.POST:
        return HttpResponse(json.dumps({'status': 0, 'error':'Question Id is not valid'}))
    try:
        question = Questions.objects.get(id=request.POST['question_id'])
    except Questions.DoesNotExist:
        return HttpResponse(json.dumps({'status': 0, 'error':'Question Id is not valid'}))
    if 'content' not in request.POST:
        return HttpResponse(json.dumps({'status': 0, 'error':'Please enter Content for Answer'}))
    if 'status' not in request.POST:
        return HttpResponse(json.dumps({'status': 0, 'error':'Please enter Status of Answer'}))
    if 'order' not in request.POST:
        return HttpResponse(json.dumps({'status': 0, 'error':'Please enter Order of Answer'}))
    if 'is_correct' not in request.POST:
        return HttpResponse(json.dumps({'status': 0, 'error':'Please enter Answer is correct or not'}))
    
    try:
        answer = Questions()
        answer.question_id = question
        answer.content = request.POST['content']
        answer.status = request.POST['status']
        answer.order = request.POST['order']
        answer.is_correct = request.POST['is_correct']
        answer.save()
    except Exception as e:
        return HttpResponse(json.dumps({'status': 0, 'error': str(e)}))
    return HttpResponse(json.dumps({'status': 1, 'msg': 'Answer Added Successfully'}))

@csrf_exempt
def update(request, id):
    try:
        answer = Answers.objects.get(id=id)
    except Answers.DoesNotExist:
        return HttpResponse(json.dumps({'status': 0, 'error': 'Invalid Answer'}))
    if not request.user.is_authenticated:
        return HttpResponse(json.dumps({'status': 0, 'error': 'You are not loggedin'}))
    if 'question_id' not in request.POST:
        return HttpResponse(json.dumps({'status': 0, 'error':'Question Id is not valid'}))
    try:
        question = Questions.objects.get(id=request.POST['question_id'])
    except Questions.DoesNotExist:
        return HttpResponse(json.dumps({'status': 0, 'error':'Question Id is not valid'}))
    if 'content' not in request.POST:
        return HttpResponse(json.dumps({'status': 0, 'error':'Please enter Content for Answer'}))
    if 'status' not in request.POST:
        return HttpResponse(json.dumps({'status': 0, 'error':'Please enter Status of Answer'}))
    if 'order' not in request.POST:
        return HttpResponse(json.dumps({'status': 0, 'error':'Please enter Order of Answer'}))
    if 'is_correct' not in request.POST:
        return HttpResponse(json.dumps({'status': 0, 'error':'Please enter Answer is correct or not'}))
    
    try:
        answer.question_id = question
        answer.content = request.POST['content']
        answer.status = request.POST['status']
        answer.order = request.POST['order']
        answer.is_correct = request.POST['is_correct']
        answer.save()
    except Exception as e:
        return HttpResponse(json.dumps({'status': 0, 'error': str(e)}))
    return HttpResponse(json.dumps({'status': 1, 'msg': 'Answer Updated Successfully'}))

@csrf_exempt
def delete(request, id):
    try:
        answer = Answers.objects.get(id=id)
    except Answers.DoesNotExist:
        return HttpResponse(json.dumps({'status': 0, 'error': 'Answer does not exists'}))
    answer.delete()
    return HttpResponse(json.dumps({'status': 1, 'msg': 'Answer Deleted Successfully'}))