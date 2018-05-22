from django.shortcuts import render, redirect, get_object_or_404
from .models import Order, OrderCourse
from django.contrib.auth.models import User
from django.http import HttpResponse
import simplejson as json

def index(request):
    orders = Order.objects.all()
    context = {'orders': orders}
    return render(request, 'orders/orderlisting.html', context)

def show(request, id):
    orders = Order.objects.all().filter(user_id=id)
    orderDetails = []
    for order in orders:
        courses = []
        orderCourses = OrderCourse.objects.all().filter(order_id=order.id)
        for orderCourse in orderCourses:
            courses.append({
                'course_id' : orderCourse.course_id.id,
                'course_name' : orderCourse.course_id.title,
                'course_price' : orderCourse.course_price,
            })
        orderDetails.append({
            'id' : order.id,
            'course_price' : order.course_price,
            'tax_price' : order.tax_price,
            'discount_price' : order.discount_price,
            'total_price' : order.total_price,
            'currency' : order.currency,
            'courses' : courses,
            'date' : str(order.created_at),
        })
    return HttpResponse(json.dumps({'orders' : orderDetails}))
    # context = {'order': order}
    # return render(request, 'orders/singleorder.html', context)

def delete(request, id):
    order = Order.objects.get(id=id)
    order.delete()
    return redirect('/api/paypal/orders')

# def getCourses(request, id):
#     orderCourses = OrderCourse.objects.all().filter(order_id=id)
#     courses = []
#     for orderCourse in orderCourses:
#         courses.append({
#             'id' : orderCourse.course_id.id,
#             'name' : orderCourse.course_id.title,
#             'price' : orderCourse.course_id.price,
#         })
#     context = {'courses':courses}

#     return HttpResponse(json.dumps({'order' : id, 'courses':course}))