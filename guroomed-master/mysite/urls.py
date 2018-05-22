# Copyright 2015 Google Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

from django.conf.urls import include, url
from django.urls import path
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth.views import login
from rest_framework_jwt.views import obtain_jwt_token
from guroomed import views as guroomed_views

urlpatterns = [
    url(r'^api/', include('guroomed.urls')),
    url(r'^api/videos/', include('zenvimeo.urls')),
    url(r'^api/homepage/', include('homepage.urls')),
    url(r'^api/courses/', include('courses.urls')),
    url(r'^api/paypal/', include('paywithpaypal.urls')),
    url(r'^api/user/', include('users.urls')),
    url(r'^api/draft/', include('drafts.urls')),
    url(r'^api/admin/', admin.site.urls),
    url(r'^api/quiz/', include('quizzes.urls')),
    url(r'^', include('guroomed.urls')),
    # url(r'^api/api-token-auth/', obtain_jwt_token, name="jwttoken"),
    # path('<path:path>/', guroomed_views.frontendRoutes, name="frontend_index"),
    # url(r'^(?P<path>.*)/$', guroomed_views.frontendRoutes, name="index"),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)