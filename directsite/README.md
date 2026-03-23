# 🌐 Universal Django Project

**DirectSite** — универсальный Django-проект для развёртывания на любом хостинге.

---

## 🚀 Особенности

- ✅ **Универсальность** — работает на PythonAnywhere, Timeweb, Beget, VPS, Docker, Render, Railway
- ✅ **Авто-определение хостинга** — проект сам определяет где запущен
- ✅ **Единая конфигурация** — все настройки в `.env`
- ✅ **Быстрый старт** — развёртывание за 5-15 минут
- ✅ **Production-ready** — безопасность, логирование, оптимизация
- ✅ **Telegram уведомления** — заявки приходят в Telegram
- ✅ **Email уведомления** — дублирование на email

---

## 📋 Требования

- Python 3.8+ (рекомендуется 3.10)
- Django 4.2+
- SQLite (по умолчанию) или PostgreSQL

---

## 🎯 Быстрый старт

### 1. Клонирование/загрузка

```bash
# Если используете git
git clone <repository-url>
cd directsite

# Или распакуйте архив
cd directsite
```

### 2. Настройка окружения

```bash
# Скопируйте .env.example в .env
cp .env.example .env

# Отредактируйте .env
nano .env  # или используйте любой редактор
```

**Минимальные настройки:**
```env
DEBUG=False
SECRET_KEY=ваш-секретный-ключ
ALLOWED_HOSTS=ваш-домен.com
```

### 3. Установка зависимостей

```bash
# Создание виртуального окружения
python -m venv venv

# Активация (Linux/Mac)
source venv/bin/activate

# Активация (Windows)
venv\Scripts\activate

# Установка зависимостей
pip install -r requirements.txt
```

### 4. Инициализация

```bash
# Применение миграций
python manage.py migrate

# Сбор статики
python manage.py collectstatic --noinput

# Создание суперпользователя
python manage.py createsuperuser
```

### 5. Запуск

```bash
# Для разработки
python manage.py runserver

# Для production (Gunicorn)
gunicorn --config gunicorn.conf.py directsite.wsgi:application
```

---

## 📚 Документация

| Файл | Описание |
|------|----------|
| [QUICK_START.md](QUICK_START.md) | Быстрый старт за 5 минут |
| [HOSTING_GUIDE.md](HOSTING_GUIDE.md) | Полное руководство по хостингам |
| [README_DEPLOY.md](README_DEPLOY.md) | Инструкция для PythonAnywhere |

---

## 🌍 Поддерживаемые хостинги

### Shared Hosting

| Хостинг | Сложность | Бесплатно |
|---------|-----------|-----------|
| **PythonAnywhere** | ⭐ | ✅ (ограниченно) |
| **Timeweb** | ⭐⭐ | ❌ |
| **Beget** | ⭐⭐ | ✅ (ограниченно) |

### VPS / Cloud

| Платформа | Сложность | Бесплатно |
|-----------|-----------|-----------|
| **VPS (Ubuntu)** | ⭐⭐⭐⭐ | ❌ |
| **Docker** | ⭐⭐⭐ | ✅ (локально) |
| **Render** | ⭐⭐ | ✅ (ограниченно) |
| **Railway** | ⭐⭐ | ❌ |

---

## 🛠️ Структура проекта

```
directsite/
├── .env                      # Переменные окружения (не в git!)
├── .env.example              # Шаблон .env
├── .gitignore                # Игнорируемые файлы
├── requirements.txt          # Зависимости Python
├── runtime.txt               # Версия Python
├── Procfile                  # Для облачных платформ
├── gunicorn.conf.py          # Конфигурация Gunicorn
├── manage.py                 # Django management script
├── passenger_wsgi.py         # Для shared hosting
├── deploy.sh                 # Скрипт развёртывания (Linux/Mac)
├── deploy.ps1                # Скрипт развёртывания (Windows)
├── check_hosting.py          # Проверка конфигурации
├── config.py                 # Универсальная конфигурация
│
├── directsite/               # Основной модуль Django
│   ├── settings.py           # Настройки Django
│   ├── urls.py               # URL маршруты
│   ├── wsgi.py               # WSGI конфигурация
│   └── telegram_config.py    # Telegram настройки
│
├── core/                     # Основное приложение
│   ├── models.py             # Модели (Lead, VacancyApplication)
│   ├── views.py              # Представления
│   ├── forms.py              # Формы
│   ├── admin.py              # Админка
│   └── migrations/           # Миграции БД
│
├── templates/                # HTML шаблоны
│   ├── base.html
│   ├── index.html
│   ├── service.html
│   ├── contacts.html
│   ├── vacancy.html
│   └── ...
│
├── static/                   # Статические файлы (CSS, JS, images)
├── staticfiles/              # Собранная статика (для production)
├── logs/                     # Логи
└── db.sqlite3                # База данных SQLite
```

