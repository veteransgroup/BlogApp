"""
Django settings for blogproject project.

Generated by 'django-admin startproject' using Django 2.2.3.

For more information on this file, see
https://docs.djangoproject.com/en/2.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/2.2/ref/settings/
"""

import os

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
back = os.path.dirname

BASE_DIR = back(back(back(os.path.abspath(__file__))))

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/2.2/howto/deployment/checklist/

# Application definition

INSTALLED_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    "pure_pagination",  # 分页
    "haystack",  # 搜索
    "blog.apps.BlogConfig",  # 注册 blog 应用
    "comments.apps.CommentsConfig",  # 注册 comments 应用
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

ROOT_URLCONF = "blogproject.urls"

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [os.path.join(BASE_DIR, "templates")],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
            ],
        },
    },
]

WSGI_APPLICATION = "blogproject.wsgi.application"

# Database
# https://docs.djangoproject.com/en/2.2/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': os.environ.get('DJANGO_DB_NAME', 'postgres'),
        'USER': os.environ.get('DJANGO_DB_USER', 'postgres'),
        'PASSWORD': os.environ.get('DJANGO_DB_PASSWORD', 'postgres'),
        'HOST': os.environ.get('DJANGO_DB_HOST', 'db'),
        'PORT': os.environ.get('DJANGO_DB_PORT', '5432'),
    }
}

# Password validation
# https://docs.djangoproject.com/en/2.2/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        "NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator",
    },
    {"NAME": "django.contrib.auth.password_validation.MinimumLengthValidator",},
    {"NAME": "django.contrib.auth.password_validation.CommonPasswordValidator",},
    {"NAME": "django.contrib.auth.password_validation.NumericPasswordValidator",},
]

# Internationalization
# https://docs.djangoproject.com/en/2.2/topics/i18n/

LANGUAGE_CODE = "en-us"

TIME_ZONE = "Pacific/Auckland"

USE_I18N = True

USE_L10N = True

USE_TZ = True

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/2.2/howto/static-files/

STATIC_URL = "/static/"
STATIC_ROOT = os.path.join(BASE_DIR, "static")

# 分页设置
PAGINATION_SETTINGS = {
    "PAGE_RANGE_DISPLAYED": 4,
    "MARGIN_PAGES_DISPLAYED": 2,
    "SHOW_FIRST_PAGE_WHEN_INVALID": True,
}

# 搜索设置
HAYSTACK_CONNECTIONS = {
    "default": {
        "ENGINE": "blog.elasticsearch2_ik_backend.Elasticsearch2IkSearchEngine",
        "URL": "",
        "INDEX_NAME": "blog_app",
    },
}
HAYSTACK_SEARCH_RESULTS_PER_PAGE = 10

enable = os.environ.get("ENABLE_HAYSTACK_REALTIME_SIGNAL_PROCESSOR", "yes")
if enable in {"true", "True", "yes"}:
    HAYSTACK_SIGNAL_PROCESSOR = "haystack.signals.RealtimeSignalProcessor"

HAYSTACK_CUSTOM_HIGHLIGHTER = "blog.utils.Highlighter"
# HAYSTACK_DEFAULT_OPERATOR = 'AND'
# HAYSTACK_FUZZY_MIN_SIM = 0.1
