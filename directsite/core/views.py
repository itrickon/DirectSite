import logging
import requests
from django.shortcuts import render, redirect
from django.http import JsonResponse
from django.contrib import messages
from django.core.mail import send_mail, EmailMultiAlternatives
from django.conf import settings
from .models import Lead, VacancyApplication
from .forms import LeadForm, VacancyApplicationForm

# Импорт из переменных окружения (для Render)
TELEGRAM_BOT_TOKEN = settings.TELEGRAM_BOT_TOKEN
TELEGRAM_CHAT_ID = settings.TELEGRAM_CHAT_ID

logger = logging.getLogger('core')


def send_to_telegram(message: str) -> bool:
    """Отправляет сообщение в Telegram"""
    try:
        url = f'https://api.telegram.org/bot{TELEGRAM_BOT_TOKEN}/sendMessage'
        data = {
            'chat_id': TELEGRAM_CHAT_ID,
            'text': message,
            'parse_mode': 'HTML'
        }
        logger.info("=== Отправка в Telegram ===")
        logger.info(f"Chat ID: {TELEGRAM_CHAT_ID}")

        # Прокси для обхода блокировки Telegram в России
        # Формат: http://логин:пароль@ip:port
        proxies = {
            'http': 'http://KPsDQN:ySWMcT@190.111.161.74:9658',
            'https': 'http://KPsDQN:ySWMcT@190.111.161.74:9658',
        }

        response = requests.post(url, data=data, timeout=10, proxies=proxies)
        logger.info(f"Status code: {response.status_code}")

        if response.status_code == 200:
            logger.info("Успешно отправлено!")
            return True
        else:
            logger.warning(f"Ошибка Telegram API: {response.status_code} - {response.text}")
            return False
    except requests.exceptions.Timeout as e:
        logger.error(f"Таймаут при отправке в Telegram: {e}")
        return False
    except requests.exceptions.ConnectionError as e:
        logger.error(f"Ошибка соединения с Telegram: {e}")
        return False
    except Exception as e:
        logger.error(f"Неожиданная ошибка при отправке в Telegram: {e}")
        return False


def send_email_notification(lead_or_application) -> bool:
    """Отправляет уведомление на email"""
    try:
        if isinstance(lead_or_application, Lead):
            subject = f"Новая заявка от {lead_or_application.name}"
            message = f"""
Получена новая заявка с сайта!

Имя: {lead_or_application.name}
Телефон: {lead_or_application.phone}
Email: {lead_or_application.email or 'Не указан'}
Услуга: {lead_or_application.get_service_display()}
Комментарий: {lead_or_application.message or 'Не указан'}
Дата: {lead_or_application.created_at.strftime('%d.%m.%Y %H:%M')}
            """.strip()
        else:
            subject = f"Отклик на вакансию от {lead_or_application.name}"
            message = f"""
Получен новый отклик на вакансию!

Имя: {lead_or_application.name}
Телефон: {lead_or_application.phone}
Email: {lead_or_application.email or 'Не указан'}
Вакансия: {lead_or_application.position}
Опыт: {lead_or_application.experience or 'Не указан'}
Дата: {lead_or_application.created_at.strftime('%d.%m.%Y %H:%M')}
            """.strip()

        send_mail(
            subject,
            message,
            settings.DEFAULT_FROM_EMAIL,
            [settings.ADMIN_EMAIL],
            fail_silently=False,
        )
        logger.info(f"Email отправлен на {settings.ADMIN_EMAIL}")
        return True
    except Exception as e:
        logger.error(f"Ошибка при отправке email: {e}")
        return False


def index(request):
    """Главная страница"""
    if request.method == 'POST':
        form = LeadForm(request.POST)
        if form.is_valid():
            lead = form.save()

            # Отправляем в Telegram
            message = f"""
<b>Новая заявка с сайта!</b>

<b>Имя:</b> {lead.name}
<b>Телефон:</b> {lead.phone}
<b>Email:</b> {lead.email or 'Не указан'}
<b>Услуга:</b> {lead.get_service_display()}
<b>Комментарий:</b> {lead.message or 'Не указан'}

<b>Дата:</b> {lead.created_at.strftime('%d.%m.%Y %H:%M')}
            """.strip()

            send_to_telegram(message)
            
            # Отправляем email уведомление
            send_email_notification(lead)

            if request.headers.get('X-Requested-With') == 'XMLHttpRequest':
                return JsonResponse({'success': True, 'message': 'Заявка успешно отправлена!'})
            messages.success(request, 'Заявка успешно отправлена!')
            return redirect('index')
        else:
            if request.headers.get('X-Requested-With') == 'XMLHttpRequest':
                return JsonResponse({'success': False, 'errors': form.errors}, status=400)
            messages.error(request, 'Ошибка при отправке заявки.')
    else:
        form = LeadForm()
    return render(request, 'index.html', {'form': form})


