"""
Django settings for DirectSite project.
Universal configuration for any hosting provider.

Supported hosting:
- PythonAnywhere
- Timeweb
- Beget
- VPS (Ubuntu/CentOS)
- Docker
- Render, Railway, Heroku
- Local development
"""

from pathlib import Path
import os

# Import universal configuration
from config import (
    get_bool_env,
    get_list_env,
    detect_hosting,
    get_database_config,
    get_allowed_hosts,
    get_static_root,
    get_project_path,
)

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

# ============================================================
# AUTO-DETECT HOSTING TYPE
# ============================================================
HOSTING_TYPE = detect_hosting()

# ============================================================
# CORE SETTINGS
# ============================================================

# Security settings from environment
SECRET_KEY = os.environ.get('SECRET_KEY', 'django-insecure-change-this-in-production')
DEBUG = get_bool_env('DEBUG', False)

# Allowed hosts from environment or defaults
ALLOWED_HOSTS = get_allowed_hosts(HOSTING_TYPE)

# ============================================================
# DATABASE CONFIGURATION
# ============================================================
DATABASES = get_database_config(BASE_DIR, HOSTING_TYPE)

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

ROOT_URLCONF = 'directsite.urls'

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

LANGUAGE_CODE = 'ru-ru'  # Russian language
TIME_ZONE = 'Europe/Moscow'  # Moscow timezone
USE_I18N = True
USE_TZ = True

# ============================================================
# STATIC FILES
# ============================================================

STATIC_URL = os.environ.get('STATIC_URL', '/static/')
STATIC_ROOT = get_static_root(BASE_DIR, HOSTING_TYPE)
STATICFILES_DIRS = [BASE_DIR / 'static']

# ============================================================
# DEFAULT PRIMARY KEY FIELD TYPE
# ============================================================

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

# ============================================================
# SECURITY SETTINGS (PRODUCTION)
# ============================================================

if not DEBUG:
    # Security headers
    SECURE_SSL_REDIRECT = get_bool_env('SECURE_SSL_REDIRECT', True)
    SESSION_COOKIE_SECURE = get_bool_env('SESSION_COOKIE_SECURE', True)
    CSRF_COOKIE_SECURE = get_bool_env('CSRF_COOKIE_SECURE', True)
    SECURE_BROWSER_XSS_FILTER = True
    SECURE_CONTENT_TYPE_NOSNIFF = True
    X_FRAME_OPTIONS = 'DENY'
    SECURE_HSTS_SECONDS = get_bool_env('SECURE_HSTS_SECONDS', 31536000)
    SECURE_HSTS_INCLUDE_SUBDOMAINS = get_bool_env('SECURE_HSTS_INCLUDE_SUBDOMAINS', True)
    SECURE_HSTS_PRELOAD = get_bool_env('SECURE_HSTS_PRELOAD', True)

# CSRF trusted origins
CSRF_TRUSTED_ORIGINS = [
    'http://localhost:8000',
    'http://127.0.0.1:8000',
    'https://tricko66.pythonanywhere.com',
    'https://direct-line-sar.ru',
    'https://www.direct-line-sar.ru',
]

# Add from environment
csrf_origins = get_list_env('CSRF_TRUSTED_ORIGINS')
if csrf_origins:
    CSRF_TRUSTED_ORIGINS.extend(csrf_origins)

# ============================================================
# LOGGING
# ============================================================

LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'formatters': {
        'verbose': {
            'format': '{levelname} {asctime} {module} {message}',
            'style': '{',
        },
        'simple': {
            'format': '{levelname} {message}',
            'style': '{',
        },
    },
    'handlers': {
        'file': {
            'level': 'INFO',
            'class': 'logging.FileHandler',
            'filename': BASE_DIR / 'logs' / 'django.log',
            'formatter': 'verbose',
        },
        'console': {
            'level': 'DEBUG' if DEBUG else 'INFO',
            'class': 'logging.StreamHandler',
            'formatter': 'simple',
        },
    },
    'loggers': {
        'django': {
            'handlers': ['file', 'console'],
            'level': 'INFO',
            'propagate': True,
        },
        'core': {
            'handlers': ['file', 'console'],
            'level': 'INFO',
            'propagate': False,
        },
    },
}

# ============================================================
# TELEGRAM CONFIGURATION
# ============================================================

TELEGRAM_BOT_TOKEN = os.environ.get('TELEGRAM_BOT_TOKEN', '')
TELEGRAM_CHAT_ID = os.environ.get('TELEGRAM_CHAT_ID', '')
TELEGRAM_PROXY = os.environ.get('TELEGRAM_PROXY', '')

# ============================================================
# EMAIL CONFIGURATION
# ============================================================

EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = os.environ.get('EMAIL_HOST', 'smtp.gmail.com')
EMAIL_PORT = int(os.environ.get('EMAIL_PORT', 587))
EMAIL_USE_TLS = get_bool_env('EMAIL_USE_TLS', True)
EMAIL_HOST_USER = os.environ.get('EMAIL_HOST_USER', '')
EMAIL_HOST_PASSWORD = os.environ.get('EMAIL_HOST_PASSWORD', '')
DEFAULT_FROM_EMAIL = os.environ.get('DEFAULT_FROM_EMAIL', 'DirectLine <noreply@direct-line-sar.ru>')
ADMIN_EMAIL = os.environ.get('ADMIN_EMAIL', 'directlines@atomicmail.io')

# ============================================================
# HOSTING-SPECIFIC SETTINGS
# ============================================================

# PythonAnywhere specific
if HOSTING_TYPE == 'pythonanywhere':
    # PythonAnywhere has specific requirements
    pass

# Timeweb specific
elif HOSTING_TYPE == 'timeweb':
    # Timeweb uses Passenger
    pass

# VPS/Docker specific
elif HOSTING_TYPE in ('vps', 'docker'):
    # Can use Gunicorn, Nginx, etc.
    pass

# ============================================================
# DEBUG TOOLBAR (DEVELOPMENT ONLY)
# ============================================================

if DEBUG:
    # Enable debug toolbar in development
    INSTALLED_APPS.append('debug_toolbar')
    MIDDLEWARE.append('debug_toolbar.middleware.DebugToolbarMiddleware')
    INTERNAL_IPS = ['127.0.0.1', 'localhost']

# ============================================================
# PRINT CONFIGURATION INFO (DEBUG MODE)
# ============================================================

if DEBUG:
    print(f"\n{'='*60}")
    print(f"DJANGO CONFIGURATION (DEBUG MODE)")
    print(f"{'='*60}")
    print(f"Hosting Type: {HOSTING_TYPE}")
    print(f"BASE_DIR: {BASE_DIR}")
    print(f"DEBUG: {DEBUG}")
    print(f"ALLOWED_HOSTS: {ALLOWED_HOSTS}")
    print(f"DATABASE: {DATABASES['default']['ENGINE']}")
    print(f"STATIC_ROOT: {STATIC_ROOT}")
    print(f"TELEGRAM_BOT_TOKEN: {'***' if TELEGRAM_BOT_TOKEN else 'Not set'}")
    print(f"EMAIL_HOST_USER: {EMAIL_HOST_USER or 'Not set'}")
    print(f"{'='*60}\n")
