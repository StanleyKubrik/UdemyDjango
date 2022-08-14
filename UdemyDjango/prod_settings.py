import os
from pathlib import Path

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-d0wneb86dif+ee4k32&d7gu^3p_jw-g&y^r#2ifu9kc!31^&#c'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False

ALLOWED_HOSTS = ['127.0.0.1']

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'test',
        'USER': 'sng',
        'PASSWORD': '123456',
        'HOST': 'localhost',
        'PORT': '5432'
    }
}

STATICFILES_DIRS = [
    BASE_DIR / 'UdemyDjango/static/'
]

STATIC_ROOT = os.path.join(BASE_DIR, 'static')