def service(request):
    """Страница услуг"""
    if request.method == 'POST':
        form = LeadForm(request.POST)
        if form.is_valid():
            lead = form.save()

            # Отправляем в Telegram
            message = f"""
<b>Новая заявка с сайта!</b>

<b>Имя:</b> {lead.name}
<b>Телефон:</b> {lead.phone}
<b>Email:</b> {lead.email or 'Не указан'}
<b>Услуга:</b> {lead.get_service_display()}
<b>Комментарий:</b> {lead.message or 'Не указан'}

<b>Дата:</b> {lead.created_at.strftime('%d.%m.%Y %H:%M')}
            """.strip()

            send_to_telegram(message)
            
            # Отправляем email уведомление
            send_email_notification(lead)

            if request.headers.get('X-Requested-With') == 'XMLHttpRequest':
                return JsonResponse({'success': True, 'message': 'Заявка успешно отправлена!'})
            messages.success(request, 'Заявка успешно отправлена!')
            return redirect('service')
        else:
            if request.headers.get('X-Requested-With') == 'XMLHttpRequest':
                return JsonResponse({'success': False, 'errors': form.errors}, status=400)
            messages.error(request, 'Ошибка при отправке заявки.')
    else:
        form = LeadForm()
    return render(request, 'service.html', {'form': form})


def contacts(request):
    """Страница контактов"""
    if request.method == 'POST':
        form = LeadForm(request.POST)
        if form.is_valid():
            lead = form.save()

            # Отправляем в Telegram
            message = f"""
<b>Новая заявка с сайта!</b>

<b>Имя:</b> {lead.name}
<b>Телефон:</b> {lead.phone}
<b>Email:</b> {lead.email or 'Не указан'}
<b>Услуга:</b> {lead.get_service_display()}
<b>Комментарий:</b> {lead.message or 'Не указан'}

<b>Дата:</b> {lead.created_at.strftime('%d.%m.%Y %H:%M')}
            """.strip()

            send_to_telegram(message)
            
            # Отправляем email уведомление
            send_email_notification(lead)

            if request.headers.get('X-Requested-With') == 'XMLHttpRequest':
                return JsonResponse({'success': True, 'message': 'Заявка успешно отправлена!'})
            messages.success(request, 'Заявка успешно отправлена!')
            return redirect('contacts')
        else:
            if request.headers.get('X-Requested-With') == 'XMLHttpRequest':
                return JsonResponse({'success': False, 'errors': form.errors}, status=400)
            messages.error(request, 'Ошибка при отправке заявки.')
    else:
        form = LeadForm()
    return render(request, 'contacts.html', {'form': form})


def vacancy(request):
    """Страница вакансий"""
    if request.method == 'POST':
        form = VacancyApplicationForm(request.POST)
        if form.is_valid():
            app = form.save()

            # Отправляем в Telegram
            message = f"""
<b>Новый отклик на вакансию!</b>

<b>Имя:</b> {app.name}
<b>Телефон:</b> {app.phone}
<b>Email:</b> {app.email or 'Не указан'}
<b>Вакансия:</b> {app.position}
<b>Опыт:</b> {app.experience or 'Не указан'}

<b>Дата:</b> {app.created_at.strftime('%d.%m.%Y %H:%M')}
            """.strip()

            send_to_telegram(message)
            
            # Отправляем email уведомление
            send_email_notification(app)

            if request.headers.get('X-Requested-With') == 'XMLHttpRequest':
                return JsonResponse({'success': True, 'message': 'Отклик успешно отправлен!'})
            messages.success(request, 'Отклик успешно отправлен!')
            return redirect('vacancy')
        else:
            if request.headers.get('X-Requested-With') == 'XMLHttpRequest':
                return JsonResponse({'success': False, 'errors': form.errors}, status=400)
            messages.error(request, 'Ошибка при отправке отклика.')
    else:
        form = VacancyApplicationForm()
    return render(request, 'vacancy.html', {'form': form})


def calculator(request):
    """Страница калькулятора"""
    return render(request, 'calculator.html')


def team(request):
    """Страница команды"""
    return render(request, 'team.html')


def privacy_policy(request):
    """Политика конфиденциальности"""
    return render(request, 'privacy-policy.html')


def user_agreement(request):
    """Пользовательское соглашение"""
    return render(request, 'polzovatelskoe-soglashenie.html')
