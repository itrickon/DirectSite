from django import forms
from .models import Lead, VacancyApplication


class LeadForm(forms.ModelForm):
    """Форма заявки от клиента"""
    class Meta:
        model = Lead
        fields = ['name', 'phone', 'email', 'service', 'message']
        widgets = {
            'name': forms.TextInput(attrs={
                'class': 'form-input',
                'placeholder': 'Ваше имя',
                'required': True,
            }),
            'phone': forms.TextInput(attrs={
                'class': 'form-input',
                'placeholder': '+7 (999) 999-99-99',
                'required': True,
            }),
            'email': forms.EmailInput(attrs={
                'class': 'form-input',
                'placeholder': 'example@mail.ru',
            }),
            'service': forms.Select(attrs={
                'class': 'form-input',
            }),
            'message': forms.Textarea(attrs={
                'class': 'form-input',
                'placeholder': 'Дополнительная информация',
                'rows': 3,
            }),
        }


class VacancyApplicationForm(forms.ModelForm):
    """Форма отклика на вакансию"""
    class Meta:
        model = VacancyApplication
        fields = ['name', 'phone', 'email', 'position', 'experience']
        widgets = {
            'name': forms.TextInput(attrs={
                'class': 'form-input',
                'placeholder': 'Иван Иванов',
                'required': True,
            }),
            'phone': forms.TextInput(attrs={
                'class': 'form-input',
                'placeholder': '+7 (999) 999-99-99',
                'required': True,
            }),
            'email': forms.EmailInput(attrs={
                'class': 'form-input',
                'placeholder': 'example@mail.ru',
            }),
            'position': forms.Select(attrs={
                'class': 'form-input',
                'required': True,
            }),
            'experience': forms.Textarea(attrs={
                'class': 'form-input',
                'placeholder': 'Расскажите о вашем опыте работы...',
                'rows': 3,
            }),
        }
