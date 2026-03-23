"""
Django settings for DirectSite project.
Настройки для PythonAnywhere
"""

from pathlib import Path
import os

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

# ============================================================
# CORE SETTINGS
# ============================================================

SECRET_KEY = os.environ.get('SECRET_KEY', 'django-insecure-v3&o7+pphz)9b4k8d3f@tkm(*h1tu(e6b#k82z_6q570c**%!9')
DEBUG = os.environ.get('DEBUG', 'False').lower() == 'true'

ALLOWED_HOSTS = [
    'tricko66.pythonanywhere.com',
    'localhost',
    '127.0.0.1',
]

# ============================================================
# DATABASE CONFIGURATION (SQLite)
# ============================================================

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

# ============================================================
# APPLICATION DEFINITION
# ============================================================

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'core',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

# Security middleware for production
if not DEBUG:
    MIDDLEWARE.insert(0, 'django.middleware.security.SecurityMiddleware')

# ============================================================
# ROOT URL CONF - ОБЯЗАТЕЛЬНО!
# ============================================================

ROOT_URLCONF = 'directsite.urls'

# ============================================================
# TEMPLATES
# ============================================================

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / 'templates'],
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

# ============================================================
# WSGI APPLICATION
# ============================================================

WSGI_APPLICATION = 'directsite.wsgi.application'

# ============================================================
# AUTHENTICATION
# ============================================================

AUTH_PASSWORD_VALIDATORS = [
    {'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator'},
    {'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator'},
    {'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator'},
    {'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator'},
]

# ============================================================
# INTERNATIONALIZATION
# ============================================================

LANGUAGE_CODE = 'ru-ru'
TIME_ZONE = 'Europe/Moscow'
USE_I18N = True
USE_TZ = True

# ============================================================
# STATIC FILES
# ============================================================

STATIC_URL = '/static/'
STATIC_ROOT = BASE_DIR / 'staticfiles'
STATICFILES_DIRS = [BASE_DIR / 'static']

# ============================================================
# DEFAULT PRIMARY KEY FIELD TYPE
# ============================================================

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

# ============================================================
# SECURITY SETTINGS (PRODUCTION)
# ============================================================

if not DEBUG:
    SECURE_SSL_REDIRECT = True
    SESSION_COOKIE_SECURE = True
    CSRF_COOKIE_SECURE = True
    SECURE_BROWSER_XSS_FILTER = True
    SECURE_CONTENT_TYPE_NOSNIFF = True
    X_FRAME_OPTIONS = 'DENY'
    SECURE_HSTS_SECONDS = 31536000
    SECURE_HSTS_INCLUDE_SUBDOMAINS = True
    SECURE_HSTS_PRELOAD = True

# CSRF trusted origins
CSRF_TRUSTED_ORIGINS = [
    'http://localhost:8000',
    'http://127.0.0.1:8000',
    'https://tricko66.pythonanywhere.com',
    'https://direct-line-sar.ru',
    'https://www.direct-line-sar.ru',
]

# ============================================================
# LOGGING - ОТКЛЮЧЕНО ДЛЯ PYTHONANYWHERE
# ============================================================

LOGGING = {}

# ============================================================
# TELEGRAM CONFIGURATION
# ============================================================

TELEGRAM_BOT_TOKEN = os.environ.get('TELEGRAM_BOT_TOKEN', '')
TELEGRAM_CHAT_ID = os.environ.get('TELEGRAM_CHAT_ID', '')

# ============================================================
# EMAIL CONFIGURATION
# ============================================================

EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = os.environ.get('EMAIL_HOST', 'smtp.gmail.com')
EMAIL_PORT = int(os.environ.get('EMAIL_PORT', 587))
EMAIL_USE_TLS = True
EMAIL_HOST_USER = os.environ.get('EMAIL_HOST_USER', '')
EMAIL_HOST_PASSWORD = os.environ.get('EMAIL_HOST_PASSWORD', '')
DEFAULT_FROM_EMAIL = os.environ.get('DEFAULT_FROM_EMAIL', 'DirectLine <noreply@direct-line-sar.ru>')
ADMIN_EMAIL = os.environ.get('ADMIN_EMAIL', 'directlines@atomicmail.io')

# ============================================================
# PRINT CONFIGURATION (DEBUG)
# ============================================================

if DEBUG:
    print(f"\n{'='*60}")
    print(f"DJANGO CONFIGURATION (DEBUG MODE)")
    print(f"{'='*60}")
    print(f"BASE_DIR: {BASE_DIR}")
    print(f"DEBUG: {DEBUG}")
    print(f"ALLOWED_HOSTS: {ALLOWED_HOSTS}")
    print(f"DATABASE: {DATABASES['default']['ENGINE']}")
    print(f"{'='*60}\n")
