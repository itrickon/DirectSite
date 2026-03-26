# DirectSite — Веб-сайт для маркетингового IT агентства Direct Line

## Описание

DirectSite — это веб-сайт для маркетингового IT агентства Direct Line, специализирующейся на услугах лидогенерации, call-центра, продвижения на Авито, рекрутинга и комплексных маркетинговых решениях.

Сайт предоставляет информацию об услугах компании, позволяет оставить заявку на консультацию, ознакомиться с вакансиями и использовать онлайн-калькулятор для расчёта стоимости услуг.

## Технологии

- **Backend:** Django 4.2
- **Frontend:** HTML5, CSS3, JavaScript
- **База данных:** SQLite
- **Хостинг:** Beget (Passenger WSGI)
- **Интеграции:** Telegram Bot API

## Структура проекта

```
directsite/
├── directsite/              # Основной проект Django
│   ├── settings.py          # Настройки проекта
│   ├── urls.py              # URL-маршруты
│   ├── wsgi.py              # WSGI конфигурация
│   └── asgi.py              # ASGI конфигурация
├── core/                    # Основное приложение
│   ├── models.py            # Модели данных (Lead, VacancyApplication)
│   ├── views.py             # Обработчики запросов
│   ├── forms.py             # Формы (LeadForm, VacancyApplicationForm)
│   └── admin.py             # Админ-панель
├── templates/               # HTML-шаблоны
├── static/                  # Статические файлы (CSS, JS, изображения)
├── logs/                    # Логи приложения
├── passenger_wsgi.py        # Точка входа для Beget
├── manage.py                # Утилита управления Django
├── requirements.txt         # Зависимости проекта
└── .env                     # Переменные окружения
```

## Установка и запуск

### Локальная разработка

1. Клонируйте репозиторий:
```bash
git clone <repository-url>
cd DirectSite/directsite
```

2. Создайте виртуальное окружение:
```bash
python -m venv venv
source venv/bin/activate  # Linux/Mac
venv\Scripts\activate     # Windows
```

3. Установите зависимости:
```bash
pip install -r requirements.txt
```

4. Примените миграции:
```bash
python manage.py migrate
```

5. Создайте суперпользователя:
```bash
python manage.py createsuperuser
```

6. Запустите сервер разработки:
```bash
python manage.py runserver
```

Сайт будет доступен по адресу: http://127.0.0.1:8000/

### Развёртывание на Beget

1. Загрузите файлы проекта в папку `/home/i/itrickon/itrickon.beget.tech/public_html/`

2. Установите зависимости:
```bash
cd /home/i/itrickon/itrickon.beget.tech/public_html
source venv/bin/activate
pip install -r requirements.txt
```

3. Примените миграции:
```bash
python manage.py migrate
python manage.py collectstatic --noinput
```

4. Перезапустите приложение через панель Beget или файл `restart.txt`

## Конфигурация

### Переменные окружения (.env)

| Переменная | Описание | Пример |
|------------|----------|--------|
| `DEBUG` | Режим отладки | `True` / `False` |
| `SECRET_KEY` | Секретный ключ Django | `your-secret-key` |
| `ALLOWED_HOSTS` | Разрешённые хосты | `example.com,www.example.com` |
| `TELEGRAM_BOT_TOKEN` | Токен Telegram-бота | `123456:ABC-DEF1234` |
| `TELEGRAM_CHAT_ID` | ID чата для уведомлений | `123456789` |
| `EMAIL_HOST` | SMTP сервер | `smtp.gmail.com` |
| `EMAIL_PORT` | SMTP порт | `587` |
| `EMAIL_HOST_USER` | Email для уведомлений | `noreply@example.com` |

### Безопасность (продакшен)

Для продакшена установите в `.env`:

```env
DEBUG=False
SECRET_KEY=<сгенерируйте новый ключ>
SECURE_SSL_REDIRECT=True
SESSION_COOKIE_SECURE=True
CSRF_COOKIE_SECURE=True
```

## Функционал

### Для посетителей

- Просмотр информации об услугах
- Онлайн-калькулятор расчёта стоимости
- Отправка заявок через форму обратной связи
- Ознакомление с вакансиями и отклик на них
- Просмотр контактной информации

### Для администраторов

- Админ-панель Django для управления заявками
- Просмотр и экспорт данных
- Управление контентом через административный интерфейс
- Уведомления о новых заявках в Telegram и на Email

## Страницы сайта

| URL | Описание |
|-----|----------|
| `/` | Главная страница |
| `/service/` | Услуги компании |
| `/team/` | Команда |
| `/contacts/` | Контакты |
| `/calculator/` | Калькулятор услуг |
| `/vacancy/` | Вакансии |
| `/admin/` | Админ-панель |
| `/privacy-policy/` | Политика конфиденциальности |
| `/user-agreement/` | Пользовательское соглашение |

## Модели данных

### Lead (Заявка)

Поля:
- `name` — Имя клиента
- `phone` — Телефон
- `email` — Email (опционально)
- `service` — Выбранная услуга
- `message` — Комментарий
- `status` — Статус заявки (новая, в работе, успешно, отказ)
- `created_at` — Дата создания
- `updated_at` — Дата обновления

### VacancyApplication (Отклик на вакансию)

Поля:
- `name` — Имя соискателя
- `phone` — Телефон
- `email` — Email
- `position` — Должность
- `experience` — Опыт работы
- `created_at` — Дата создания

## Логирование

Логи сохраняются в папку `logs/`:
- `django.log` — Логи Django приложения
- `passenger.log` — Логи Passenger WSGI

## Требования

- Python 3.10+
- Django 4.2
- pip

## Зависимости

Основные пакеты указаны в `requirements.txt`:
- Django>=4.2,<5.0
- requests>=2.31.0
- python-dotenv>=1.0.0
- dj-database-url>=2.1.0
- gunicorn>=21.2.0

