"""
Django settings for settings project.

Generated by 'django-admin startproject' using Django 3.2.7.

For more information on this file, see
https://docs.djangoproject.com/en/3.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/3.2/ref/settings/
"""
import os
import dotenv
import django_heroku
from pathlib import Path

# Build paths inside the project like this: BASE_DIR / "subdir".
BASE_DIR = Path(__file__).resolve().parent.parent
dotenv.read_dotenv(os.path.join(BASE_DIR, ".env"))
DATA_DIR = os.path.dirname(os.path.dirname(__file__))

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = "django-insecure-*i%4&r-if=7j73!4u*h9!ec(=01-*4&o1l@zjefrm!aw$d+-h7"

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['*']


# Application definition

INSTALLED_APPS = [
    # Admin
    "admin_interface",
    "colorfield",
    "ckeditor",

    # Dajngo
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    "django.contrib.sites",

    # Django helpers
    "django_filters",

    # Rest Framework
    "rest_framework",
    "rest_framework.authtoken",

    # Rest Auth / All Auth
    "rest_auth",
    "allauth",
    "allauth.account",
    "rest_auth.registration",

    # Aplications
    "about_us.apps.AboutUsConfig",
    "accounts.apps.AccountsConfig",
    "catalogs.apps.CatalogsConfig",
    "managements.apps.ManagementsConfig",
    "posts.apps.PostsConfig",
    "products.apps.ProductsConfig",
]

MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
]

ROOT_URLCONF = "settings.urls"

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
                "django.template.context_processors.request",
            ],
        },
    },
]

WSGI_APPLICATION = "settings.wsgi.application"

AUTH_USER_MODEL = "accounts.User"

# Database
# https://docs.djangoproject.com/en/3.2/ref/settings/#databases

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.postgresql",
        "NAME": os.environ.get("DATABASE_NAME", "e-commerce-prd"),
        "USER": os.environ.get("DATABASE_USER", "postgres"),
        "PASSWORD": os.environ.get("DATABASE_PASSWORD", "postgres"),
        "HOST": os.environ.get("DATABASE_HOST", "localhost"),
        "PORT": os.environ.get("DATABASE_PORT", "5432"),
    }
}


# Password validation
# https://docs.djangoproject.com/en/3.2/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        "NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.MinimumLengthValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.CommonPasswordValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.NumericPasswordValidator",
    },
]

# Internationalization
# https://docs.djangoproject.com/en/3.2/topics/i18n/

LANGUAGE_CODE = "en-us"

TIME_ZONE = "UTC"

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.2/howto/static-files/

MEDIA_URL = "/media/"
MEDIA_ROOT = os.path.join(DATA_DIR, "media")

STATIC_URL = "/static/"
STATIC_ROOT = os.path.join(DATA_DIR, "static")

# Default primary key field type
# https://docs.djangoproject.com/en/3.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"

# Variables
SITE_ID = 1

# to use old_password when setting a new password
OLD_PASSWORD_FIELD_ENABLED = True
# to keep the user logged in after password change
LOGOUT_ON_PASSWORD_CHANGE = False

# Auth
ACCOUNT_AUTHENTICATION_METHOD = "email"
ACCOUNT_EMAIL_REQUIRED = True
ACCOUNT_UNIQUE_EMAIL = True
ACCOUNT_USER_MODEL_USERNAME_FIELD = None
ACCOUNT_USERNAME_REQUIRED = False
ACCOUNT_LOGOUT_ON_GET = True

# UNSURE
ACCOUNT_EMAIL_VERIFICATION = "none"
ACCOUNT_LOGIN_ATTEMPTS_LIMIT = 5
ACCOUNT_LOGIN_ATTEMPTS_TIMEOUT = 86400  # 1 day in seconds
ACCOUNT_LOGOUT_REDIRECT_URL = "/api/login/"
LOGIN_REDIRECT_URL = "/user/"
SOCIALACCOUNT_EMAIL_VERIFICATION = "none"

AUTHENTICATION_BACKENDS = (
    "django.contrib.auth.backends.ModelBackend",
    "allauth.account.auth_backends.AuthenticationBackend"
)

REST_AUTH_SERIALIZERS = {
    "LOGIN_SERIALIZER": "accounts.api.serializers.CustomLoginSerializer",
    "DEFAULT_FROM_EMAIL": "eduardo.monita.dias@gmail.com"
}
REST_AUTH_REGISTER_SERIALIZERS = {
    "REGISTER_SERIALIZER": "accounts.api.serializers.CustomRegistrationSerializer"
}

# Email
EMAIL_BACKEND = "django.core.mail.backends.console.EmailBackend"
# EMAIL_USE_TLS = True
# EMAIL_HOST = "smtp.gmail.com"
# EMAIL_PORT = 587
# EMAIL_HOST_USER = "youremail@gmail.com"
# EMAIL_HOST_PASSWORD = "yourpassword"
# DEFAULT_FROM_EMAIL = "youremail@gmail.com"
# DEFAULT_TO_EMAIL = EMAIL_HOST_USER

# Django Admin Interface
X_FRAME_OPTIONS = "SAMEORIGIN"
SILENCED_SYSTEM_CHECKS = ["security.W019"]

# Rest Framework
# REST_FRAMEWORK = {
# }

# Log
LOGGING = {
    "version": 1,
    "disable_existing_loggers": False,
    "root": {
        "level": "INFO",
        "handlers": ["console"],
    },
    "formatters": {
        "verbose": {
            "format": "%(levelname)s %(asctime)s %(module)s "
                      "%(process)d %(thread)d %(message)s"
        },
    },
    "handlers": {
        "console": {
            "level": "DEBUG",
            "class": "logging.StreamHandler",
            "formatter": "verbose"
        }
    },
    "loggers": {
        "django.db.backends": {
            "level": "ERROR",
            "handlers": ["console"],
            "propagate": False,
        },
        "django.security.DisallowedHost": {
            "level": "ERROR",
            "handlers": ["console", ],
            "propagate": False,
        },
        "about_us": {
            "level": "DEBUG",
            "handlers": ["console", ],
            "propagate": False,
        },
        "accounts": {
            "level": "DEBUG",
            "handlers": ["console", ],
            "propagate": False,
        },
        "catalogs": {
            "level": "DEBUG",
            "handlers": ["console", ],
            "propagate": False,
        },
        "managements": {
            "level": "DEBUG",
            "handlers": ["console", ],
            "propagate": False,
        },
        "posts": {
            "level": "DEBUG",
            "handlers": ["console", ],
            "propagate": False,
        },
        "products": {
            "level": "DEBUG",
            "handlers": ["console", ],
            "propagate": False,
        },
    },
}

CKEDITOR_UPLOAD_PATH = "ckeditor/"

django_heroku.settings(locals())
