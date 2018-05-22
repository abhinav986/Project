from django.conf.urls import url, include

from . import views
from . import all_users
from . import usercart
from . import user_permi
from . import usercourses
from . import inprogress
from django.contrib.auth import views as auth_views

# from django.conf.urls import url, include
# from django.views import generic
# from rest_framework.schemas import get_schema_view
# from rest_framework_simplejwt.views import (
#     TokenObtainPairView,
#     TokenRefreshView,
# )

urlpatterns = [

    url(r'^login', views.login_form, name='login_form'),
    url(r'^logout', views.custom_logout, name='custom_logout'),
    url(r'^frontend/logout', views.frontend_logout, name='frontend_logout'),
    url(r'^authlogin', views.custom_login, name='custom_login'),
    url(r'^changepd', views.change_password, name='change_password'),
    url(r'^signup/$', views.custom_signup, name='custom_signup'),
    url(r'^frontend/signup/$', views.frontend_signup, name='frontend_signup'),
    url(r'^frontend/login', views.frontend_login, name='frontend_login'),
    url(r'^frontend/verifyjwt', views.verify_jwt, name='verify_jwt'),
    url(r'^password_reset/$', views.password_reset, name='password_reset'),
    url(r'^reset/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$', views.password_reset_confirm, name='password_reset_confirm'),
    url(r'^password_change/$', views.password_change, name='password_change'),

    url('^', include('django.contrib.auth.urls')),

    url(r'^users$', all_users.index, name='users_index'),
    url(r'^users/create$', all_users.create, name='users_create_form'),
    url(r'^users/store$', all_users.store, name='users_create'),
    url(r'^users/show/(?P<id>\d+)$', all_users.show, name='users_show'),
    url(r'^users/edit/(?P<id>\d+)$', all_users.edit, name='users_edit'),
    url(r'^users/edit/update/(?P<id>\d+)$', all_users.update, name='users_update'),
    url(r'^users/delete/(?P<id>\d+)$', all_users.delete, name='users_delete'),
    url(r'^users/profile/$', all_users.getProfile, name='getProfile'),
    url(r'^users/profile/store$', all_users.storeProfile, name='storeProfile'),
    url(r'^users/profile/store/picture$', all_users.storeProfilePicture, name='storeProfilePicture'),

    url(r'^usercourses$', usercourses.index, name='usercourses_index'),
    url(r'^usercourses/create$', usercourses.create, name='usercourses_create_form'),
    # url(r'^usercourses/frontend/store$', usercourses.store_frontend, name='usercourses_maped'),
    url(r'^usercourses/store$', usercourses.store, name='usercourses_create'),
    url(r'^usercourses/edit/(?P<id>\d+)$', usercourses.edit, name='usercourses_edit'),
    url(r'^usercourses/edit/update/(?P<id>\d+)$', usercourses.update, name='usercourses_update'),
    url(r'^usercourses/delete/(?P<id>\d+)$', usercourses.delete, name='usercourses_delete'),

    url(r'^inprogress$', inprogress.index, name='inprogress_index'),
    url(r'^inprogress/create$', inprogress.create, name='inprogress_create_form'),
    url(r'^inprogress/store$', inprogress.store, name='inprogress_create'),
    url(r'^inprogress/edit/(?P<id>\d+)$', inprogress.edit, name='inprogress_edit'),
    url(r'^inprogress/edit/update/(?P<id>\d+)$', inprogress.update, name='inprogress_update'),
    url(r'^inprogress/delete/(?P<id>\d+)$', inprogress.delete, name='inprogress_delete'),

    url(r'^permissions$', user_permi.index, name='permissions_index'),
    url(r'^permissions/create$', user_permi.create, name='permissions_form'),
    url(r'^permissions/store$', user_permi.store, name='permissions_create'),
    url(r'^permissions/edit/(?P<id>\d+)$', user_permi.edit, name='permissions_edit'),
    url(r'^permissions/edit/update/(?P<id>\d+)$', user_permi.update, name='permissions_update'),
    url(r'^permissions/delete/(?P<id>\d+)$', user_permi.delete, name='permissions_update_delete'),

    url(r'^usercart/add$', usercart.addCart),
    url(r'^usercart/get/(?P<id>\d+)$', usercart.getCart),
    url(r'^usercart/delete/(?P<id>\d+)$', usercart.deleteCart),

    url(r'^$', views.frontend, name=''),
]