from django.conf.urls import url
from . import views
from . import category
from . import tag
from . import language
from . import sub_category
from . import instructor
from . import includes
from . import curriculumsection
from . import curriculumlecture
from . import studentreview
from . import es_custom
from . import search


urlpatterns= [
    url(r'^$', views.index, name='course_index'),
    url(r'^mycourses/(?P<id>\d+)$', views.mycourses, name='course_mycourses'),
    url(r'^create$', views.create, name='course_create_form'),
    url(r'^store$', views.store, name='course_create'),
    url(r'^edit/(?P<id>\d+)$', views.edit, name='course_edit'),
    url(r'^show/(?P<id>\d+)$', views.show, name='course_single'),
    url(r'^edit/update/(?P<id>\d+)$', views.update, name='course_update'),
    url(r'^delete/(?P<id>\d+)$', views.delete, name='course_delete'),
    url(r'^frontend/show/(?P<id>\d+)$', views.frontend_show, name='frontend_course_single'),
    url(r'^curriculum/(?P<id>\d+)$', views.getCurriculum, name='get_curriculum'),

    url(r'^cat$', category.index, name='category_index'),
    url(r'^cat/create$', category.create, name='category_create_form'),
    url(r'^cat/store$', category.store, name='category_create'),
    url(r'^cat/edit/(?P<id>\d+)$', category.edit, name='category_edit'),
    url(r'^cat/edit/update/(?P<id>\d+)$', category.update, name='category_update'),
    url(r'^cat/delete/(?P<id>\d+)$', category.delete, name='category_delete'),
    
    url(r'^subcat$', sub_category.index, name='sub_category_index'),
    url(r'^subcat/create$', sub_category.create, name='sub_category_create_form'),
    url(r'^subcat/store$', sub_category.store, name='sub_category_create'),
    url(r'^subcat/edit/(?P<id>\d+)$', sub_category.edit, name='sub_category_edit'),
    url(r'^subcat/edit/update/(?P<id>\d+)$', sub_category.update, name='sub_category_update'),
    url(r'^subcat/delete/(?P<id>\d+)$', sub_category.delete, name='sub_category_delete'),
    
    url(r'^lang$', language.index, name='language_index'),
    url(r'^lang/create$', language.create, name='language_create_form'),
    url(r'^lang/store$', language.store, name='language_create'),
    url(r'^lang/edit/(?P<id>\d+)$', language.edit, name='language_edit'),
    url(r'^lang/edit/update/(?P<id>\d+)$', language.update, name='language_update'),
    url(r'^lang/delete/(?P<id>\d+)$', language.delete, name='language_delete'),
    
    url(r'^instruct$', instructor.index, name='instruct_index'),
    url(r'^instruct/create$', instructor.create, name='instruct_create_form'),
    url(r'^instruct/store$', instructor.store, name='instruct_create'),
    url(r'^instruct/show/(?P<id>\d+)$', instructor.show, name='instruct_show'),
    url(r'^instruct/edit/(?P<id>\d+)$', instructor.edit, name='instruct_edit'),
    url(r'^instruct/edit/update/(?P<id>\d+)$', instructor.update, name='instruct_update'),
    url(r'^instruct/delete/(?P<id>\d+)$', instructor.delete, name='instruct_delete'),
    url(r'^instructor/signup$', instructor.instructor_signup, name='instructor_signup'),
    url(r'^instructor/activate/(?P<uidb64>[0-9A-Za-z_\-\']+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$',
        instructor.activate, name='activate_instructor'),

    url(r'^search$', es_custom.index, name='elasticsearch_index'),
    url(r'^syncdb$', es_custom.syncDB, name='syncdb'),
    url(r'^search/index/create/(?P<name>[a-z0-9_.-]+)$', es_custom.create_index, name='es_create_index'),
    url(r'^search/index/delete/(?P<name>[a-z0-9_.-]+)$', es_custom.delete_index, name='es_delete_index'),
    url(r'^mapping/get/(?P<name>[a-z0-9_.-]+)$', es_custom.mapping_get),
    url(r'^mapping/modify/(?P<name>[a-z0-9_.-]+)$', es_custom.mapping_modify),
    url(r'^search/create$', es_custom.create, name='es_create'),
    url(r'^search/store$', es_custom.store, name='es_store'),
    url(r'^search/edit/(?P<id>\d+)$', es_custom.edit, name='es_edit'),
    url(r'^search/edit/update/(?P<id>\d+)$', es_custom.update, name='es_update'),
    url(r'^search/delete/(?P<id>\d+)$', es_custom.delete, name='es_delete'),
    url(r'^search/form$', search.index, name='es_form'),
    url(r'^search/filters$', search.search, name='es_filter'),

    url(r'^tag/$', tag.index, name='tag_index'),
    url(r'^tag/create$', tag.create, name='tag_create_form'),
    url(r'^tag/store$', tag.store, name='tag_create'),
    url(r'^tag/edit/(?P<id>\d+)$', tag.edit, name='tag_edit'),
    url(r'^tag/edit/update/(?P<id>\d+)$', tag.update, name='tag_update'),
    url(r'^tag/delete/(?P<id>\d+)$', tag.delete, name='tag_delete'),

    url(r'^includes$', includes.index, name='includes_index'),
    url(r'^includes/create$', includes.create, name='includes_create_form'),
    url(r'^includes/store$', includes.store, name='includes_create'),
    url(r'^includes/edit/(?P<id>\d+)$', includes.edit, name='includes_edit'),
    url(r'^includes/edit/update/(?P<id>\d+)$', includes.update, name='includes_update'),
    url(r'^includes/delete/(?P<id>\d+)$', includes.delete, name='includes_delete'),

    url(r'^curriculumsec$', curriculumsection.index, name='curriculumsection_index'),
    url(r'^curriculumsec/create$', curriculumsection.create, name='curriculumsection_create_form'),
    url(r'^curriculumsec/store$', curriculumsection.store, name='curriculumsection_create'),
    url(r'^curriculumsec/edit/(?P<id>\d+)$', curriculumsection.edit, name='curriculumsection_edit'),
    url(r'^curriculumsec/edit/update/(?P<id>\d+)$', curriculumsection.update, name='curriculumsection_update'),
    url(r'^curriculumsec/delete/(?P<id>\d+)$', curriculumsection.delete, name='curriculumsection_delete'),

    url(r'^curriculumlec$', curriculumlecture.index, name='curriculumlecture_index'),
    url(r'^curriculumlec/create$', curriculumlecture.create, name='curriculumlecture_create_form'),
    url(r'^curriculumlec/store$', curriculumlecture.store, name='curriculumlecture_create'),
    url(r'^curriculumlec/edit/(?P<id>\d+)$', curriculumlecture.edit, name='curriculumlecture_edit'),
    url(r'^curriculumlec/edit/update/(?P<id>\d+)$', curriculumlecture.update, name='curriculumlecture_update'),
    url(r'^curriculumlec/delete/(?P<id>\d+)$', curriculumlecture.delete, name='curriculumlecture_delete'),

    url(r'^studentreview$', studentreview.index, name='studentreview_index'),
    url(r'^studentreview/create$', studentreview.create, name='studentreview_create_form'),
    url(r'^studentreview/store$', studentreview.store, name='studentreview_create'),
    url(r'^studentreview/edit/(?P<id>\d+)$', studentreview.edit, name='studentreview_edit'),
    url(r'^studentreview/edit/update/(?P<id>\d+)$', studentreview.update, name='studentreview_update'),
    url(r'^studentreview/delete/(?P<id>\d+)$', studentreview.delete, name='studentreview_delete'),
]