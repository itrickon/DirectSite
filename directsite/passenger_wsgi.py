"""
WSGI configuration for shared hosting (PythonAnywhere, Timeweb, Beget).
This file is used by Passenger/mod_wsgi to load your Django application.
"""

import os
import sys

# ============================================================
# PROJECT PATH CONFIGURATION
# ============================================================

# Get the project root directory
# Adjust this path according to your hosting:
# PythonAnywhere: /home/Tricko66/directsite
# Timeweb: /home/u/cc697629/directsite
# Beget: /home/u/username/mysite

# Auto-detect from HOME environment variable
home = os.environ.get('HOME', '')
username = home.split('/')[-1] if home else 'user'

# Try common hosting paths
possible_paths = [
    f'/home/{username}/directsite',
    f'/home/u/{username}/directsite',
    f'/home/{username}/mysite',
    f'/var/www/{username}/directsite',
    os.path.dirname(os.path.dirname(os.path.abspath(__file__))),
]

# Find the correct project path
PROJECT_PATH = None
for path in possible_paths:
    if os.path.exists(path):
        PROJECT_PATH = path
        break

if not PROJECT_PATH:
    PROJECT_PATH = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# Add project to Python path
if PROJECT_PATH not in sys.path:
    sys.path.insert(0, PROJECT_PATH)

# ============================================================
# DJANGO SETTINGS
# ============================================================

# Set Django settings module
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'directsite.settings')

# ============================================================
# IMPORT APPLICATION
# ============================================================

# Import Django WSGI application
from django.core.wsgi import get_wsgi_application

application = get_wsgi_application()

# ============================================================
# DEBUG INFORMATION (remove in production)
# ============================================================

# Uncomment for debugging:
# import sys
# with open('/tmp/wsgi_debug.txt', 'w') as f:
#     f.write(f"Python path: {sys.path}\n")
#     f.write(f"Project path: {PROJECT_PATH}\n")
#     f.write(f"HOME: {os.environ.get('HOME', 'Not set')}\n")
