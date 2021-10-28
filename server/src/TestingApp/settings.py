import os
from dotenv import dotenv_values
from distutils import util

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

config = dotenv_values('../.env')

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = str(config["SECRET_KEY"])

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = bool(util.strtobool(config["DEBUG"]))


ALLOWED_HOSTS = [
    '127.0.0.1', 'localhost', 'testserver'
]

CORS_ALLOWED_ORIGINS = [
    "http://localhost:3000",
    "http://127.0.0.1:3000",
    "http://localhost:8000",
    "http://127.0.0.1:8000",
]

CORS_ALLOW_METHODS = [
    "DELETE",
    "GET",
    "OPTIONS",
    "PATCH",
    "POST",
    "PUT",
]

CORS_ALLOW_HEADERS = [
    "accept",
    "accept-encoding",
    "authorization",
    "content-type",
    "dnt",
    "origin",
    "user-agent",
    "x-csrftoken",
    "x-requested-with",
]

CORS_PREFLIGHT_MAX_AGE = 86400

CORS_ALLOW_CREDENTIALS = True


INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    # customs
    'app',
    'app_orders',
    'app_ems',

    # third-party
    "corsheaders",
    'debug_toolbar',
    'rest_framework',
    'livereload',
]

MIDDLEWARE = [
    'debug_toolbar.middleware.DebugToolbarMiddleware',
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'corsheaders.middleware.CorsMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'livereload.middleware.LiveReloadScript',
]

ROOT_URLCONF = 'TestingApp.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [
            os.path.join(BASE_DIR, 'templates')
        ],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                # defaults
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',

                # customs
                'TestingApp.context_processors.globals'
            ],
            'libraries':{
                'globals': 'TestingApp.templatetags.globals',
            }
        },
    },
]

WSGI_APPLICATION = 'TestingApp.wsgi.application'


# Database
# https://docs.djangoproject.com/en/3.0/ref/settings/#databases

DATABASES = {
    'default': {
        # SQLite Settings
        # 'ENGINE': 'django.db.backends.sqlite3',
        # 'NAME': os.path.join('{}/db/'.format(BASE_DIR), 'TestingApp.sqlite3'),

        # MySQL Settings
        'ENGINE': 'django.db.backends.mysql',
        'NAME': config["DB_NAME"],
        'USER': config["DB_USER"],
        'PASSWORD': config["DB_PASSWORD"],
        'PORT': config["DB_PORT"],
    }
}


# Password validation
# https://docs.djangoproject.com/en/3.0/ref/settings/#auth-password-validators

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


LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'handlers': {
        'console': {
            'class': 'logging.StreamHandler',
        },
    },
    'root': {
        'handlers': ['console'],
        'level': 'WARNING',
    },
}


# Internationalization
# https://docs.djangoproject.com/en/3.0/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.0/howto/static-files/

STATIC_URL = '/static/'
STATICFILES_DIRS = [
    "static",
]

INTERNAL_IPS = [
    '127.0.0.1',
    'localhost'
]

DEBUG_TOOLBAR_CONFIG = {
}

REST_FRAMEWORK = {
    # Use Django's standard `django.contrib.auth` permissions,
    # or allow read-only access for unauthenticated users.
    'DEFAULT_PERMISSION_CLASSES': [
        'rest_framework.permissions.IsAuthenticated'
    ]
}

# Constants
PAGE_SIZE = int(config["PAGE_SIZE"])
PROTOCOL = config["PROTOCOL"]
APP_NAME = 'TestingApp'
