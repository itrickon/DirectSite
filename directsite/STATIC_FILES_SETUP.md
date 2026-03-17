# Настройка статических файлов Django

## Текущая конфигурация

### settings.py
```python
STATIC_URL = 'static/'
STATICFILES_DIRS = [BASE_DIR / 'static']
STATIC_ROOT = BASE_DIR / 'staticfiles'
```

## Структура папок

```
directsite/
├── static/              # Исходные статические файлы (разработка)
│   ├── css/            # CSS файлы (пусто)
│   ├── js/             # JavaScript файлы (пусто)
│   └── images/         # Изображения
│       ├── DirectLine_6.png
│       ├── 1773323333c8e6.png
│       └── _.jpg
└── staticfiles/        # Собранные файлы (продакшен, в .gitignore)
    ├── admin/          # Статика Django админки
    └── images/         # Копии изображений
```

## Команды

### Сбор статических файлов
```bash
cd "c:\Users\I\Desktop\GitHub Repositories\DirectSite\directsite"
..\myenv\Scripts\python.exe manage.py collectstatic --noinput
```

### Очистка staticfiles
```bash
..\myenv\Scripts\python.exe manage.py collectstatic --clear
```

## Настройка для продакшена

### 1. В settings.py изменить:
```python
DEBUG = False
STATIC_URL = '/static/'
STATIC_ROOT = BASE_DIR / 'staticfiles'
```

### 2. Настройка веб-сервера

**Nginx пример:**
```nginx
location /static/ {
    alias /path/to/directsite/staticfiles/;
}
```

**Apache пример:**
```apache
Alias /static/ /path/to/directsite/staticfiles/
<Directory /path/to/directsite/staticfiles>
    Require all granted
</Directory>
```

### 3. WhiteNoise для Django (опционально)

Для обслуживания статики через Django:

```bash
pip install whitenoise
```

```python
# settings.py
MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',  # После SecurityMiddleware
    # ... остальные middleware
]

STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'
```

## Примечания

- Папка `staticfiles/` добавлена в `.gitignore`
- Пустые папки `css/` и `js/` содержат `.gitkeep` для отслеживания в git
- Все изображения доступны через `{% static 'images/filename.png' %}`
