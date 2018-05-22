from django.http import HttpResponse
import simplejson as json
from django.contrib.auth.models import User
from courses.models import Course
from guroomed.models import UserCart
from .models import Tax
from django.conf import settings


def display(request):
	user = request.user
	cart = UserCart.objects.all().filter(user_id = user.id)
	taxObj = Tax.objects.all()
	tax = taxObj[0].value

	course_price = 0
	discount_price = 0
	tax_price = 0
	for item in cart:
		if item.course_id.discount != 0:
			discount_price += item.course_id.price - item.course_id.discount
		tax_price += item.course_id.price * tax / 100
		course_price += item.course_id.price

	user_id = user.id
	total_price = course_price + tax_price - discount_price
	currency = settings.PAYPAL_CURRENCY

	status = None
	if 'status' in request.GET:
		status = request.GET['status']

	context = {
		'status': status,
		# 'course_id': course_id,
		'user_id': user_id,
		'course_price': course_price,
		'tax_price': tax_price,
		'discount_price': discount_price,
		'total_price': total_price,
		'currency': currency,
		'params': request.build_absolute_uri('/')+'api/paypal/create?course_price='+str(course_price)+'&user_id='+str(user_id)+'&tax_price='+str(tax_price)+'&discount_price='+str(discount_price)+'&p_currency='+currency+'&total_price='+str(total_price)
	}
	return HttpResponse(json.dumps({'context':context}))