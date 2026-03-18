from django.shortcuts import render, redirect
from django.http import JsonResponse
from django.views.decorators.http import require_POST
from django.contrib import messages
from .models import Lead, VacancyApplication
from .forms import LeadForm, VacancyApplicationForm


def index(request):
    """Главная страница"""
    if request.method == 'POST':
        form = LeadForm(request.POST)
        if form.is_valid():
            form.save()
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
            form.save()
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
            form.save()
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
            form.save()
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


def privacy_policy(request):
    """Политика конфиденциальности"""
    return render(request, 'privacy-policy.html')


def user_agreement(request):
    """Пользовательское соглашение"""
    return render(request, 'polzovatelskoe-soglashenie.html')
