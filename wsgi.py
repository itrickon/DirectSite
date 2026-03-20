import os
import sys

# Путь к вашему логину на Timeweb
TIMWEB_LOGIN = 'your_login'

# Активация виртуального окружения
activate_this = os.path.expanduser(f'/home/c/{TIMWEB_LOGIN}/directsite.site/venv/bin/activate_this.py')
exec(open(activate_this).read(), {'__file__': activate_this})

# Добавляем путь к проекту
sys.path.insert(1, os.path.expanduser(f'/home/c/{TIMWEB_LOGIN}/directsite.site/public_html/source/directsite'))

from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'directsite.settings')
application = get_wsgi_application()
