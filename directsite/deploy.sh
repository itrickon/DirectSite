#!/bin/bash
# ============================================================
# UNIVERSAL DEPLOY SCRIPT
# Автоматическая настройка Django проекта на любом хостинге
# ============================================================

set -e  # Exit on error

# Colors for output
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
NC='\033[0m' # No Color

# Functions
print_step() {
    echo -e "${GREEN}>>> $1${NC}"
}

print_warning() {
    echo -e "${YELLOW}!!! $1${NC}"
}

print_error() {
    echo -e "${RED}!!! $1${NC}"
}

# ============================================================
# DETECT HOSTING ENVIRONMENT
# ============================================================

detect_environment() {
    print_step "Detecting environment..."
    
    if [ -n "$PYTHONANYWHERE" ]; then
        HOSTING="pythonanywhere"
    elif [ -n "$RENDER" ]; then
        HOSTING="render"
    elif [ -n "$RAILWAY" ]; then
        HOSTING="railway"
    elif [ -f "/.dockerenv" ]; then
        HOSTING="docker"
    elif [ -n "$HEROKU" ]; then
        HOSTING="heroku"
    else
        HOSTING="shared"
    fi
    
    echo "Detected hosting: $HOSTING"
}

# ============================================================
# INSTALL DEPENDENCIES
# ============================================================

install_dependencies() {
    print_step "Installing dependencies..."
    
    if command -v python3 &> /dev/null; then
        PYTHON=python3
    elif command -v python &> /dev/null; then
        PYTHON=python
    else
        print_error "Python not found!"
        exit 1
    fi
    
    echo "Using Python: $($PYTHON --version)"
    
    # Create virtual environment if not exists
    if [ ! -d ".venv" ]; then
        print_step "Creating virtual environment..."
        $PYTHON -m venv .venv
    fi
    
    # Activate virtual environment
    print_step "Activating virtual environment..."
    source .venv/bin/activate
    
    # Upgrade pip
    pip install --upgrade pip
    
    # Install requirements
    if [ -f "requirements.txt" ]; then
        print_step "Installing Python packages..."
        pip install -r requirements.txt
    else
        print_error "requirements.txt not found!"
        exit 1
    fi
}

# ============================================================
# DATABASE MIGRATIONS
# ============================================================

run_migrations() {
    print_step "Running database migrations..."
    
    python manage.py migrate --noinput
    
    print_step "Database migrations completed!"
}

# ============================================================
# COLLECT STATIC FILES
# ============================================================

collect_static() {
    print_step "Collecting static files..."
    
    # Create staticfiles directory if not exists
    mkdir -p staticfiles
    
    python manage.py collectstatic --noinput
    
    print_step "Static files collected!"
}

# ============================================================
# CREATE SUPERUSER (OPTIONAL)
# ============================================================

create_superuser() {
    print_warning "Create superuser? (y/n)"
    read -r response
    
    if [[ "$response" =~ ^([yY][eE][sS]|[yY])$ ]]; then
        print_step "Creating superuser..."
        python manage.py createsuperuser
    fi
}

# ============================================================
# SETUP LOGS DIRECTORY
# ============================================================

setup_logs() {
    print_step "Setting up logs directory..."
    
    mkdir -p logs
    touch logs/django.log
    touch logs/gunicorn_access.log
    touch logs/gunicorn_error.log
    
    print_step "Logs directory ready!"
}

# ============================================================
# HOSTING-SPECIFIC SETUP
# ============================================================

setup_pythonanywhere() {
    print_step "PythonAnywhere-specific setup..."
    
    # Create bash profile for virtualenv
    cat > ~/.bash_profile << 'EOF'
# PythonAnywhere virtualenv
export VIRTUALENV=/home/$(whoami)/.venvs/directsite
source $VIRTUALENV/bin/activate
EOF
    
    print_warning "Don't forget to:"
    echo "1. Set up Web App in PythonAnywhere control panel"
    echo "2. Configure WSGI file: /home/$(whoami)/directsite/passenger_wsgi.py"
    echo "3. Add static files mapping: /static/ -> /home/$(whoami)/directsite/staticfiles/"
    echo "4. Click Reload button"
}

setup_timeweb() {
    print_step "Timeweb-specific setup..."
    
    print_warning "Don't forget to:"
    echo "1. Set Python version in control panel"
    echo "2. Configure .htaccess"
    echo "3. Set up passenger_wsgi.py"
}

setup_vps() {
    print_step "VPS-specific setup..."
    
    print_warning "For production with Gunicorn and Nginx:"
    echo "1. Copy gunicorn.service to /etc/systemd/system/"
    echo "2. systemctl enable gunicorn"
    echo "3. systemctl start gunicorn"
    echo "4. Configure Nginx as reverse proxy"
}

# ============================================================
# MAIN EXECUTION
# ============================================================

main() {
    echo "============================================================"
    echo "UNIVERSAL DJANGO DEPLOY SCRIPT"
    echo "============================================================"
    
    detect_environment
    
    install_dependencies
    run_migrations
    collect_static
    setup_logs
    
    case $HOSTING in
        pythonanywhere)
            setup_pythonanywhere
            ;;
        timeweb)
            setup_timeweb
            ;;
        vps|docker)
            setup_vps
            ;;
    esac
    
    echo ""
    echo "============================================================"
    print_step "Deployment completed successfully!"
    echo "============================================================"
    echo ""
    echo "Next steps:"
    echo "1. Check logs/django.log for any errors"
    echo "2. Run: python manage.py check"
    echo "3. Start the server or reload your web app"
    echo ""
}

# Run main function
main "$@"
