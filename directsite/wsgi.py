"""
WSGI entry point for shared hosting (Beget, Timeweb).
Этот файл должен быть в public_html/
"""

import os
import sys

# ============================================================
# ПУТИ К ПРОЕКТУ (измените под ваш хостинг)
# ============================================================

# Для Beget: замените 'cc697629' на ваш логин
USERNAME = 'cc697629'

# Пути
BASE_DIR = f'/home/c/{USERNAME}/public_html'
PROJECT_DIR = f'{BASE_DIR}/directsite'
VENV_DIR = f'{BASE_DIR}/venv'

# ============================================================
# АКТИВАЦИЯ ВИРТУАЛЬНОГО ОКРУЖЕНИЯ
# ============================================================

activate_this = os.path.join(VENV_DIR, 'bin', 'activate_this.py')
try:
    with open(activate_this) as f:
        exec(f.read(), {'__file__': activate_this})
except FileNotFoundError:
    pass  # Если нет venv, работаем без него

# ============================================================
# ДОБАВЛЯЕМ ПРОЕКТ В sys.path
# ============================================================

if PROJECT_DIR not in sys.path:
    sys.path.insert(0, PROJECT_DIR)

# ============================================================
# ЗАГРУЗКА DJANGO
# ============================================================

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'directsite.settings')

from django.core.wsgi import get_wsgi_application

application = get_wsgi_application()
