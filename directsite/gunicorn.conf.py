"""
Gunicorn configuration file for production deployment.
Use with: gunicorn --config gunicorn.conf.py directsite.wsgi:application
"""

import multiprocessing
import os

# ============================================================
# SERVER BINDING
# ============================================================

# Bind to all interfaces (for Docker) or localhost
bind = os.environ.get('GUNICORN_BIND', '0.0.0.0:8000')

# ============================================================
# WORKERS
# ============================================================

# Number of worker processes
# Formula: (2 x $num_cores) + 1
workers = int(os.environ.get('GUNICORN_WORKERS', multiprocessing.cpu_count() * 2 + 1))

# Worker class
worker_class = 'sync'

# Threads per worker
threads = int(os.environ.get('GUNICORN_THREADS', 1))

# Timeout for worker processes
timeout = int(os.environ.get('GUNICORN_TIMEOUT', 30))

# Keep-alive connections
keepalive = int(os.environ.get('GUNICORN_KEEPALIVE', 2))

# ============================================================
# LOGGING
# ============================================================

# Log files
accesslog = os.environ.get('GUNICORN_ACCESS_LOG', 'logs/gunicorn_access.log')
errorlog = os.environ.get('GUNICORN_ERROR_LOG', 'logs/gunicorn_error.log')

# Log level
loglevel = os.environ.get('GUNICORN_LOG_LEVEL', 'info')

# ============================================================
# PROCESS NAMING
# ============================================================

proc_name = 'directsite'

# ============================================================
# SERVER HOOKS
# ============================================================

def on_starting(server):
    """Called just before the master process is initialized."""
    print("Starting Gunicorn server...")

def on_reload(server):
    """Called to recycle workers during a reload via SIGHUP."""
    print("Reloading Gunicorn server...")
