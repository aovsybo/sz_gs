"""
Django settings for config project.

Generated by 'django-admin startproject' using Django 5.0.1.

For more information on this file, see
https://docs.djangoproject.com/en/5.0/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/5.0/ref/settings/
"""

import os
from pathlib import Path

from dotenv import load_dotenv

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent.parent
load_dotenv(BASE_DIR / ".env")


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/5.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = os.environ.get("SECRET_KEY"),

SKOROZVON_LOGIN = os.environ.get("SKOROZVON_LOGIN")
SKOROZVON_API_KEY = os.environ.get("SKOROZVON_API_KEY")
SKOROZVON_APPLICATION_ID = os.environ.get("SKOROZVON_APPLICATION_ID")
SKOROZVON_APPLICATION_KEY = os.environ.get("SKOROZVON_APPLICATION_KEY")

GS_SCOPES = os.environ.get("GS_SCOPES").split(',')
GS_TABLE_ID = os.environ.get("GS_TABLE_ID")
GS_MAIN_SHEET_ID = os.environ.get("GS_MAIN_SHEET_ID")
GS_MAIN_SHEET_NAME = "Шаблон"
SKOROZVON_TO_GS_NAME = {
    "ЮСИ. Лидген Авито РНД": "ЮСИ. Лидген с Авито РнД",
    "22.12.23 ЮСИ база Крд": "ЮСИ. ГКЦ РнД",
    "ЮСИ. Сайты ЖК РНД (проект с оплатой за лид)": "ЮСИ. Сайты ЖК РнД. (Проект с оплатой за лид)",
    "ЮСИ.СТВ Лидген с Авито ": "ЮСИ. Лидген с Авито Ств",
    "ЮСИ ГКЦ Ств": "ЮСИ. ГКЦ Ств",
    "ЮСИ. Сайты ЖК Ств (проект с оплатой за лид) ": "ЮСИ. Сайты ЖК Ств. (Проект с оплатой за лид)",
    "ЮСИ Сайты Крд (проект с оплатой за лид)": "ЮСИ. Сайты ЖК Крд. (Проект с оплатой за лид)",
    "ЮСИ ГКЦ Крд": "ЮСИ. ГКЦ Крд"
}
# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = os.environ.get("ALLOWED_HOSTS").split(',')

# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    'rest_framework',

    'integrations',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'config.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / 'templates']
        ,
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

WSGI_APPLICATION = 'config.wsgi.application'


# Database
# https://docs.djangoproject.com/en/5.0/ref/settings/#databases


DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME':  os.environ.get("MYSQL_DB"),
        'USER':  os.environ.get("MYSQL_USER"),
        'PASSWORD':  os.environ.get("MYSQL_PASSWORD"),
        'HOST':  os.environ.get("MYSQL_HOST"),
        'PORT':  os.environ.get("POSTGRES_PORT", 3306),
    }
}


# Password validation
# https://docs.djangoproject.com/en/5.0/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]


# Internationalization
# https://docs.djangoproject.com/en/5.0/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/5.0/howto/static-files/

STATIC_URL = 'static/'

# Default primary key field type
# https://docs.djangoproject.com/en/5.0/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
