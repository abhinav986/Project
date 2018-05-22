from django.conf.urls import url
from . import views
from . import draft_courses,reject_reasons
from django.urls import path


urlpatterns= [
    url(r'^create/$', draft_courses.create, name='draft_course_create'),
    url(r'^course-basics/(?P<id>\d+)/$', draft_courses.add_basics, name='draft_add_basics'),
    url(r'^course-goals/(?P<id>\d+)/$', draft_courses.add_goals, name='draft_add_goals'),
    url(r'^curriculum-section/(?P<id>\d+)/$', draft_courses.add_sections, name='draft_add_sections'),
    url(r'^curriculum-lecture/(?P<id>\d+)/$', draft_courses.add_lectures, name='draft_add_lectures'),
    url(r'^curriculum/(?P<id>\d+)/$', draft_courses.get_curriculum, name='draft_get_curriculum'),
    url(r'^submit/(?P<id>\d+)/$', draft_courses.draft_submit, name='draft_submit'),
    url(r'^assign/(?P<course_id>\d+)/$', draft_courses.course_assign, name='course_assign'),
    
    url(r'^(?P<id>\d+)/$', views.view_draft, name='view_draft'),
    url(r'^reviewer/action/$', views.reviewer_action, name='reviewer_action'),
    url(r'^manager/action/$', views.manager_action, name='manager_action'),

    path('', reject_reasons.index, name='index'),
    path('create', reject_reasons.create, name='create'),
    path('create_save', reject_reasons.create_save, name='create_save'),
    path('delete<int:id>', reject_reasons.delete, name='delete'),
    path('edit<int:id>', reject_reasons.edit, name='edit'),
    path('edit_save<int:id>', reject_reasons.edit_save, name='edit_save'),
]