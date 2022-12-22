from .base import *
import os
from decouple import config


try:
    from .local import *
except ImportError:
    pass

SECRET_KEY = config('DJANGO_SECRET_KEY')
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
# Note: for now, we are using the AWS naming-convention from Boto3
AWS_S3_REGION_NAME = os.getenv("AWS_S3_REGION_NAME", "sfo3")
AWS_ACCESS_KEY_ID = os.getenv("AWS_ACCESS_KEY_ID")
AWS_SECRET_ACCESS_KEY = os.getenv("AWS_SECRET_ACCESS_KEY")
AWS_STORAGE_BUCKET_NAME = os.getenv("AWS_STORAGE_BUCKET_NAME")
AWS_LOCATION = os.getenv("AWS_LOCATION", "static")
PUBLIC_MEDIA_LOCATION = os.getenv("PUBLIC_MEDIA_LOCATION", "media")
AWS_DEFAULT_ACL = "public-read"
AWS_S3_ENDPOINT_URL = f"https://{AWS_S3_REGION_NAME}.digitaloceanspaces.com"
AWS_S3_OBJECT_PARAMETERS = {"CacheControl": "max-age=86400"}
