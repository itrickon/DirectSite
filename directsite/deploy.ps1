# ============================================================
# UNIVERSAL DEPLOY SCRIPT FOR WINDOWS (PowerShell)
# ============================================================

Write-Host "============================================================" -ForegroundColor Green
Write-Host "UNIVERSAL DJANGO DEPLOY SCRIPT (Windows)" -ForegroundColor Green
Write-Host "============================================================" -ForegroundColor Green
Write-Host ""

# ============================================================
# CHECK PYTHON
# ============================================================

Write-Host ">>> Checking Python installation..." -ForegroundColor Green

try {
    $pythonVersion = python --version 2>&1
    Write-Host "Found: $pythonVersion" -ForegroundColor Green
} catch {
    Write-Host "!!! Python not found! Please install Python 3.8+" -ForegroundColor Red
    exit 1
}

# ============================================================
# CREATE VIRTUAL ENVIRONMENT
# ============================================================

Write-Host ""
Write-Host ">>> Creating virtual environment..." -ForegroundColor Green

if (-not (Test-Path ".venv")) {
    python -m venv .venv
    Write-Host "Virtual environment created!" -ForegroundColor Green
} else {
    Write-Host "Virtual environment already exists" -ForegroundColor Yellow
}

# ============================================================
# ACTIVATE VIRTUAL ENVIRONMENT
# ============================================================

Write-Host ""
Write-Host ">>> Activating virtual environment..." -ForegroundColor Green
& ".\.venv\Scripts\Activate.ps1"

# ============================================================
# INSTALL DEPENDENCIES
# ============================================================

Write-Host ""
Write-Host ">>> Installing dependencies..." -ForegroundColor Green

if (Test-Path "requirements.txt") {
    pip install --upgrade pip
    pip install -r requirements.txt
    Write-Host "Dependencies installed!" -ForegroundColor Green
} else {
    Write-Host "!!! requirements.txt not found!" -ForegroundColor Red
    exit 1
}

# ============================================================
# DATABASE MIGRATIONS
# ============================================================

Write-Host ""
Write-Host ">>> Running database migrations..." -ForegroundColor Green

python manage.py migrate --noinput

Write-Host "Database migrations completed!" -ForegroundColor Green

# ============================================================
# COLLECT STATIC FILES
# ============================================================

Write-Host ""
Write-Host ">>> Collecting static files..." -ForegroundColor Green

if (-not (Test-Path "staticfiles")) {
    New-Item -ItemType Directory -Path "staticfiles" | Out-Null
}

python manage.py collectstatic --noinput

Write-Host "Static files collected!" -ForegroundColor Green

# ============================================================
# SETUP LOGS DIRECTORY
# ============================================================

Write-Host ""
Write-Host ">>> Setting up logs directory..." -ForegroundColor Green

if (-not (Test-Path "logs")) {
    New-Item -ItemType Directory -Path "logs" | Out-Null
    New-Item -ItemType File -Path "logs\django.log" | Out-Null
}

Write-Host "Logs directory ready!" -ForegroundColor Green

# ============================================================
# CREATE SUPERUSER (OPTIONAL)
# ============================================================

Write-Host ""
Write-Host ">>> Create superuser? (y/n)" -ForegroundColor Yellow
$response = Read-Host

if ($response -eq "y" -or $response -eq "Y") {
    Write-Host "Creating superuser..." -ForegroundColor Green
    python manage.py createsuperuser
}

# ============================================================
# FINAL CHECK
# ============================================================

Write-Host ""
Write-Host ">>> Running Django check..." -ForegroundColor Green

python manage.py check

# ============================================================
# COMPLETE
# ============================================================

Write-Host ""
Write-Host "============================================================" -ForegroundColor Green
Write-Host "DEPLOYMENT COMPLETED SUCCESSFULLY!" -ForegroundColor Green
Write-Host "============================================================" -ForegroundColor Green
Write-Host ""
Write-Host "Next steps:" -ForegroundColor Yellow
Write-Host "1. Check logs\django.log for any errors"
Write-Host "2. Run: python manage.py runserver (for development)"
Write-Host "3. Or configure your web server for production"
Write-Host ""

# Deactivate virtual environment
deactivate
