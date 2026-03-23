#!/bin/bash
# Скрипт для исправления ошибки логирования на PythonAnywhere

echo "=================================================="
echo "Исправление ошибки логирования для PythonAnywhere"
echo "=================================================="

# Переход в папку проекта
cd /home/Tricko66/directsite

echo ""
echo "1. Создание папки logs..."
mkdir -p logs

echo "2. Создание файла django.log..."
touch logs/django.log

echo "3. Установка правильных прав..."
chmod 755 logs
chmod 644 logs/django.log

echo "4. Проверка..."
ls -la logs/

echo ""
echo "=================================================="
echo "Готово!"
echo "=================================================="
echo ""
echo "Теперь:"
echo "1. Вернитесь на вкладку Web в панели PythonAnywhere"
echo "2. Нажмите оранжевую кнопку 'Reload'"
echo "3. Проверьте сайт: https://tricko66.pythonanywhere.com/"
echo ""
