"""
WSGI entry point for Beget hosting.
"""
import os
import sys

# Пути для Beget
BASE_DIR = '/home/i/itrickon/itrickon.beget.tech/public_html'
PROJECT_DIR = os.path.join(BASE_DIR, 'directsite')
VENV_DIR = os.path.join(BASE_DIR, 'venv')

# Активация venv
activate_this = os.path.join(VENV_DIR, 'bin', 'activate_this.py')
try:
    with open(activate_this) as f:
        exec(f.read(), {'__file__': activate_this})
except FileNotFoundError:
    pass

# Добавляем проект в sys.path
for path in [BASE_DIR, PROJECT_DIR]:
    if path not in sys.path:
        sys.path.insert(0, path)

# Django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'directsite.settings')
os.environ.setdefault('PROJECT_ROOT', BASE_DIR)
os.environ.setdefault('PUBLIC_HTML_DIR', BASE_DIR)

from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()