import os

templates_dir = r'c:\Users\Honor\Desktop\GitHub Doc\DirectSite\directsite\templates'

# Список файлов (кроме index.html и contacts.html)
# contacts.html не нужна кнопка "Связаться", так как это страница контактов
files = ['service.html', 'vacancy.html', 'team.html', 'calculator.html']

for filename in files:
    filepath = os.path.join(templates_dir, filename)
    if not os.path.exists(filepath):
        continue
    
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Находим ссылку на Контакты и заменяем на кнопку Связаться
    old_link = '<a href="{% url \'contacts\' %}" class="nav-link text-gray-300 hover:text-gold-500 text-sm font-medium">Контакты</a>'
    new_btn = '<a href="{% url \'contacts\' %}" class="btn-gold px-6 py-2.5 text-sm font-bold uppercase tracking-widest rounded-sm">Связаться</a>'
    
    content = content.replace(old_link, new_btn)
    
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(content)
    
    print(f"✓ {filename} обновлён")

print("\nГотово! Кнопка 'Связаться' добавлена в навигацию")
