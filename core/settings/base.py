"""
Django settings for wf_website project.

Generated by 'django-admin startproject' using Django 2.1.3.

For more information on this file, see
https://docs.djangoproject.com/en/2.1/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/2.1/ref/settings/
"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os
from decouple import config

from braintree import Configuration as BraintreeConfiguration
from braintree import Environment as BraintreeEnvironment
import dj_database_url

from dotenv import load_dotenv

load_dotenv()

# TODO: set this to a secure value before deploying to production
ALLOWED_HOSTS = ["www.spotlightkenya.club", "spotlightkenya.club", "127.0.0.1","0.0.0.0",
                 "localhost",'spotlight-kenya.herokuapp.com']
CSRF_TRUSTED_ORIGINS = ['https://www.spotlightkenya.club']
PROJECT_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
BASE_DIR = os.path.dirname(PROJECT_DIR)

AUTH_USER_MODEL = "accounts.User"
SECRET_KEY = "96yjsswp=2)rr3@9&-p2rx*2#*vo*0afk9%8egu&an#0a@el)9"
CART_SESSION_ID = "cart"

# Braintree settings
BRAINTREE_MERCHANT_ID = os.getenv("BRAINTREE_MERCHANT_ID")
BRAINTREE_PUBLIC_KEY = os.getenv("BRAINTREE_PUBLIC_KEY")
BRAINTREE_PRIVATE_KEY = os.getenv("BRAINTREE_PRIVATE_KEY")

BraintreeConfiguration.configure(
    BraintreeEnvironment.Sandbox,
    BRAINTREE_MERCHANT_ID,
    BRAINTREE_PUBLIC_KEY,
    BRAINTREE_PRIVATE_KEY,
)

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/2.1/howto/deployment/checklist/


# Application definition

INSTALLED_APPS = [


    'whitenoise.runserver_nostatic',
    "wagtailemoji",
    "accounts",

    "community",
    "contact",
    "content_migration",
    "documents",
    "events",
    "blogs",
    "facets",
    "forms",
    "home",
    "library",
    "memorials",
    "navigation",



    "search",

    "subscription",
    "wagtailpod",
    "magazine",
    "streams",
    "wf_pages",
    "wagtail.contrib.forms",
    "wagtail.contrib.modeladmin",
    "wagtail.contrib.redirects",
    "wagtail.contrib.routable_page",
    "wagtail.contrib.settings",
    "wagtail.contrib.styleguide",
    "wagtail.embeds",
    "wagtail.sites",
    "wagtail.users",
    "wagtail.snippets",
    "wagtail.documents",
    "wagtail.images",
    "wagtail.search",
    "wagtail.admin",
    "wagtail.core",
    "modelcluster",
    "taggit",
    "hitcount",
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    'django.contrib.sites',

    "django.contrib.sitemaps",
    "crispy_forms",
    "flatpickr",
    "wagtail_color_panel",
    "wagtailfontawesome",
    "wagtailmedia",

]

CRISPY_TEMPLATE_PACK = "bootstrap4"

SITE_ID = 1

MIDDLEWARE = [
    'whitenoise.middleware.WhiteNoiseMiddleware',
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
    "django.middleware.security.SecurityMiddleware",
    "wagtail.contrib.redirects.middleware.RedirectMiddleware",

]

X_FRAME_OPTIONS = "SAMEORIGIN"

ROOT_URLCONF = "core.urls"

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [os.path.join(PROJECT_DIR, "templates")],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
                "wagtail.contrib.settings.context_processors.settings",
            ]
        },
    }
]

WSGI_APPLICATION = "core.wsgi.application"


# Database
# https://docs.djangoproject.com/en/2.1/ref/settings/#databases
DATABASE_URL = os.getenv("DATABASE_URL")

if DATABASE_URL:
    DATABASES = {"default": dj_database_url.parse(DATABASE_URL)}
else:
    DATABASES = {
        "default": {

                    'ENGINE': 'django.db.backends.postgresql_psycopg2',
                    'NAME': config('DB_NAME'),
                    'HOST': config('DB_HOST'),
                    'USER': config('DB_USER'),
                    'PASSWORD': config('DB_PASSWORD'),
                    'PORT': '5432',
        }
    }

DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"

WAGTAILSEARCH_BACKENDS = {
    "default": {
        "BACKEND": "wagtail.search.backends.database",
    }
}

# Password validation
# https://docs.djangoproject.com/en/2.1/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        "NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator"
    },
    {"NAME": "django.contrib.auth.password_validation.MinimumLengthValidator"},
    {"NAME": "django.contrib.auth.password_validation.CommonPasswordValidator"},
    {"NAME": "django.contrib.auth.password_validation.NumericPasswordValidator"},
]

LOGIN_REDIRECT_URL = "/"

# Internationalization
# https://docs.djangoproject.com/en/2.1/topics/i18n/

LANGUAGE_CODE = "en-us"

TIME_ZONE = "UTC"

USE_I18N = True

USE_L10N = True

USE_TZ = True

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/2.1/howto/static-files/

STATICFILES_FINDERS = [
    "django.contrib.staticfiles.finders.FileSystemFinder",
    "django.contrib.staticfiles.finders.AppDirectoriesFinder",
]

# STATICFILES_DIRS = [
#  os.path.join(BASE_DIR, 'static'),
#   os.path.join(BASE_DIR, 'media')
# ]
# ManifestStaticFilesStorage is recommended in production, to prevent outdated
# Javascript / CSS assets being served from cache (e.g. after a Wagtail upgrade).
# See https://docs.djangoproject.com/en/2.1/ref/contrib/staticfiles/#manifeststaticfilesstorage
# STATICFILES_STORAGE = "django.contrib.staticfiles.storage.ManifestStaticFilesStorage"

STATIC_ROOT = os.path.join(BASE_DIR, "staticfiles")
STATIC_URL = "/static/"
# STATIC_URL = 'http://spotlight-club-bucket.s3-website.ap-south-1.amazonaws.com' + '/static/'
STATICFILES_STORAGE = "whitenoise.storage.CompressedManifestStaticFilesStorage"
# STATICFILES_STORAGE = "django.contrib.staticfiles.storage.CachedStaticFilesStorage"
MEDIA_ROOT = os.path.join(BASE_DIR, "mediafiles")
MEDIA_URL = "/media/"
# MEDIA_URL = 'http://spotlight-club.s3-website.ap-south-1.amazonaws.com' + '/media/'
from .cdn.conf import * #noqa
# Wagtail settings
WAGTAIL_USER_CUSTOM_FIELDS = ['first_name', 'last_name']

WAGTAIL_SITE_NAME = "Spotlight Kenya"



# Base URL to use when referring to full URLs within the Wagtail admin backend -
# e.g. in notification emails. Don't include '/admin' or a trailing slash
# BASE_URL = "http://example.com"
WAGTAILADMIN_BASE_URL = 'http://spotlightkenya.club/'
EMAIL_BACKEND = "django.core.mail.backends.console.EmailBackend"
# DJANGO_SETTINGS_MODULE=core.settings.dev
# WAGTAIL_FRONTEND_LOGIN_TEMPLATE = 'accounts/templates/registration/login.html'
WAGTAIL_FRONTEND_LOGIN_URL = '/accounts/login/'
# COLLECTFAST_STRATEGY = "collectfast.strategies.filesystem.FileSystemStrategy"
# COLLECTFAST_ENABLED = False

EMAIL_USE_TLS = True
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_HOST_USER = 'spotlightkenya7@gmail.com'
EMAIL_HOST_PASSWORD = config('EMAIL_PASSWORD')
EMAIL_PORT = '587'
EMAIL_USER_TLS = True
EMAIL_USER_SSL = True
DEFAULT_FROM_EMAIL = 'www@spotlightkenya.club'
EMAIL_TO = 'spotlightkenya7@gmail.com'
