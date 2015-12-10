"""
Django settings for flocs project.

Generated by 'django-admin startproject' using Django 1.8.2.

For more information on this file, see
https://docs.djangoproject.com/en/1.8/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.8/ref/settings/
"""

import dj_database_url
import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

FRONTEND_DIR = os.path.join(BASE_DIR, 'frontend')

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.8/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '-zocq!_l$gw_@cc1u7l$7j8y=b&+t2e4^e9bmx1&rk0ztp*&dj'

ON_SERVER = os.getenv('ON_AL', "False") == "True"
DEBUG = os.getenv('DJANGO_DEBUG', "False") == "True"
if not ON_SERVER:
    DEBUG = True
ALLOWED_HOSTS = ['*']

if ON_SERVER:
    # for production:
    FRONTEND_BUILD_DIR = os.path.join(BASE_DIR, 'frontend', 'production-build')
else:
    # for development:
    FRONTEND_BUILD_DIR = os.path.join(BASE_DIR, 'frontend', 'development-build')


# Application definition

INSTALLED_APPS = (
    # django
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    # third party
    'django_extensions',

    # our apps
    'common',
    'tasks',
    'practice',
    'flocs',
)

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'django.middleware.security.SecurityMiddleware',
)

ROOT_URLCONF = 'flocs.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',

        # frontend home directory (where to search for index.html)
        'DIRS': [FRONTEND_BUILD_DIR],

        # allow for fallback index.html in flocs/templates/
        'APP_DIRS': True,

        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'flocs.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.8/ref/settings/#databases

DATABASES = {"default": dj_database_url.config(default='sqlite:///' + os.path.join(BASE_DIR, 'db.sqlite3'))}


# Internationalization
# https://docs.djangoproject.com/en/1.8/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = False


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.8/howto/static-files/

STATIC_URL = '/static/'
STATICFILES_DIRS = (
    os.path.join(FRONTEND_BUILD_DIR, 'static'),
)
STATIC_ROOT = os.path.join(BASE_DIR, '../static')

LOGGING_DIR = os.getenv('LOGGING_DIR', "logs")
LOGGING = {
        'version': 1,
        'formatters': {
            'production': {
                'format': '[%(asctime)s] %(levelname)s %(module)s "%(message)s"'
                },
            'devel': {
                'format': '[%(asctime)s] %(levelname)s %(module)s : "%(message)s" in %(filename)s:%(lineno)s'
                },
            'request': {
                'format': '[%(asctime)s] %(levelname)s %(message)s'
                }
            },
        'handlers': {
            'practice': {
                'level': 'DEBUG',
                'class': 'logging.FileHandler',
                'filename': LOGGING_DIR + '/practice.log',
                'formatter': 'devel'
                },
            'requests': {
                'level': 'DEBUG',
                'class': 'logging.FileHandler',
                'filename': LOGGING_DIR + '/requests.log',
                'formatter': 'request'
                }
            },
        'loggers': {
            'practice': {
                'handlers': ['practice'],
                'level': 'DEBUG',
                'propagate': True
                },
            'django.request' : {
                'handlers': ['requests'],
                'level': 'DEBUG',
                'propagate': True
            }
        }
    }
