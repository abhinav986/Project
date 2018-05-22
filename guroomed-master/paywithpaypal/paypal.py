from django.template import loader
from django.http import HttpResponse
from django.shortcuts import render, redirect
import paypalrestsdk
import logging
from django.contrib.auth.models import User
from courses.models import Course
from paywithpaypal.models import Order, PaypalDetail, Payment as PD, OrderCourse, Tax
import simplejson as json
from django.conf import settings
from django.core.mail import send_mail
from guroomed.models import UserCourses as UC
from guroomed.models import UserCart
from decimal import Decimal

def paypal_execute(request):
	# check where to redirect
	if 'localhost' not in request.build_absolute_uri('/'):
		server_url = request.build_absolute_uri('/#/')
	else:
		server_url = 'http://localhost:4200/#/'

	logging.basicConfig(level=logging.INFO) # log the actions

	paypalrestsdk.configure({ # configure the  paypal credentials
		"mode": settings.PAYPAL_MODE, # sandbox or live
		"client_id": settings.PAYPAL_CLIENT_ID,
		"client_secret": settings.PAYPAL_CLIENT_SECRET 
	})


	# ID of the payment. This ID is provided when creating payment.
	payment = paypalrestsdk.Payment.find(request.GET['paymentId'])

	# PayerID is required to approve the payment.
	if payment.execute({"payer_id": request.GET['PayerID']}):  # return True or False

		cart = UserCart.objects.all().filter(user_id = request.user.id) #user cart details
		user = User.objects.get(id=request.GET['user_id']) #which user is loggedin
		
		# items = [] #list of course ids
		# for item in cart:
		# 	items.append(item.course_id)

		# course = Course.objects.get(id=request.GET['course_id'])
		
		#save in orders table
		order = Order(user_id = user, course_price = request.GET['course_price'], tax_price = request.GET['tax_price'], discount_price = request.GET['discount_price'], total_price = request.GET['total_price'], currency = request.GET['p_currency'])
		order.save()

		#save in payments table
		paymentdone = PD(order_id = order, currency = payment.transactions[0].amount.currency, payment_status = 'successful', course_price = order.course_price, tax_price = order.tax_price, discount_price = order.discount_price, total_price = order.total_price)
		paymentdone.save()

		#save in paypal details table
		pd = PaypalDetail()
		pd.order_id=order
		pd.payment_id=payment.id
		pd.state=payment.state
		pd.cart=payment.transactions[0].related_resources[0].sale.id
		pd.payer_payment_method=payment.payer.payment_method
		pd.payer_status=payment.payer.status
		pd.payer_email=payment.payer.payer_info.email
		pd.payer_id=payment.payer.payer_info.payer_id
		pd.payer_country_code=payment.payer.payer_info.country_code
		pd.transactions_amount=payment.transactions[0].amount.total
		pd.transactions_currency=payment.transactions[0].amount.currency
		# pd.payee_merchant_id=payment.transactions[0].payee.merchant_id
		# pd.payee_email=payment.transactions[0].payee.email
		pd.description=payment.transactions[0].description
		pd.payment_mode=payment.transactions[0].related_resources[0].payment_mode
		pd.reason_code=payment.transactions[0].related_resources[0].reason_code
		pd.protection_eligibility=payment.transactions[0].related_resources[0].protection_eligibility
		pd.transaction_fee=payment.transactions[0].related_resources[0].transaction_fee
		pd.save()

		course_ids = ''
		for item in cart:
			course = Course.objects.get(id=item.course_id.id)
			course_ids = course_ids + '&course_id[]=' + str(course.id)

			uc = UC(course_id=course, user_id=user, taught_learned='learned', is_favourite=0)
			uc.save()

			oc = OrderCourse(course_id=course, order_id=order, course_price=course.price)
			oc.save()

			item.delete()

		# cartItems = UserCart.objects.all().filter(user_id=user.id)
		# for item in cartItems:

		send_mail(
		    'Guroomed - Order Successful',
		    'New Courses added to your account. Click here to view. '+server_url+'mycourses',
		    'no-reply@guroomed.com',
		    [user.email],
		    fail_silently=False,
		)

		return redirect(server_url+'orderSuccess?status=1&order_id='+str(order.id)+str(course_ids)+'&course_price='+order.course_price+'&tax_price='+order.tax_price+'&discount_price='+order.discount_price+'&total_price='+order.total_price+'&currency='+order.currency)
	else:
		return HttpResponse(payment.error['name'] +' '+ payment.error['message'] )

def paypal_create(request):
	if 'localhost' not in request.build_absolute_uri('/'):
		server_url = request.build_absolute_uri('/')
	else:
		server_url = 'http://localhost:4200/'

	paypalrestsdk.configure({
		"mode": settings.PAYPAL_MODE, # sandbox or live
		"client_id": settings.PAYPAL_CLIENT_ID,
		"client_secret": settings.PAYPAL_CLIENT_SECRET 
	})

	if 'description' not in request.GET:
		description = 'Pay with Paypal'
	else :
		description = request.GET['description']

	cart = UserCart.objects.all().filter(user_id = request.GET['user_id'])
	items = []
	tax = Tax.objects.all()
	for item in cart:
		if item.course_id.discount != 0:
			price = item.course_id.discount
		else:
			price = item.course_id.price
		items.append({
			"name": item.course_id.title,
			"sku": item.course_id.id,
			"price": json.dumps(price, use_decimal=True),
			"tax": json.dumps(round((price * tax[0].value)/100, 2), use_decimal=True),
			"currency": settings.PAYPAL_CURRENCY,
			"quantity": 1
		})

	payment = paypalrestsdk.Payment({
		"intent": "sale",
		"payer": {
			"payment_method": "paypal"
		},
		"redirect_urls": {
			"return_url": server_url+"api/paypal/execute?course_price="+request.GET['course_price']+"&user_id="+request.GET['user_id']+"&tax_price="+str(request.GET['tax_price'])+"&discount_price="+str(request.GET['discount_price'])+"&total_price="+str(request.GET['total_price'])+"&p_currency="+request.GET['p_currency'],
			"cancel_url": server_url+"checkout?status=canceled"
		},
		"transactions": [{
			"item_list": {
				"items": items,
			},
			"amount": {
				"total": json.dumps(round(Decimal(request.GET['total_price']),2), use_decimal=True),
				"currency": settings.PAYPAL_CURRENCY,
				"details": {
                    "subtotal": json.dumps(Decimal(request.GET['course_price'])-Decimal(request.GET['discount_price']), use_decimal=True),
                    "tax": json.dumps(round(Decimal(request.GET['tax_price']),2), use_decimal=True),
                }
            },
			"description": description,
		    # "invoice_number": "48787589673",
		}]
	})
	# return HttpResponse(payment.transactions)

	if payment.create():
		# return HttpResponse(payment.id)
		for link in payment.links:
			if link.rel == "approval_url":
				approval_url = str(link.href)
				return redirect(approval_url)

	else:
		# return HttpResponse(payment)
		return HttpResponse(payment.error['details'])
		return HttpResponse(payment.error['name'] +' '+ payment.error['message'] )