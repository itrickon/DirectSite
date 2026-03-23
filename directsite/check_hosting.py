#!/usr/bin/env python
"""
Универсальный скрипт проверки конфигурации Django проекта.
Проверяет готовность к развёртыванию на любом хостинге.

Использование:
    python check_hosting.py
"""

import os
import sys
import json
from pathlib import Path

# Colors for output
class Colors:
    GREEN = '\033[92m'
    YELLOW = '\033[93m'
    RED = '\033[91m'
    BLUE = '\033[94m'
    BOLD = '\033[1m'
    END = '\033[0m'


def print_header(text):
    print(f"\n{Colors.BOLD}{Colors.BLUE}{'='*60}{Colors.END}")
    print(f"{Colors.BOLD}{Colors.BLUE}{text:^60}{Colors.END}")
    print(f"{Colors.BOLD}{Colors.BLUE}{'='*60}{Colors.END}\n")


def print_success(text):
    print(f"{Colors.GREEN}✓ {text}{Colors.END}")


def print_warning(text):
    print(f"{Colors.YELLOW}⚠ {text}{Colors.END}")


def print_error(text):
    print(f"{Colors.RED}✗ {text}{Colors.END}")


def print_info(text):
    print(f"{Colors.BLUE}ℹ {text}{Colors.END}")


def check_python():
    """Проверка версии Python"""
    print_header("ПРОВЕРКА PYTHON")
    
    version = sys.version_info
    version_str = f"{version.major}.{version.minor}.{version.micro}"
    print_info(f"Версия Python: {version_str}")
    
    if version.major == 3 and version.minor >= 8:
        print_success(f"Python {version_str} соответствует требованиям (3.8+)")
        return True
    elif version.major == 3 and version.minor >= 4:
        print_warning(f"Python {version_str} устарел, рекомендуется 3.8+")
        return True
    else:
        print_error(f"Python {version_str} не поддерживается. Требуется 3.4+")
        return False


def check_django():
    """Проверка установки Django"""
    print_header("ПРОВЕРКА DJANGO")
    
    try:
        import django
        version = django.get_version()
        print_info(f"Версия Django: {version}")
        
        version_parts = version.split('.')
        major = int(version_parts[0])
        minor = int(version_parts[1]) if len(version_parts) > 1 else 0
        
        if major >= 4:
            print_success(f"Django {version} соответствует требованиям")
            return True
        elif major == 3 and minor >= 2:
            print_warning(f"Django {version} устарел, рекомендуется 4.2+")
            return True
        else:
            print_error(f"Django {version} не поддерживается")
            return False
    except ImportError:
        print_error("Django не установлен")
        print_info("Выполните: pip install -r requirements.txt")
        return False


def check_env_file():
    """Проверка файла .env"""
    print_header("ПРОВЕРКА .ENV")
    
    env_file = Path('.env')
    if not env_file.exists():
        print_error("Файл .env не найден")
        print_info("Скопируйте .env.example в .env и настройте")
        return False
    
    print_success("Файл .env найден")
    
    # Проверка содержимого
    try:
        from dotenv import load_dotenv
        load_dotenv()
        
        checks = {
            'SECRET_KEY': 'Секретный ключ',
            'ALLOWED_HOSTS': 'Разрешённые хосты',
            'TELEGRAM_BOT_TOKEN': 'Telegram токен',
            'TELEGRAM_CHAT_ID': 'Telegram chat ID',
        }
        
        all_ok = True
        for key, name in checks.items():
            value = os.environ.get(key, '')
            if value:
                if key == 'SECRET_KEY' and 'django-insecure' in value:
                    print_warning(f"{name}: используется ключ по умолчанию!")
                else:
                    print_success(f"{name}: настроен")
            else:
                if key in ('SECRET_KEY', 'ALLOWED_HOSTS'):
                    print_error(f"{name}: не настроен!")
                    all_ok = False
                else:
                    print_warning(f"{name}: не настроен (опционально)")
        
        # Проверка DEBUG
        debug = os.environ.get('DEBUG', 'True').lower() == 'true'
        if debug:
            print_warning("DEBUG=True (не рекомендуется для production)")
        else:
            print_success("DEBUG=False (production режим)")
        
        return all_ok
    except ImportError:
        print_warning("python-dotenv не установлен. Проверка переменных ограничена.")
        return True


def check_database():
    """Проверка конфигурации базы данных"""
    print_header("ПРОВЕРКА БАЗЫ ДАННЫХ")
    
    try:
        os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'directsite.settings')
        import django
        django.setup()
        
        from django.conf import settings
        db_config = settings.DATABASES['default']
        engine = db_config.get('ENGINE', '')
        
        print_info(f"База данных: {engine}")
        
        if 'sqlite3' in engine:
            db_name = db_config.get('NAME', 'db.sqlite3')
            print_info(f"SQLite база: {db_name}")
            
            if Path(db_name).exists():
                print_success("Файл базы данных существует")
            else:
                print_warning("Файл базы данных будет создан при миграции")
            
            print_warning("SQLite рекомендуется только для небольших проектов")
        elif 'postgresql' in engine:
            print_success("PostgreSQL настроен (рекомендуется для production)")
        else:
            print_warning(f"Неизвестный тип БД: {engine}")
        
        return True
    except Exception as e:
        print_error(f"Ошибка проверки БД: {e}")
        return False


