import os
from pathlib import Path

from dotenv import load_dotenv
from split_settings.tools import include

load_dotenv()

include(
    'components/database.py',
    'components/templates.py',
    'components/installed_apps.py',
    'components/middleware.py',
    'components/internationalization.py',
    'components/celery_settings.py',
)


# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = os.environ.get('SECRET_KEY')

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = os.environ.get('DEBUG', False) == 'True'

ALLOWED_HOSTS = [
    '127.0.0.1',
    'localhost',
    '0.0.0.0',
]

CSRF_TRUSTED_ORIGINS = [
    'https://*0.0.0.0:8001', 'http://*0.0.0.0:8001', 'https://*127.0.0.1:8001', 'http://*127.0.0.1:8001'
]

ROOT_URLCONF = 'config.urls'

WSGI_APPLICATION = 'config.wsgi.application'

# AUTH_USER_MODEL = "users.User"

AUTHENTICATION_BACKENDS = [
    # 'users.auth.CustomBackend',
    'django.contrib.auth.backends.ModelBackend',
]

AUTH_ADMIN_LOGIN_URL = os.environ.get('AUTH_ADMIN_LOGIN_URL', default='http://localhost:8000/api/v1/auth/login_admin')

# Password validation
# https://docs.djangoproject.com/en/4.2/ref/settings/#auth-password-validators

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

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.2/howto/static-files/

# STATIC_URL = 'static/'
STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'static')

# STATIC_URL = '/backend_static/'
# STATIC_ROOT = os.path.join(BASE_DIR, 'backend_static')

# Default primary key field type
# https://docs.djangoproject.com/en/4.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'


# For debug
# INTERNAL_IPS = [
#     "127.0.0.1",
#     "localhost",
# ]
