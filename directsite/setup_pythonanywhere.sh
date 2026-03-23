#!/bin/bash
# Скрипт настройки проекта DirectSite на PythonAnywhere
# Запускать через Bash консоль на PythonAnywhere

echo "=================================================="
echo "Настройка DirectSite на PythonAnywhere"
echo "=================================================="

# Переход в папку проекта
cd /home/Tricko66/directsite

echo ""
echo "1. Проверка Python..."
python3 --version

echo ""
echo "2. Создание виртуального окружения..."
python3 -m venv /home/Tricko66/.venvs/directsite

echo ""
echo "3. Активация виртуального окружения и установка зависимостей..."
source /home/Tricko66/.venvs/directsite/bin/activate
pip install --upgrade pip
pip install -r requirements.txt

echo ""
echo "4. Применение миграций базы данных..."
python3 manage.py migrate

echo ""
echo "5. Сбор статических файлов..."
python3 manage.py collectstatic --noinput

echo ""
echo "6. Проверка конфигурации Django..."
python3 manage.py check

echo ""
echo "=================================================="
echo "Настройка завершена!"
echo "=================================================="
echo ""
echo "Следующие шаги:"
echo "1. Зайдите в панель Web: https://www.pythonanywhere.com/user/Tricko66/webapp/"
echo "2. Создайте новое web-приложение или обновите существующее"
echo "3. Укажите Code directory: /home/Tricko66/directsite"
echo "4. Укажите WSGI file: /home/Tricko66/directsite/passenger_wsgi.py"
echo "5. Добавьте Static files mapping:"
echo "   URL: /static/  →  Directory: /home/Tricko66/directsite/staticfiles/"
echo "6. Нажмите кнопку Reload"
echo ""
echo "Сайт будет доступен по адресу: https://tricko66.pythonanywhere.com/"
