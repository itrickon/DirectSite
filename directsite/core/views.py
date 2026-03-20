import requests
from django.shortcuts import render, redirect
from django.http import JsonResponse
from django.contrib import messages
from .models import Lead, VacancyApplication
from .forms import LeadForm, VacancyApplicationForm


def send_to_bitrix24(data: dict, deal_type: str = 'vacancy') -> bool:
    """
    Отправляет данные в Битрикс24 через вебхук
    
    Args:
        data: Словарь с данными заявки
        deal_type: Тип заявки ('vacancy' или 'lead')
    
    Returns:
        bool: True если успешно
    """
    # TODO: Вставьте ваш URL вебхука Битрикс24
    BITRIX24_WEBHOOK = 'ВАШ_URL_ВЕБХУКА'  # Например: https://your-company.bitrix24.ru/rest/1/xxxxx/
    
    if BITRIX24_WEBHOOK == 'ВАШ_URL_ВЕБХУКА':
        print("⚠️ Битрикс24 вебхук не настроен! Заявка сохранена только в базе.")
        return False
    
    try:
        # Формируем данные для сделки/лида
        if deal_type == 'vacancy':
            fields = {
                'fields': {
                    'TITLE': f"Отклик на вакансию: {data.get('position', 'Не указано')}",
                    'NAME': data.get('name', ''),
                    'PHONE': [{'VALUE': data.get('phone', ''), 'VALUE_TYPE': 'WORK'}],
                    'EMAIL': [{'VALUE': data.get('email', ''), 'VALUE_TYPE': 'WORK'}],
                    'COMMENTS': f"Вакансия: {data.get('position', '')}\nОпыт: {data.get('experience', '')}",
                    'SOURCE_ID': 'WEBSITE',
                    'STATUS_ID': 'NEW',
                    'OPENED': 'Y'
                }
            }
        else:  # lead
            fields = {
                'fields': {
                    'TITLE': f"Заявка с сайта: {data.get('name', '')}",
                    'NAME': data.get('name', ''),
                    'PHONE': [{'VALUE': data.get('phone', ''), 'VALUE_TYPE': 'WORK'}],
                    'EMAIL': [{'VALUE': data.get('email', ''), 'VALUE_TYPE': 'WORK'}],
                    'COMMENTS': f"Услуга: {data.get('service', '')}\nСообщение: {data.get('message', '')}",
                    'SOURCE_ID': 'WEBSITE',
                    'STATUS_ID': 'NEW',
                    'OPENED': 'Y'
                }
            }
        
        # Отправляем в Битрикс24 (создание лида)
        url = f"{BITRIX24_WEBHOOK}crm.lead.add"
        response = requests.post(url, json=fields, timeout=30)
        result = response.json()
        
        if result.get('result'):
            print(f"✅ Заявка отправлена в Битрикс24 (ID: {result['result']})")
            return True
        else:
            print(f"❌ Ошибка Битрикс24: {result}")
            return False
            
    except requests.exceptions.Timeout:
        print("⚠️ Таймаут при отправке в Битрикс24")
        return False
    except Exception as e:
        print(f"⚠️ Ошибка отправки в Битрикс24: {e}")
        return False


def index(request):
    """Главная страница"""
    if request.method == 'POST':
        form = LeadForm(request.POST)
        if form.is_valid():
            lead = form.save()
            
            # Отправляем в Битрикс24
            send_to_bitrix24({
                'name': lead.name,
                'phone': lead.phone,
                'email': lead.email,
                'service': lead.get_service_display(),
                'message': lead.message
            }, deal_type='lead')
            
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
    """Страница услуг и тарифов"""
    if request.method == 'POST':
        form = LeadForm(request.POST)
        if form.is_valid():
            lead = form.save()
            
            # Отправляем в Битрикс24
            send_to_bitrix24({
                'name': lead.name,
                'phone': lead.phone,
                'email': lead.email,
                'service': lead.get_service_display(),
                'message': lead.message
            }, deal_type='lead')
            
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
            
            # Отправляем в Битрикс24
            send_to_bitrix24({
                'name': lead.name,
                'phone': lead.phone,
                'email': lead.email,
                'service': lead.get_service_display(),
                'message': lead.message
            }, deal_type='lead')
            
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
            application = form.save()

            # Отправляем в Битрикс24
            send_to_bitrix24({
                'name': application.name,
                'phone': application.phone,
                'email': application.email,
                'position': application.position,
                'experience': application.experience
            }, deal_type='vacancy')

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