def check_migrations():
    """Проверка миграций"""
    print_header("ПРОВЕРКА МИГРАЦИЙ")
    
    try:
        os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'directsite.settings')
        import django
        django.setup()
        
        from django.core.management import call_command
        from django.db import connection
        
        # Проверка наличия миграций
        tables = connection.introspection.table_names()
        
        if tables:
            print_success(f"База данных содержит {len(tables)} таблиц")
        else:
            print_warning("База данных пуста. Выполните миграции:")
            print_info("python manage.py migrate")
        
        return True
    except Exception as e:
        print_error(f"Ошибка проверки миграций: {e}")
        return False


def check_static():
    """Проверка статических файлов"""
    print_header("ПРОВЕРКА СТАТИКИ")
    
    try:
        os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'directsite.settings')
        import django
        django.setup()
        
        from django.conf import settings
        
        static_root = settings.STATIC_ROOT
        static_dirs = settings.STATICFILES_DIRS
        
        print_info(f"STATIC_URL: {settings.STATIC_URL}")
        print_info(f"STATIC_ROOT: {static_root}")
        
        if Path(static_root).exists():
            print_success("Папка staticfiles существует")
        else:
            print_warning("Папка staticfiles не существует")
            print_info("Выполните: python manage.py collectstatic")
        
        # Проверка наличия статики в проекте
        for static_dir in static_dirs:
            if Path(static_dir).exists():
                print_success(f"Папка статики найдена: {static_dir}")
            else:
                print_warning(f"Папка статики не найдена: {static_dir}")
        
        return True
    except Exception as e:
        print_error(f"Ошибка проверки статики: {e}")
        return False


def check_templates():
    """Проверка шаблонов"""
    print_header("ПРОВЕРКА ШАБЛОНОВ")
    
    templates_dir = Path('templates')
    if not templates_dir.exists():
        print_error("Папка templates не найдена")
        return False
    
    print_success("Папка templates найдена")
    
    required_templates = [
        'base.html',
        'index.html',
        'service.html',
        'contacts.html',
        'vacancy.html',
    ]
    
    for template in required_templates:
        template_path = templates_dir / template
        if template_path.exists():
            print_success(f"Шаблон {template} найден")
        else:
            print_error(f"Шаблон {template} не найден")
    
    return True


def check_hosting_detection():
    """Проверка авто-определения хостинга"""
    print_header("ПРОВЕРКА ХОСТИНГА")
    
    try:
        from config import detect_hosting
        
        hosting_type = detect_hosting()
        print_info(f"Определён тип хостинга: {hosting_type}")
        
        hosting_info = {
            'pythonanywhere': 'PythonAnywhere',
            'timeweb': 'Timeweb',
            'beget': 'Beget',
            'vps': 'VPS/Dedicated',
            'docker': 'Docker',
            'render': 'Render',
            'railway': 'Railway',
            'shared': 'Shared Hosting',
            'local': 'Local Development',
        }
        
        if hosting_type in hosting_info:
            print_success(f"Хостинг: {hosting_info[hosting_type]}")
        else:
            print_info(f"Тип хостинга: {hosting_type}")
        
        return True
    except Exception as e:
        print_error(f"Ошибка определения хостинга: {e}")
        return False


def check_requirements():
    """Проверка requirements.txt"""
    print_header("ПРОВЕРКА ЗАВИСИМОСТЕЙ")
    
    req_file = Path('requirements.txt')
    if not req_file.exists():
        print_error("Файл requirements.txt не найден")
        return False
    
    print_success("Файл requirements.txt найден")
    
    # Проверка основных пакетов
    with open(req_file, 'r') as f:
        content = f.read().lower()
    
    required_packages = {
        'django': 'Django',
        'requests': 'Requests',
        'python-dotenv': 'python-dotenv',
    }
    
    for pkg, name in required_packages.items():
        if pkg in content:
            print_success(f"{name} указан в requirements.txt")
        else:
            print_warning(f"{name} не указан в requirements.txt")
    
    return True


def print_summary(results):
    """Вывод итогов проверки"""
    print_header("ИТОГИ ПРОВЕРКИ")
    
    total = len(results)
    passed = sum(1 for r in results if r)
    
    print_info(f"Пройдено: {passed}/{total} проверок")
    
    if passed == total:
        print_success("Все проверки пройдены! Проект готов к развёртыванию.")
        print("\nСледующие шаги:")
        print("  1. Настройте .env для вашего хостинга")
        print("  2. Выполните: python manage.py migrate")
        print("  3. Выполните: python manage.py collectstatic")
        print("  4. Запустите: python manage.py runserver")
        print("  5. Следуйте инструкции в QUICK_START.md")
    elif passed >= total * 0.7:
        print_warning("Большинство проверок пройдено. Устраните оставшиеся проблемы.")
    else:
        print_error("Многие проверки не пройдены. Настройте проект перед развёртыванием.")
    
    print()


def main():
    """Основная функция"""
    print_header("UNIVERSAL DJANGO PROJECT - CONFIGURATION CHECK")
    
    results = []
    
    # Выполнение проверок
    results.append(check_python())
    results.append(check_django())
    results.append(check_env_file())
    results.append(check_requirements())
    results.append(check_hosting_detection())
    results.append(check_database())
    results.append(check_migrations())
    results.append(check_static())
    results.append(check_templates())
    
    # Итоги
    print_summary(results)
    
    # Возврат кода ошибки
    return 0 if all(results) else 1


if __name__ == '__main__':
    sys.exit(main())
