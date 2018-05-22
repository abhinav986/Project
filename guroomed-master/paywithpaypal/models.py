from django.db import models
from django.contrib.auth.models import User
from courses.models import Course

class Order(models.Model):
	user_id = models.ForeignKey(User, on_delete=models.CASCADE)
	course_price = models.DecimalField(max_digits=9, decimal_places=2)
	tax_price = models.DecimalField(max_digits=7, decimal_places=2)
	discount_price = models.DecimalField(max_digits=7, decimal_places=2)
	total_price = models.DecimalField(max_digits=9, decimal_places=2)
	currency = models.CharField(max_length=10)
	created_at = models.DateField(auto_now=True)
	updated_at = models.DateField(auto_now=True)

class OrderCourse(models.Model):
	order_id = models.ForeignKey(Order, on_delete=models.CASCADE)
	course_id = models.ForeignKey(Course, on_delete=models.CASCADE)
	course_price = models.DecimalField(max_digits=9, decimal_places=2)

class Payment(models.Model):
	order_id = models.ForeignKey(Order, on_delete=models.CASCADE)
	course_price = models.DecimalField(max_digits=9, decimal_places=2, null=True)
	tax_price = models.DecimalField(max_digits=7, decimal_places=2, null=True)
	discount_price = models.DecimalField(max_digits=7, decimal_places=2, null=True)
	total_price = models.DecimalField(max_digits=9, decimal_places=2, null=True)
	currency = models.CharField(max_length=10)
	payment_status_choices = (('successful','successful'),('failed','failed'))
	payment_status = models.CharField(max_length=12, choices=payment_status_choices)
	created_at = models.DateField(auto_now=True)
	updated_at = models.DateField(auto_now=True)

class PaypalDetail(models.Model):
	order_id = models.ForeignKey(Order, on_delete=models.CASCADE)
	payment_id = models.CharField(max_length=100)
	state = models.CharField(max_length=30, null=True)
	cart = models.CharField(max_length=30, null=True)
	payer_payment_method = models.CharField(max_length=30, null=True)
	payer_status = models.CharField(max_length=50, null=True)
	payer_email = models.CharField(max_length=255, null=True)
	payer_id = models.CharField(max_length=100, null=True)
	payer_country_code = models.CharField(max_length=10, null=True)
	transactions_amount = models.DecimalField(max_digits=9, decimal_places=2, null=True)
	transactions_currency = models.CharField(max_length=10, null=True)
	payee_merchant_id = models.CharField(max_length=50, null=True)
	payee_email = models.CharField(max_length=255, null=True)
	description = models.CharField(max_length=500, null=True)
	payment_mode = models.CharField(max_length=50, null=True)
	reason_code = models.CharField(max_length=50, null=True)
	protection_eligibility = models.CharField(max_length=50, null=True)
	transaction_fee = models.DecimalField(max_digits=5, decimal_places=2, null=True)
	created_at = models.DateField(auto_now=True, null=True)
	updated_at = models.DateField(auto_now=True, null=True)

class Tax(models.Model):
	name = models.CharField(max_length=30, null=True)
	description = models.CharField(max_length=100, null=True)
	value = models.DecimalField(max_digits=5, decimal_places=2)