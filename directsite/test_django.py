#!/usr/bin/env python3
"""
Тестовый скрипт для проверки настроек Django
"""
import os
import sys
import traceback

BASE_DIR = '/home/i/itrickon/itrickon.beget.tech/public_html'
PROJECT_DIR = os.path.join(BASE_DIR, 'directsite')

# Добавляем пути
for path in [BASE_DIR, PROJECT_DIR]:
    if path not in sys.path:
        sys.path.insert(0, path)

print("=" * 60)
print("DJANGO CONFIGURATION TEST")
print("=" * 60)

# Проверяем sys.path
print(f"\nsys.path:")
for p in sys.path[:5]:
    print(f"  - {p}")

# Проверяем переменные окружения
print(f"\nEnvironment variables:")
print(f"  DJANGO_SETTINGS_MODULE: {os.environ.get('DJANGO_SETTINGS_MODULE', 'NOT SET')}")
print(f"  PROJECT_ROOT: {os.environ.get('PROJECT_ROOT', 'NOT SET')}")
print(f"  PUBLIC_HTML_DIR: {os.environ.get('PUBLIC_HTML_DIR', 'NOT SET')}")

# Устанавливаем переменные
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'directsite.settings')

# Проверяем наличие config.py
print(f"\nChecking config.py:")
config_path = os.path.join(BASE_DIR, 'config.py')
print(f"  config.py exists: {os.path.exists(config_path)}")

# Проверяем наличие settings.py
print(f"\nChecking settings.py:")
settings_path = os.path.join(PROJECT_DIR, 'settings.py')
print(f"  settings.py exists: {os.path.exists(settings_path)}")

# Пытаемся импортировать Django
print(f"\nImporting Django...")
try:
    import django
    print(f"  Django version: {django.VERSION}")
except ImportError as e:
    print(f"  ERROR: {e}")
    print("  Install Django: pip3 install --user Django")

# Пытаемся загрузить настройки
print(f"\nLoading Django settings...")
try:
    from django.conf import settings
    print(f"  Settings loaded successfully")
    print(f"  DEBUG: {settings.DEBUG}")
    print(f"  ALLOWED_HOSTS: {settings.ALLOWED_HOSTS}")
    print(f"  BASE_DIR: {settings.BASE_DIR}")
except Exception as e:
    print(f"  ERROR: {e}")
    traceback.print_exc()

# Пытаемся импортировать WSGI
print(f"\nLoading WSGI application...")
try:
    from django.core.wsgi import get_wsgi_application
    application = get_wsgi_application()
    print(f"  WSGI application created successfully")
except Exception as e:
    print(f"  ERROR: {e}")
    traceback.print_exc()

print("\n" + "=" * 60)
print("TEST COMPLETE")
print("=" * 60)
