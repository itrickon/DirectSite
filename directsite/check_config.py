#!/usr/bin/env python
"""Скрипт для проверки конфигурации Django перед запуском на хостинге"""
import os
import sys

print("=" * 50)
print("ПРОВЕРКА КОНФИГУРАЦИИ DJANGO")
print("=" * 50)

# Проверка пути
print(f"\n1. Текущий путь: {os.getcwd()}")
print(f"   Python: {sys.executable}")
print(f"   Версия Python: {sys.version}")

# Проверка Django
try:
    import django
    print(f"\n2. Django установлен: {django.VERSION}")
except ImportError as e:
    print(f"\n2. ❌ Django НЕ установлен: {e}")

# Проверка settings.py
try:
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'directsite.settings')
    import django
    django.setup()
    print("\n3. ✅ settings.py загружен успешно")
except Exception as e:
    print(f"\n3. ❌ Ошибка загрузки settings.py: {e}")

# Проверка базы данных
try:
    from django.conf import settings
    print(f"\n4. DATABASES: {settings.DATABASES['default']['ENGINE']}")
    print(f"   Путь к БД: {settings.DATABASES['default'].get('NAME', 'N/A')}")
except Exception as e:
    print(f"\n4. ❌ Ошибка проверки БД: {e}")

# Проверка STATIC
try:
    print(f"\n5. STATIC_URL: {settings.STATIC_URL}")
    print(f"   STATIC_ROOT: {settings.STATIC_ROOT}")
except Exception as e:
    print(f"\n5. ❌ Ошибка проверки статики: {e}")

# Проверка ALLOWED_HOSTS
try:
    print(f"\n6. ALLOWED_HOSTS: {settings.ALLOWED_HOSTS}")
    print(f"   DEBUG: {settings.DEBUG}")
except Exception as e:
    print(f"\n6. ❌ Ошибка проверки ALLOWED_HOSTS: {e}")

print("\n" + "=" * 50)
print("ПРОВЕРКА ЗАВЕРШЕНА")
print("=" * 50)
