from django.shortcuts import render, redirect, get_object_or_404
from .models import PaypalDetail
from django.contrib.auth.models import User


def index(request):
    paypaldbs = PaypalDetail.objects.all()
    context = {'paypaldbs': paypaldbs}
    return render(request, 'paypaldb/paypaldblisting.html', context)

# def show(request, id):
#     paypaldb = PaypalDetail.objects.get(id=id)
#     context = {'paypaldb': paypaldb}
#     return render(request, 'paypaldb/paypaldbsingle.html', context)

def delete(request, id):
    paypaldb = PaypalDetail.objects.get(id=id)
    paypaldb.delete()
    return redirect('/api/paypal/paypaldb')