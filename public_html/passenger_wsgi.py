"""
Passenger WSGI entry point for Timeweb hosting.
Этот файл должен быть в public_html/
"""

import os
import sys

# Ваш логин на Timeweb
TIMWEB_LOGIN = 'cc697629'

# Пути на сервере (ваша структура)
BASE_DIR = f'/home/c/{TIMWEB_LOGIN}/directsite/public_html'
PROJECT_DIR = f'{BASE_DIR}/directsite'
VENV_DIR = f'{BASE_DIR}/venv'

# Активация виртуального окружения
try:
    activate_this = f'{VENV_DIR}/bin/activate_this.py'
    exec(open(activate_this).read(), {'__file__': activate_this})
except FileNotFoundError:
    pass  # Если нет venv, работаем без него

# Добавляем проект в sys.path
sys.path.insert(0, PROJECT_DIR)

# Устанавливаем переменные окружения
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'directsite.settings')
os.environ.setdefault('PYTHONHOME', VENV_DIR)

# Импортируем Django application
from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()
