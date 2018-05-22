from django.conf.urls import url
from django.contrib import admin
from . import views
from . import infostrip
from . import footerstrip

urlpatterns = [
    url(r'^$', views.HomeData.as_view()),

    url(r'^infostrip$', infostrip.index, name='infostrip_index'),
    url(r'^infostrip/create$', infostrip.create, name='infostrip_create_form'),
    url(r'^infostrip/store$', infostrip.store, name='infostrip_create'),
    url(r'^infostrip/edit/(?P<id>\d+)$', infostrip.edit, name='infostrip_edit'),
    url(r'^infostrip/edit/update/(?P<id>\d+)$', infostrip.update, name='infostrip_update'),
    url(r'^infostrip/delete/(?P<id>\d+)$', infostrip.delete, name='infostrip_delete'),

    url(r'^fstrip$', footerstrip.index, name='footerstrip_index'),
    url(r'^fstrip/create$', footerstrip.create, name='footerstrip_create_form'),
    url(r'^fstrip/store$', footerstrip.store, name='footerstrip_create'),
    url(r'^fstrip/edit/(?P<id>\d+)$', footerstrip.edit, name='footerstrip_edit'),
    url(r'^fstrip/edit/update/(?P<id>\d+)$', footerstrip.update, name='footerstrip_update'),
    url(r'^fstrip/delete/(?P<id>\d+)$', footerstrip.delete, name='footerstrip_delete'),
]