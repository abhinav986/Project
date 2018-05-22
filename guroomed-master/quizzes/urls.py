from django.conf.urls import url
from . import views
from . import quiz, questiontype, question, answer

urlpatterns= [
    # url(r'^$', quiz.index, name='quiz_index'),
    # url(r'^create$', quiz.create, name='quiz_create'),
    url(r'^store$', quiz.store, name='quiz_store'),
    # url(r'^edit/(?P<id>\d+)$', quiz.edit, name='quiz_edit'),
    url(r'^update/(?P<id>\d+)$', quiz.update, name='quiz_update'),
    url(r'^delete/(?P<id>\d+)$', quiz.delete, name='quiz_delete'),
    # url(r'^question-type/$', questiontype.index, name='questiontype_index'),
    # # url(r'^question-type/create$', questiontype.create, name='questiontype_create'),
    url(r'^question-type/store$', questiontype.store, name='questiontype_store'),
    # # url(r'^question-type/edit/(?P<id>\d+)$', questiontype.edit, name='questiontype_edit'),
    # url(r'^question-type/update/(?P<id>\d+)$', questiontype.update, name='questiontype_update'),
    # url(r'^question-type/delete/(?P<id>\d+)$', questiontype.delete, name='questiontype_delete'),

    # url(r'^question/$', question.index, name='question_index'),
    # # url(r'^question/create$', question.create, name='question_create'),
    url(r'^question/store$', question.store, name='question_store'),
    # # url(r'^question/edit/(?P<id>\d+)$', question.edit, name='question_edit'),
    url(r'^question/update/(?P<id>\d+)$', question.update, name='question_update'),
    url(r'^question/delete/(?P<id>\d+)$', question.delete, name='question_delete'),

    # url(r'^answer/$', answer.index, name='answer_index'),
    # # url(r'^answer/create$', answer.create, name='answer_create'),
    # url(r'^answer/store$', answer.store, name='answer_store'),
    # # url(r'^answer/edit/(?P<id>\d+)$', answer.edit, name='answer_edit'),
    # url(r'^answer/update/(?P<id>\d+)$', answer.update, name='answer_update'),
    # url(r'^answer/delete/(?P<id>\d+)$', answer.delete, name='answer_delete'),
]