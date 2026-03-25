"""
Passenger WSGI entry point for Beget hosting - NEW VERSION
"""
import os
import sys

BASE_DIR = '/home/i/itrickon/itrickon.beget.tech/public_html'
PROJECT_DIR = os.path.join(BASE_DIR, 'directsite')
VENV_DIR = os.path.join(BASE_DIR, 'venv')

# Проверка существования venv
print(f"CHECKING: {VENV_DIR}/bin/activate_this.py exists = {os.path.exists(VENV_DIR + '/bin/activate_this.py')}", flush=True)

# Активация venv
activate_path = os.path.join(VENV_DIR, 'bin', 'activate_this.py')
if os.path.exists(activate_path):
    print(f"ACTIVATING: {activate_path}", flush=True)
    with open(activate_path) as f:
        exec(f.read(), {'__file__': activate_path})
    print("ACTIVATED", flush=True)

# Добавляем проект в sys.path
for p in [BASE_DIR, PROJECT_DIR]:
    if p not in sys.path:
        sys.path.insert(0, p)

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'directsite.settings')

print(f"IMPORTING DJANGO from {sys.executable}", flush=True)
from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()
print("SUCCESS", flush=True)
