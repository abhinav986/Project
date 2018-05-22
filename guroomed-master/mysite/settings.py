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

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.8/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'pf-@jxtojga)z+4s*uwbgjrq$aep62-thd0q7f&o77xtpka!_m'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

# SECURITY WARNING: App Engine's security features ensure that it is safe to
# have ALLOWED_HOSTS = ['*'] when the app is deployed. If you deploy a Django
# app not on App Engine, make sure to set an appropriate host here.
# See https://docs.djangoproject.com/en/1.10/ref/settings/
ALLOWED_HOSTS = ['*']

# Application definition

INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'rolepermissions',
    'embed_video',
    'elasticsearch',
    'social_django',
    # 'rest_framework',
    'courses',
    'guroomed',
    'homepage',
    'paywithpaypal',
    'zenvimeo',
    'drafts',
    'users',
    'quizzes',
)

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'social_django.middleware.SocialAuthExceptionMiddleware',
]


ROOT_URLCONF = 'mysite.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.media',
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                'social_django.context_processors.backends',
                'social_django.context_processors.login_redirect',
            ],
        },
    },
]

EMBED_VIDEO_BACKENDS = (
    'zenvimeo.backends.ZenVimeoBackend',
)

WSGI_APPLICATION = 'mysite.wsgi.application'

AUTHENTICATION_BACKENDS = (
    'social_core.backends.open_id.OpenIdAuth',
    'social_core.backends.facebook.FacebookOAuth2',
    'social_core.backends.google.GoogleOAuth',
    'social_core.backends.google.GoogleOpenId',
    'social_core.backends.google.GoogleOAuth2',
    'django.contrib.auth.backends.ModelBackend',
)

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'guroomed',
        'USER': 'postgres',
        'PASSWORD': 'postgres',
        'HOST': 'localhost',
        'PORT': '',
    }
}

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


STATIC_URL = '/static/'
STATIC_ROOT = 'static/'

MEDIA_ROOT = 'media/'
MEDIA_URL = '/media/'

# REST_FRAMEWORK = {
#     'DEFAULT_PERMISSION_CLASSES': (
#         'rest_framework.permissions.IsAuthenticated',
#     ),
#     'DEFAULT_AUTHENTICATION_CLASSES': (
#         'rest_framework_simplejwt.authentication.JWTAuthentication',
#         'rest_framework.authentication.SessionAuthentication',
#         # 'rest_framework.authentication.BasicAuthentication',
#     ),
#     # 'DEFAULT_RENDERER_CLASSES': (
#     #     'rest_framework.renderers.JSONRenderer',
#     #     'rest_framework.renderers.BrowsableAPIRenderer',
#     # )
# }


# Adding roles to user for managing notes
ROLEPERMISSIONS_MODULE = 'mysite.roles'

LOGIN_URL = 'login'
LOGOUT_URL = 'logout'
LOGIN_REDIRECT_URL = 'index'

SOCIAL_AUTH_FACEBOOK_KEY = '111928296072462'
SOCIAL_AUTH_FACEBOOK_SECRET = '858ecdcd9782a34f7fc49ee644f6d09f'
SOCIAL_AUTH_GOOGLE_OAUTH2_KEY = '659654452019-7cmffctlmudlg1ehl4idhbv3410pou2r.apps.googleusercontent.com'
SOCIAL_AUTH_GOOGLE_OAUTH2_SECRET = 'i3Q46Is9EeLiEnea_I6YHQDn'

PAYPAL_MODE = 'sandbox'
PAYPAL_CLIENT_ID = 'Ab0ERv426c3LYIJX0Ipmv7qn2rVnGR9VtGT03Ei5_wZEwmTN9f8AEtdwQdUGnxixO708DA5JjGz607Or'
PAYPAL_CLIENT_SECRET = 'EGmfrsZC0rueulxjUVKy4VV9neVTDdmAfTk5uOe6nmOUl2bOxyBUOeoLDtGTfDBkucNJCxUr77-jAYIZ'
PAYPAL_CURRENCY = 'USD'

# VIMEO_CLIENT_ID = 'b7baa439ea567788a4148c657c07e93ec4db8297'
# VIMEO_CLIENT_SECRET = 'zCEqW4WgzW5tTIslhj5fhJeH6FZLIx/viDI/G9Jm9l+R2ZaHKnpWAwRbZU9Fax4CmB1lHb8Dv0EA2R8i8SgJTlEBoAYcOTZ8n50hEEQ5Ksin0AajMYpa+Mc/31qKyOI3'
# VIMEO_ACCESS_TOKEN = '00f2e9edee60097de39e5059f4834f57'

VIMEO_CLIENT_ID = '6869620e96ab6edae1edcf435217fe6795d2de11'
VIMEO_CLIENT_SECRET = 'mgTalcAB2pBKf5DBE1IOAlaOT5P7icvKYl9ufCr9tmhDvRlmJAtqysbY8XbYkaH1gVv81XXdaYLjGDCWYmJUO/MRhwNwDOAL6sbdOXTsxX18fYqMGZ6wxKdiqf1TYxdz'
VIMEO_ACCESS_TOKEN = 'e44431abe8a0611f2de0892343749552'

EMAIL_HOST = 'smtp.gmail.com'
EMAIL_PORT = 465
EMAIL_HOST_USER = 'zenrays.amruta@gmail.com'
EMAIL_HOST_PASSWORD = 'pi3.1415'
EMAIL_USE_SSL = True
DEFAULT_FROM_EMAIL = 'Guroomed <noreply@guroomed.com>'

FILE_UPLOAD_MAX_MEMORY_SIZE = 10

ATOMIC_REQUESTS = True

AUTOCOMMIT = True
