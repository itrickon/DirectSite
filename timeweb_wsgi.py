import os
import sys

# Ваш логин на Timeweb - ЗАМЕНИТЕ на ваш!
TIMWEB_LOGIN = 'cc697629'

# Активация виртуального окружения
activate_this = f'/home/c/{TIMWEB_LOGIN}/directsite.site/venv/bin/activate_this.py'

try:
    exec(open(activate_this).read(), {'__file__': activate_this})
except FileNotFoundError:
    pass  # Если нет venv, пробуем без него

# Добавляем путь к проекту
project_path = f'/home/c/{TIMWEB_LOGIN}/directsite.site/source/directsite'
sys.path.insert(0, project_path)

from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'directsite.settings')
application = get_wsgi_application()
