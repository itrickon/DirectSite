import os
import sys

# Путь к проекту на Timeweb
project_home = '/home/u/cc697629/directsite'
if project_home not in sys.path:
    sys.path.insert(0, project_home)

# Устанавливаем переменную окружения для Django
os.environ['DJANGO_SETTINGS_MODULE'] = 'directsite.settings'

# Импортируем WSGI-приложение Django
from directsite.wsgi import application
