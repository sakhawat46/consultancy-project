import os
from pathlib import Path

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve(strict=True).parent.parent

TEMPLATES_DIR = os.path.join(BASE_DIR,'templates')
STATIC_DIR = os.path.join(BASE_DIR,'static')
MEDIA_DIR = os.path.join(BASE_DIR, 'media')

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '3_bgv0ser4bh=0#jy&ygs3bftdei#ojaq7l4jc*47z4#xc4=!c'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'bgd_consultancy_app',
    'crispy_forms',
    'widget_tweaks',
    'ckeditor',
    'login_app',
    'payment_app',
]

CRISPY_TEMPLATE_PACK = 'bootstrap4'

#custom user model
AUTH_USER_MODEL = 'login_app.User'

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'bgd_consultancy.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [TEMPLATES_DIR,],
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

WSGI_APPLICATION = 'bgd_consultancy.wsgi.application'


# Database
# https://docs.djangoproject.com/en/3.1/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}


# Password validation
# https://docs.djangoproject.com/en/3.1/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/3.1/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'Asia/Dhaka'

USE_I18N = True

USE_L10N = True

USE_TZ = True



# Default primary key field type
# https://docs.djangoproject.com/en/3.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'



# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.1/howto/static-files/

STATIC_URL = '/static/'

STATICFILES_DIRS = [
    STATIC_DIR,

]

STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')

#media
MEDIA_ROOT = MEDIA_DIR
MEDIA_URL = '/media/'


# LOGIN_URL = '/account/login/'


# Stripe Settings

STRIPE_PUBLIC_KEY = 'pk_test_51N3cKsKr6TSZKaUe8mat0fIe5BjOBSJlhPOWeu8MTDME7ZzFpb3M03gEFhH114KMA9ykvByUIbeBCZKHsIsbjQwT00RJJota0N'
STRIPE_PUBLISHABLE_KEY = 'pk_test_51N3cKsKr6TSZKaUe8mat0fIe5BjOBSJlhPOWeu8MTDME7ZzFpb3M03gEFhH114KMA9ykvByUIbeBCZKHsIsbjQwT00RJJota0N'
STRIPE_SECRET_KEY = 'sk_test_51N3cKsKr6TSZKaUetj41MEHx5tpvwUGRjTpZKSI3AZZ08UQUQ5NhceIKtoe7zecJTkkRm6cPQt13l0VVpRUenRwW00EnkQl8eD'


# STRIPE_PUBLIC_KEY = os.environ.get('STRIPE_TEST_PUBLIC')
# STRIPE_SECRET_KEY = os.environ.get('STRIPE_TEST_SECRET')