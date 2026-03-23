import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'directsite.settings')
django.setup()

import json
from core.models import Lead, VacancyApplication

# Читаем backup (SQLite)
print("Чтение данных из backup_utf8.json...")
with open('backup_utf8.json', 'r', encoding='utf-8') as f:
    data = json.load(f)

# Переносим Lead
print("\nПеренос заявок (Lead):")
lead_count = 0
for item in data:
    if isinstance(item, dict) and item.get('model') == 'core.lead':
        fields = item['fields']
        Lead.objects.create(
            name=fields['name'],
            phone=fields['phone'],
            email=fields.get('email', ''),
            service=fields.get('service', ''),
            message=fields.get('message', ''),
            status=fields.get('status', 'new'),
        )
        print(f'  ✅ Lead: {fields["name"]}')
        lead_count += 1

# Переносим VacancyApplication
print("\nПеренос откликов (VacancyApplication):")
vacancy_count = 0
for item in data:
    if isinstance(item, dict) and item.get('model') == 'core.vacancyapplication':
        fields = item['fields']
        VacancyApplication.objects.create(
            name=fields['name'],
            phone=fields['phone'],
            email=fields.get('email', ''),
            position=fields.get('position', ''),
            experience=fields.get('experience', ''),
        )
        print(f'  VacancyApplication: {fields["name"]}')
        vacancy_count += 1

print(f'\nПеренос завершён!')
print(f'   Перенесено заявок: {lead_count}')
print(f'   Перенесено откликов: {vacancy_count}')
