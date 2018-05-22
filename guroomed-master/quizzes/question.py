from django.http import HttpResponse
from .models import Quizzes, QuestionTypes, Questions, Answers
from django.views.decorators.csrf import csrf_exempt
import simplejson as json
# from django.shortcuts import render, redirect
# from courses.models import CurriculumSection as CS
# from django.contrib.auth.models import User, Group


@csrf_exempt
def store(request):
    if not request.user.is_authenticated:
        return HttpResponse(json.dumps({'status': 0, 'error': 'You are not loggedin'}))
    if 'quiz_id' not in request.POST:
        return HttpResponse(json.dumps({'status': 0, 'error':'Quiz Id is not valid'}))
    try:
        quiz = Quizzes.objects.get(id=request.POST['quiz_id'])
    except Quizzes.DoesNotExist:
        return HttpResponse(json.dumps({'status': 0, 'error':'Quiz Id is not valid'}))
    if 'type_id' not in request.POST:
        return HttpResponse(json.dumps({'status': 0, 'error':'Type Id is not valid'}))
    try:
        q_type = QuestionTypes.objects.get(id=request.POST['type_id'])
    except QuestionTypes.DoesNotExist:
        return HttpResponse(json.dumps({'status': 0, 'error':'Type Id is not valid'}))
    if 'content' not in request.POST:
        return HttpResponse(json.dumps({'status': 0, 'error':'Please enter Content for question'}))
    if 'status' not in request.POST:
        return HttpResponse(json.dumps({'status': 0, 'error':'Please enter Status of question'}))
    if 'order' not in request.POST:
        return HttpResponse(json.dumps({'status': 0, 'error':'Please enter Order of question'}))
    
    try:
        question = Questions()
        question.quiz_id = quiz
        question.type_id = q_type
        question.content = request.POST['content']
        question.status = bool(request.POST['status'])
        question.order = request.POST['order']
        question.save()
        # taking recent created id and store quiz answer in answers table 
        # question_id = question.id
        answer = Answers()
        quiz_ans = json.loads(request.POST['answer'])
        for i in quiz_ans:
            answer.question_id = question
            answer.answer = i['option']
            answer.status = bool(request.POST['status'])
            answer.order = request.POST['order']
            answer.is_correct = bool(i['answer'])
            answer.pk = None
            answer.save()
        return HttpResponse(json.dumps({'status': 1, 'msg': 'Quiz created Successfully'}))
    except Exception as e:
        return HttpResponse(json.dumps({'status': 0, 'error': str(e)}))

@csrf_exempt
def update(request, id):
    try:
        question = Questions.objects.get(id=id)
    except Questions.DoesNotExist:
        return HttpResponse(json.dumps({'status': 0, 'error': 'Invalid Question'}))
    if not request.user.is_authenticated:
        return HttpResponse(json.dumps({'status': 0, 'error': 'You are not loggedin'}))
    if 'quiz_id' not in request.POST:
        return HttpResponse(json.dumps({'status': 0, 'error':'Quiz Id is not valid'}))
    try:
        quiz = Quizzes.objects.get(id=request.POST['quiz_id'])
    except Quizzes.DoesNotExist:
        return HttpResponse(json.dumps({'status': 0, 'error':'Quiz Id is not valid'}))
    if 'type_id' not in request.POST:
        return HttpResponse(json.dumps({'status': 0, 'error':'Type Id is not valid'}))
    try:
        q_type = QuestionTypes.objects.get(id=request.POST['type_id'])
    except QuestionTypes.DoesNotExist:
        return HttpResponse(json.dumps({'status': 0, 'error':'Type Id is not valid'}))
    if 'content' not in request.POST:
        return HttpResponse(json.dumps({'status': 0, 'error':'Please enter Content for question'}))
    if 'status' not in request.POST:
        return HttpResponse(json.dumps({'status': 0, 'error':'Please enter Status of question'}))
    if 'order' not in request.POST:
        return HttpResponse(json.dumps({'status': 0, 'error':'Please enter Order of question'}))
    
    try:
        question.quiz_id = quiz
        question.type_id = q_type
        question.content = request.POST['content']
        question.status = request.POST['status']
        question.order = request.POST['order']
        question.save()
    except Exception as e:
        return HttpResponse(json.dumps({'status': 0, 'error': str(e)}))

@csrf_exempt
def delete(request, id):
    try:
        question = Questions.objects.get(id=id)
    except Questions.DoesNotExist:
        return HttpResponse(json.dumps({'status': 0, 'error': 'Question does not exists'}))
    question.delete()
    return HttpResponse(json.dumps({'status': 1, 'msg': 'Question Deleted Successfully'}))