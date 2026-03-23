#!/bin/bash
# Скрипт деплоя DirectSite на сервер

echo "=== 🚀 Деплой DirectSite ==="

# 1. Переходим в директорию проекта
cd /var/www/directsite || exit 1

# 2. Активируем виртуальное окружение
source venv/bin/activate

# 3. Обновляем зависимости
echo "📦 Установка зависимостей..."
pip install -r requirements.txt

# 4. Применяем миграции
echo "🗄️  Применение миграций..."
python directsite/manage.py migrate

# 5. Собираем статику
echo "📁 Сборка статических файлов..."
python directsite/manage.py collectstatic --noinput

# 6. Перезапускаем Gunicorn
echo "🔄 Перезапуск Gunicorn..."
sudo systemctl restart directsite

echo "✅ Деплой завершён!"
echo ""
echo "📊 Проверка статуса:"
sudo systemctl status directsite
