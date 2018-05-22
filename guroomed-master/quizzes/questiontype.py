from django.views.decorators.csrf import csrf_exempt
from .models import QuestionTypes
import simplejson as json
from django.http import HttpResponse


@csrf_exempt
def store(request):
    try:
        if 'name' not in request.POST:
        	return HttpResponse(json.dumps({'status': 0, 'error': 'Please Enter Name for the Question Type'}))
        question_type = QuestionTypes()
        question_type.name = request.POST['name']
        question_type.save()
    except Exception as e:
        return HttpResponse(json.dumps({'status': 0, 'error': str(e)}))
    return HttpResponse(json.dumps({'status': 1, 'msg': 'Question Type saved successfuly - '+question_type.name}))
