"""
Django settings for real_estate project.

Generated by 'django-admin startproject' using Django 3.0.

For more information on this file, see
https://docs.djangoproject.com/en/3.0/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/3.0/ref/settings/
"""

import os
from decouple import config

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
PROJECT_NAME = 'real_estate'


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.0/howto/deployment/checklist/

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = config('DJANGO_DEBUG', default=True, cast=bool)
DEBUG_PROPAGATE_EXCEPTIONS = True

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = config(
    'SECRET_KEY',
    default='k+_y0&-+l^@7w+y3%6#c4wav1bvd7k9p(z%m5m-c00*5ssu7$7'
)

ALLOWED_HOSTS = ['inmobiliaria2020.herokuapp.com', '127.0.0.1', '0.0.0.0', '*']

# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'search',
    'storages',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware'
]

ROOT_URLCONF = '{PROJECT_NAME}.urls'.format(PROJECT_NAME=PROJECT_NAME)

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, PROJECT_NAME, 'templates')],
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

WSGI_APPLICATION = '{PROJECT_NAME}.wsgi.application'.format(
    PROJECT_NAME=PROJECT_NAME
)

# Database
# https://docs.djangoproject.com/en/3.0/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'real_estate',
        'USER': 'postgres',
        'PASSWORD': 'root',
        'HOST': 'localhost',
        'PORT': '5432',
    }
}

# Password validation
# https://docs.djangoproject.com/en/3.0/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.\
UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.\
MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.\
CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.\
NumericPasswordValidator',
    },
]


# Internationalization
# https://docs.djangoproject.com/en/3.0/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.0/howto/static-files/

STATICFILES_DIRS = [
    os.path.join(BASE_DIR, PROJECT_NAME, 'static'),
]

TEMPLATE_DIRS = [
    os.path.join(BASE_DIR, PROJECT_NAME, 'templates'),
]

STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles', 'static-root')
MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'staticfiles', "media-root")

if config('DJANGO_PRODUCTION_ENV', default=False, cast=bool):
    from .settings_production import DATABASES as db
    DATABASES = db
    AWS_DEFAULT_ACL = None
    AMAZON_DOMAIN = 's3-sa-east-1.amazonaws.com'
    AWS_ACCESS_KEY_ID = config(
        'AWS_ACCESS_KEY_ID',
        default='AKIAYP73WOXS3Q4UFDUN'
    )
    AWS_SECRET_ACCESS_KEY = config(
        'AWS_SECRET_ACCESS_KEY',
        default='qPpcCnHHGV1/zvmTCVmbFAIRN1LHVfi9pKNT+w1d'
    )
    AWS_STORAGE_BUCKET_NAME = config(
        'AWS_STORAGE_BUCKET_NAME',
        default='inmobiliaria'
    )
    AWS_S3_CUSTOM_DOMAIN = '{AWS_STORAGE_BUCKET_NAME}.{AMAZON_DOMAIN}'.format(
        AWS_STORAGE_BUCKET_NAME=AWS_STORAGE_BUCKET_NAME,
        AMAZON_DOMAIN=AMAZON_DOMAIN,
    )
    AWS_S3_OBJECT_PARAMETERS = {
        'CacheControl': 'max-age=86400',
    }
    AWS_LOCATION = 'static'
    STATIC_URL = 'https://{AWS_S3_CUSTOM_DOMAIN}/{AWS_LOCATION}/'.format(
        AWS_S3_CUSTOM_DOMAIN=AWS_S3_CUSTOM_DOMAIN,
        AWS_LOCATION=AWS_LOCATION,
    )
    STATICFILES_STORAGE = 'storages.backends.s3boto3.S3Boto3Storage'
    DEFAULT_FILE_STORAGE = 'real_estate.storage_backends.MediaStorage'
