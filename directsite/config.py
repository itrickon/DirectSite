"""
Универсальная система конфигурации для Django проекта
Поддерживает различные хостинги: PythonAnywhere, Timeweb, Beget, VPS и др.
"""
import os
import sys
from pathlib import Path

try:
    from dotenv import load_dotenv
    load_dotenv()
except ImportError:
    pass


def get_bool_env(name, default=False):
    """Получить boolean значение из переменной окружения"""
    value = os.environ.get(name, str(default)).lower()
    return value in ('true', '1', 'yes', 'on')


def get_list_env(name, default=None):
    """Получить список из переменной окружения (через запятую)"""
    value = os.environ.get(name, '')
    if value:
        return [item.strip() for item in value.split(',')]
    return default or []


def detect_hosting():
    """
    Авто-определение типа хостинга по переменным окружения и путям
    """
    # Проверка переменной окружения
    hosting_type = os.environ.get('HOSTING_TYPE', '').lower()
    if hosting_type:
        return hosting_type

    # PythonAnywhere
    if 'PYTHONANYWHERE' in os.environ.get('HOME', '').upper():
        return 'pythonanywhere'
    if 'pythonanywhere' in sys.executable.lower():
        return 'pythonanywhere'

    # Beget - проверка по пути
    home = os.environ.get('HOME', '')
    if '/home/i/' in home or '/beget.tech/' in home:
        return 'beget'

    # Docker
    if os.path.exists('/.dockerenv'):
        return 'docker'

    # Render
    if os.environ.get('RENDER'):
        return 'render'

    # Railway
    if os.environ.get('RAILWAY'):
        return 'railway'

    # Heroku
    if os.environ.get('HEROKU'):
        return 'heroku'

    # VPS (по наличию DATABASE_URL)
    if os.environ.get('DATABASE_URL'):
        return 'vps'

    # По умолчанию - shared hosting или локальная разработка
    return 'shared'


def get_database_config(base_dir, hosting_type=None):
    """
    Конфигурация базы данных в зависимости от хостинга
    """
    database_url = os.environ.get('DATABASE_URL', '')

    # Если есть DATABASE_URL - используем PostgreSQL
    if database_url:
        import dj_database_url
        return {'default': dj_database_url.config(default=database_url, conn_max_age=600)}

    # SQLite по умолчанию
    return {
        'default': {
            'ENGINE': 'django.db.backends.sqlite3',
            'NAME': base_dir / 'db.sqlite3',
        }
    }


def get_allowed_hosts(hosting_type=None):
    """
    Получение списка разрешённых хостов
    """
    # Из переменной окружения (приоритет)
    allowed_hosts = get_list_env('ALLOWED_HOSTS')
    if allowed_hosts:
        return allowed_hosts

    # По умолчанию для разных хостингов
    defaults = {
        'pythonanywhere': ['tricko66.pythonanywhere.com', 'localhost', '127.0.0.1'],
        'timeweb': ['cc697629.tw1.ru', 'localhost', '127.0.0.1'],
        'beget': ['yoursite.beget.tech', 'localhost', '127.0.0.1'],
        'vps': ['localhost', '127.0.0.1'],
        'docker': ['localhost', '127.0.0.1', '0.0.0.0'],
        'render': ['localhost', '127.0.0.1'],
        'railway': ['localhost', '127.0.0.1'],
        'shared': ['localhost', '127.0.0.1'],
    }

    return defaults.get(hosting_type, ['localhost', '127.0.0.1'])


def get_static_root(base_dir, hosting_type=None):
    """
    Получение пути для STATIC_ROOT
    """
    # Из переменной окружения
    static_root = os.environ.get('STATIC_ROOT', '')
    if static_root:
        return static_root

    # По умолчанию
    return str(base_dir / 'staticfiles')


def get_project_path(base_dir, hosting_type=None):
    """
    Получение пути к проекту
    """
    # Из переменной окружения
    project_path = os.environ.get('PROJECT_PATH', '')
    if project_path:
        return project_path

    # Авто-определение для популярных хостингов
    home = os.environ.get('HOME', '')

    paths = {
        'pythonanywhere': f'/home/{home.split("/")[-1]}/directsite',
        'timeweb': f'/home/u/{home.split("/")[-1]}/directsite',
        'beget': f'/home/u/{home.split("/")[-1]}/mysite',
    }

    return paths.get(hosting_type, str(base_dir))


# Экспорт функций
__all__ = [
    'get_bool_env',
    'get_list_env',
    'detect_hosting',
    'get_database_config',
    'get_allowed_hosts',
    'get_static_root',
    'get_project_path',
]
