from django.shortcuts import render, redirect, get_object_or_404
from .models import Payment
from django.contrib.auth.models import User


def index(request):
    payments = Payment.objects.all()
    context = {'payments': payments}
    return render(request, 'payments/paymentlisting.html', context)

def delete(request, id):
    payment = Payment.objects.get(id=id)
    payment.delete()
    return redirect('/api/paypal/payments')