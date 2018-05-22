from django.contrib.auth.models import User
from django.http import HttpResponse
import simplejson as json
from .models import UserCart
from courses.models import Course
from django.views.decorators.csrf import csrf_exempt


@csrf_exempt
def addCart(request):
    if request.POST['user_id'] == '':
        return HttpResponse(json.dumps({'error':'Please send User Id'}))
    if request.POST.getlist('course_ids[]') == '':
        return HttpResponse(json.dumps({'error':'Please send atleast one Course Id'}))
    else:
        selectedCourses = []
        for course_id in request.POST.getlist('course_ids[]'):
            try:
                course = Course.objects.get(id=course_id)
            except Course.DoesNotExist:
                return HttpResponse(json.dumps({'error':'Wrong Course Id'}))
            selectedCourses.append(course.id)
    try:
        user = User.objects.get(id=request.POST['user_id'])
    except User.DoesNotExist:
        return HttpResponse(json.dumps({'error':'Wrong User Id'}))

    existCart = UserCart.objects.all().filter(user_id=request.POST['user_id'])
    cartItems = []
    count = 0
    if existCart:
        for cart in existCart:
            count += 1
            cartItems.append(cart.course_id.id)

    for sc in selectedCourses:
        if sc not in cartItems:
            count += 1
            course = Course.objects.get(id=sc)
            uc = UserCart(user_id=user, course_id=course)
            uc.save();
    
    return HttpResponse(json.dumps({'status':1, 'count':count}))


def getCart(request, id):
    cartItems = UserCart.objects.all().filter(user_id=id)
    cartDetails = []
    count = 0
    for item in cartItems:
        count += 1
        course = {'courseId':item.course_id.id}
        cartDetails.append(course)
    return HttpResponse(json.dumps({'items':cartDetails, 'count':count}))


@csrf_exempt
def deleteCart(request, id):
    count = len(UserCart.objects.all().filter(user_id=id))
    # return HttpResponse(request.POST)
    if 'course_id' in request.POST:
        cartItems = UserCart.objects.all().filter(user_id=id, course_id=request.POST['course_id'])
        if cartItems:
            count -= 1
    else:    
        cartItems = UserCart.objects.all().filter(user_id=id)
        if cartItems:
            count = 0
    for item in cartItems:
        item.delete()

    return HttpResponse(json.dumps({'status':1, 'count':count}))