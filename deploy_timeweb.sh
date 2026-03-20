#!/bin/bash
# Скрипт для деплоя на виртуальный хостинг Timeweb

# Настройки
TIMWEB_LOGIN="your_login"
SITE_NAME="directsite"

# Пути
BASE_DIR="/home/c/${TIMWEB_LOGIN}/${SITE_NAME}.site"
PUBLIC_HTML="${BASE_DIR}/public_html"
VENV_DIR="${BASE_DIR}/venv"

echo "=== Деплой на Timeweb ==="

# 1. Создание виртуального окружения (если нет)
if [ ! -d "${VENV_DIR}" ]; then
    echo "Создание виртуального окружения..."
    cd "${BASE_DIR}"
    wget https://bootstrap.pypa.io/virtualenv/3.10/virtualenv.pyz
    python3 virtualenv.pyz venv
fi

# 2. Активация виртуального окружения
source "${VENV_DIR}/bin/activate"

# 3. Установка зависимостей
echo "Установка зависимостей..."
cd "${PUBLIC_HTML}/source"
pip install -r requirements.txt

# 4. Миграции
echo "Выполнение миграций..."
cd "${PUBLIC_HTML}/source/directsite"
python manage.py migrate

# 5. Сборка статики
echo "Сборка статических файлов..."
python manage.py collectstatic --noinput

# 6. Создание суперпользователя (опционально)
# python manage.py createsuperuser

echo "=== Деплой завершён! ==="
echo "Откройте http://${TIMWEB_LOGIN}.tw1.ru/"
