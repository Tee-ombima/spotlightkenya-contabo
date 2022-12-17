from .base import *
import os
from decouple import config


try:
    from .local import *
except ImportError:
    pass

SECRET_KEY = config('SECRET_KEY')
DEBUG = False
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': config('DB_NAME'),
        'HOST': config('DB_HOST'),
        'USER': config('DB_USER'),
        'PASSWORD': config('DB_PASSWORD'),
        'PORT': '5432',
    }
}

#SESSION_COOKIE_SECURE = True
#CSRF_COOKIE_SECURE=True
#SECURE_SSL_REDIRECT = True

#SECURE_HSTS_SECONDS= 31536000
#SECURE_HSTS_PRELOAD = True
#SECURE_HSTS_INCLUDE_SUBDOMAINS=True
