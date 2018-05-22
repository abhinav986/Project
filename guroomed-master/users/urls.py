from django.conf.urls import url
from . import views
from . import managers
from . import reviewers


urlpatterns= [
	url(r'^auth/$', views.get_JWTtoken, name='get_JWTtoken'),

	url(r'^dashboard/(?P<role_id>\d+)/(?P<status_id>\d+)/$', views.view_dashboard, name='dashboard'),
	url(r'^reviewer/create/$', reviewers.create, name='reviewer_create'),
	url(r'^reviewer/edit/(?P<id>\d+)/$', reviewers.edit, name='reviewer_edit'),
	url(r'^reviewer/delete/(?P<id>\d+)/$', reviewers.delete, name='reviewer_delete'),
	url(r'^reviewer/listing/(?P<manager_id>\d+)/(?P<sub_cat_id>\d+)/$', reviewers.listing, name='reviewer_listing'),
	
	url(r'^manager/listing/$', managers.listing, name='manager_listing'),
	url(r'^manager/create/$', managers.create, name='manager_create'),
	url(r'^manager/edit/(?P<id>\d+)/$', managers.edit, name='manager_edit'),
	url(r'^manager/password/(?P<id>\d+)/$', managers.password, name='manager_password'),
	url(r'^manager/delete/(?P<id>\d+)/$', managers.delete, name='manager_delete'),
	url(r'^manager/assign-sub/(?P<id>\d+)/$', managers.assign_sub, name='manager_assign_sub'),
]