---

## ⚙️ Конфигурация

### Переменные окружения (.env)

```env
# Основные
DEBUG=False
SECRET_KEY=ваш-секретный-ключ
ALLOWED_HOSTS=domain.com,www.domain.com

# База данных (опционально, SQLite по умолчанию)
DATABASE_URL=postgresql://user:pass@localhost/dbname

# Telegram
TELEGRAM_BOT_TOKEN=token
TELEGRAM_CHAT_ID=chat_id

# Email
EMAIL_HOST_USER=@gmail.com
EMAIL_HOST_PASSWORD=app-password
ADMIN_EMAIL=admin@example.com

# Хостинг (опционально, авто-определение)
HOSTING_TYPE=pythonanywhere
```

---

## 📦 Основные команды

```bash
# Проверка конфигурации
python check_hosting.py

# Проверка Django
python manage.py check

# Миграции
python manage.py makemigrations
python manage.py migrate

# Создание суперпользователя
python manage.py createsuperuser

# Сбор статики
python manage.py collectstatic --noinput

# Запуск сервера разработки
python manage.py runserver

# Запуск production сервера
gunicorn --config gunicorn.conf.py directsite.wsgi:application
```

---

## 🔧 Развёртывание

### Автоматическое (рекомендуется)

**Linux/Mac:**
```bash
chmod +x deploy.sh
./deploy.sh
```

**Windows:**
```powershell
.\deploy.ps1
```

### Ручное развёртывание

Следуйте инструкции в [HOSTING_GUIDE.md](HOSTING_GUIDE.md) для вашего хостинга.

---

## 🔐 Безопасность

### Для production обязательно:

1. **DEBUG=False** в `.env`
2. **Секретный ключ** — сгенерируйте новый
3. **ALLOWED_HOSTS** — укажите ваши домены
4. **HTTPS** — используйте SSL сертификат
5. **.env не в git** — добавьте в `.gitignore`

### Генерация секретного ключа:

```bash
python -c "from django.core.management.utils import get_random_secret_key; print(get_random_secret_key())"
```

---

## 📊 Функционал

### Для пользователей:

- ✅ Главная страница с формой заявки
- ✅ Страница услуг
- ✅ Страница контактов
- ✅ Страница вакансий с формой отклика
- ✅ Калькулятор услуг
- ✅ Политика конфиденциальности
- ✅ Пользовательское соглашение

### Для администраторов:

- ✅ Панель управления Django Admin
- ✅ Управление заявками (Lead)
- ✅ Управление откликами (VacancyApplication)
- ✅ Telegram уведомления
- ✅ Email уведомления

---

## 🐛 Troubleshooting

### Частые проблемы:

**ModuleNotFoundError:**
```bash
source venv/bin/activate
pip install -r requirements.txt
```

**DisallowedHost:**
Добавьте домен в `.env`:
```env
ALLOWED_HOSTS=yourdomain.com
```

**Static files not found:**
```bash
python manage.py collectstatic --noinput
```

**Database locked:**
```bash
python manage.py migrate
```

---

## 📞 Поддержка

- **Документация Django**: https://docs.djangoproject.com/
- **Stack Overflow**: https://stackoverflow.com/questions/tagged/django
- **PythonAnywhere Help**: https://help.pythonanywhere.com/

---

## 📝 Лицензия

Этот проект создан для образовательных и коммерческих целей.

---

## ✅ Чек-лист перед запуском

- [ ] `.env` настроен
- [ ] `DEBUG=False` (для production)
- [ ] `SECRET_KEY` сгенерирован
- [ ] `ALLOWED_HOSTS` настроен
- [ ] Зависимости установлены
- [ ] Миграции применены
- [ ] Статика собрана
- [ ] Суперпользователь создан
- [ ] Логи настроены
- [ ] SSL установлен (для production)

---

## 🎉 Готово!

Проект готов к развёртыванию. Следуйте [QUICK_START.md](QUICK_START.md) или [HOSTING_GUIDE.md](HOSTING_GUIDE.md).

**Удачи! 🚀**
