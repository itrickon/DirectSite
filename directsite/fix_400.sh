#!/bin/bash
# Скрипт для исправления ошибки 400 Bad Request на PythonAnywhere

echo "============================================================"
echo "ИСПРАВЛЕНИЕ ОШИБКИ 400 BAD REQUEST"
echo "============================================================"

# Переход в папку проекта
cd /home/Tricko66/directsite

echo ""
echo "1. Проверка текущего .env..."
if [ -f .env ]; then
    echo "Файл .env найден:"
    cat .env | grep -E "(ALLOWED_HOSTS|DEBUG|SECRET_KEY)"
else
    echo "Файл .env не найден! Создаём новый..."
fi

echo ""
echo "2. Создание правильного .env..."

cat > .env << 'EOF'
# Настройки для PythonAnywhere
DEBUG=True
SECRET_KEY=django-insecure-v3&o7+pphz)9b4k8d3f@tkm(*h1tu(e6b#k82z_6q570c**%!9

# ВАЖНО: Укажите ваш точный домен PythonAnywhere
ALLOWED_HOSTS=tricko66.pythonanywhere.com,www.tricko66.pythonanywhere.com,localhost,127.0.0.1

# База данных
DATABASE_URL=

# Telegram
TELEGRAM_BOT_TOKEN=8759215207:AAH8MINAOy0pD796VyuWSxz-XiojZZUHTSE
TELEGRAM_CHAT_ID=2072693808

# Email
EMAIL_HOST=smtp.gmail.com
EMAIL_PORT=587
EMAIL_USE_TLS=True
EMAIL_HOST_USER=your-gmail@gmail.com
EMAIL_HOST_PASSWORD=your-app-password
ADMIN_EMAIL=directlines@atomicmail.io

# Хостинг
HOSTING_TYPE=pythonanywhere
EOF

echo "Файл .env создан!"
echo ""
echo "3. Проверка содержимого:"
cat .env

echo ""
echo "============================================================"
echo "ГОТОВО!"
echo "============================================================"
echo ""
echo "Следующие шаги:"
echo "1. Вернитесь на вкладку Web в панели PythonAnywhere"
echo "2. Нажмите оранжевую кнопку 'Reload'"
echo "3. Проверьте сайт: https://tricko66.pythonanywhere.com/"
echo ""
echo "Если ошибка 400 остаётся, проверьте:"
echo "- Точный домен в панели PythonAnywhere (Web → URL)"
echo "- Добавьте его в ALLOWED_HOSTS в формате: domain.pythonanywhere.com"
echo ""
