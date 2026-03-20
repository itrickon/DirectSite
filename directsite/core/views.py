import requests
from django.shortcuts import render, redirect
from django.http import JsonResponse
from django.contrib import messages
from .models import Lead, VacancyApplication
from .forms import LeadForm, VacancyApplicationForm
from directsite.telegram_config import TELEGRAM_BOT_TOKEN, TELEGRAM_CHAT_ID


def send_to_telegram(message: str) -> bool:
    """Отправляет сообщение в Telegram"""
    try:
        url = f'https://api.telegram.org/bot{TELEGRAM_BOT_TOKEN}/sendMessage'
        data = {
            'chat_id': TELEGRAM_CHAT_ID,
            'text': message,
            'parse_mode': 'HTML'
        }
        print(f"=== Отправка в Telegram ===")
        print(f"URL: {url}")
        print(f"Chat ID: {TELEGRAM_CHAT_ID}")
        print(f"Токен (первые 10 символов): {TELEGRAM_BOT_TOKEN[:10]}...")
        
        # Прокси для России (если нужно)
        proxies = {
            'http': 'http://proxy:port',
            'https': 'http://proxy:port',
        }
        
        response = requests.post(url, data=data, timeout=10)  # , proxies=proxies
        print(f"Status code: {response.status_code}")
        print(f"Response: {response.text}")
        
        if response.status_code == 200:
            print("Успешно отправлено!")
            return True
        else:
            print(f"Ошибка: {response.status_code}")
            return False
    except requests.exceptions.Timeout as e:
        print(f"Таймаут: {e}")
        print("Возможно, Telegram заблокиирован. Настройте прокси.")
        return False
    except requests.exceptions.ConnectionError as e:
        print(f"Ошибка соединения: {e}")
        print("Проверьте интернет или настройте прокси.")
        return False
    except Exception as e:
        print(f"Исключение: {e}")
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
