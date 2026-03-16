from django.shortcuts import render


def index(request):
    """Главная страница"""
    return render(request, 'index.html')


def service(request):
    """Страница услуг и тарифов"""
    return render(request, 'service.html')


def contacts(request):
    """Страница контактов"""
    return render(request, 'contacts.html')


def vacancy(request):
    """Страница вакансий"""
    return render(request, 'vacancy.html')


def calculator(request):
    """Страница калькулятора"""
    return render(request, 'calculator.html')


def privacy_policy(request):
    """Политика конфиденциальности"""
    return render(request, 'privacy-policy.html')


def user_agreement(request):
    """Пользовательское соглашение"""
    return render(request, 'polzovatelskoe-soglashenie.html')
