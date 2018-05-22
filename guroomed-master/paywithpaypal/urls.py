from django.conf.urls import url
from . import views
from . import orders, payments, paypaldb, checkout, paypal, tax

urlpatterns= [

    url(r'^orders/$', orders.index, name='orders_index'),
    url(r'^orders/(?P<id>\d+)$', orders.show, name='orders_show'),
    url(r'^orders/delete/(?P<id>\d+)$', orders.delete, name='orders_delete'),

    url(r'^taxes/$', tax.index, name='orders_index'),
    url(r'^taxes/create$', tax.create, name='orders_create'),
    url(r'^taxes/store$', tax.store, name='orders_store'),
    url(r'^taxes/delete/(?P<id>\d+)$', tax.delete, name='orders_delete'),

    url(r'^payments/$', payments.index, name='payments_index'),
    url(r'^payments/delete/(?P<id>\d+)$', payments.delete, name='payments_delete'),

    url(r'^paypaldb/$', paypaldb.index, name='paypaldb_index'),
    # url(r'^paypaldb/(?P<id>\d+)$', paypaldb.show, name='paypaldb_show'),
    url(r'^paypaldb/delete/(?P<id>\d+)$', paypaldb.delete, name='paypaldb_delete'),

    url(r'^create$', paypal.paypal_create),
    url(r'^execute$', paypal.paypal_execute),
    url(r'^checkout/$', checkout.display, name='checkout_display'),
]