"""
WSGI config for DirectSite project.
Universal configuration for any hosting provider.
"""

import os
import sys

from django.core.wsgi import get_wsgi_application

# Setup Django settings
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'directsite.settings')

# Add project directory to Python path
project_home = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
if project_home not in sys.path:
    sys.path.insert(0, project_home)

# Get WSGI application
application = get_wsgi_application()
