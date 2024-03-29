"""
Django settings for SarandONGa project.
Generated by 'django-admin startproject' using Django 4.1.4.
For more information on this file, see
https://docs.djangoproject.com/en/4.1/topics/settings/
For the full list of settings and their values, see
https://docs.djangoproject.com/en/4.1/ref/settings/
"""

from pathlib import Path
from decouple import config
import os
import braintree


# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = config('DJANGO_SECRET_KEY')


# Braintree settings
BRAINTREE_MERCHANT_ID = '93rqkcmqsz4sh4z5'  # Merchant ID
BRAINTREE_PUBLIC_KEY = 'hb24v8ns5dy6c3v4'  # Public Key
BRAINTREE_PRIVATE_KEY = 'efd21c055193c1dc43707bb28446570f'  # Private key

BRAINTREE_CONF = braintree.Configuration(
    braintree.Environment.Sandbox,
    BRAINTREE_MERCHANT_ID,
    BRAINTREE_PUBLIC_KEY,
    BRAINTREE_PRIVATE_KEY
)

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = [

]


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'main',
    'person',
    'donation',
    'subsidy',
    'stock',
    'service',
    'payment',
    'localflavor',
    'project',
    'home',
    'ong',
    'sponsorship',
]

AUTH_USER_MODEL = 'person.Worker'

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'SarandONGa.middleware.custom_404_middleware.Custom404Middleware',
]

ROOT_URLCONF = 'SarandONGa.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                'SarandONGa.context_processors.user_info',
            ],
        },
    },
]

WSGI_APPLICATION = 'SarandONGa.wsgi.application'


# Database
# https://docs.djangoproject.com/en/4.1/ref/settings/#databases

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.mysql",
        "NAME": "sarandongadb",
        "USER": "sarandonga-user",
        "PASSWORD": "sarandonga-password",
        "HOST": "127.0.0.1",
        "PORT": "3307",
    }
}


# Password validation
# https://docs.djangoproject.com/en/4.1/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/4.1/topics/i18n/

LANGUAGE_CODE = 'es'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.1/howto/static-files/

STATIC_URL = 'static/'
# MEDIA_ROOT = os.path.join(BASE_DIR, 'media')

STATICFILES_DIRS = [
    os.path.join(BASE_DIR, "static"),
]

EMAIL_HOST = 'smtp.gmail.com'
EMAIL_HOST_USER = 'sarandonga.contact@gmail.com'
EMAIL_HOST_PASSWORD = config('MAIL_KEY')
EMAIL_PORT = 587
EMAIL_USE_TLS = True


# Default primary key field type
# https://docs.djangoproject.com/en/4.1/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

LOGIN_REDIRECT_URL = "/"
LOGOUT_REDIRECT_URL = "/"
LOGIN_URL = "/login"
