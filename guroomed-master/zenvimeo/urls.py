from django.conf.urls import url

from . import views
from . import autodesk

urlpatterns = [
    url(r'^$', views.login_oauth, name='login_oauth'),
    url(r'^thanks/$', views.login_oauth, name='login_oauth'),
    url(r'^success/', views.vimeo_success, name='vimeo_success'),
    url(r'^upload/', views.vimeo_upload, name='vimeo_upload'),
    url(r'^fupload/', views.fupload, name='fupload'),
    url(r'^delete/', views.vimeo_delete, name='vimeo_delete'),
    url(r'^view/', views.group_list, name='group_list'),
    url(r'^autodesk/360/', views.autodesk, name='autodesk_360'),
    url(r'^autodesk/forge/', views.autodesk_forge, name='autodesk_forge'),
    url(r'^autodesk/auth/token', autodesk.get_token, name='autodesk_forge_get_token'),
    url(r'^autodesk/bucket/create', autodesk.bucket_create, name='autodesk_create_bucket'),
    url(r'^autodesk/bucket/check', autodesk.bucket_check, name='autodesk_check_bucket'),
    url(r'^autodesk/bucket/upload', autodesk.bucket_upload, name='autodesk_bucket_upload'),
    url(r'^autodesk/bucket/convertfile', autodesk.convert_file, name='autodesk_convert_file'),
    url(r'^autodesk/bucket/status', autodesk.file_status, name='autodesk_file_status'),
    url(r'^(?P<group>[0-9]+)/', views.vim_list, name='vim_list'),
]