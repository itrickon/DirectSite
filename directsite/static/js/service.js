/**
 * DirectLine - Скрипты для страницы услуг
 * Специфичные функции для service.html
 */

// ФУНКЦИЯ ПРОКРУТКИ К ФОРМЕ С ЗАПОЛНЕНИЕМ УСЛУГИ И КОММЕНТАРИЯ

function scrollToContactForm(fullName) {
    // Разбиваем название на услугу и тариф
    // Например: "Лидогенерация - Старт" → услуга: "Лидогенерация", тариф: "Старт"
    // Или: "Лидогенерация + Call-центр - Стандарт" → услуга: "Лидогенерация + Call-центр", тариф: "Стандарт"
    // Или: "Call-центр - Профи" → услуга: "Call-центр", тариф: "Профи"
    
    let serviceName = '';
    let tariffName = '';
    
    // Словарь для приоритетного сопоставления с услугами в форме
    // Важный порядок: сначала более специфичные (с +), потом простые
    const servicePriority = [
        'Лидогенерация + Call-центр',
        'Лидогенерация',
        'Call-центр',
        'Рекрутинг',
        'Лид-КОД',
        'Авито под ключ'
    ];
    
    // Ищем последний дефис для разделения услуги и тарифа
    const lastDashIndex = fullName.lastIndexOf(' - ');
    if (lastDashIndex !== -1) {
        const servicePart = fullName.substring(0, lastDashIndex).trim();
        tariffName = fullName.substring(lastDashIndex + 3).trim();
        
        // Приоритетное сопоставление: ищем точное вхождение услуги
        for (const service of servicePriority) {
            if (servicePart === service) {
                serviceName = service;
                break;
            }
        }
        
        // Если не нашли точное совпадение, ищем частичное
        if (!serviceName) {
            for (const service of servicePriority) {
                if (servicePart.includes(service)) {
                    serviceName = service;
                    break;
                }
            }
        }
        
        // Если всё ещё не нашли, используем как есть
        if (!serviceName) {
            serviceName = servicePart;
        }
    } else {
        // Если дефиса нет, используем полное название как услугу
        serviceName = fullName;
    }

    // Находим форму
    const formSection = document.getElementById('contact');
    if (!formSection) {
        console.error('Форма с id="contact" не найдена');
        return;
    }

    // Прокручиваем к форме
    formSection.scrollIntoView({ behavior: 'smooth', block: 'start' });

    // Выбираем услугу в выпадающем списке
    const serviceSelect = document.querySelector('select[name="service"]');
    if (serviceSelect) {
        // Точное совпадение по значению
        for (let option of serviceSelect.options) {
            if (option.value === serviceName) {
                serviceSelect.value = option.value;
                // Добавляем визуальный эффект
                serviceSelect.style.borderColor = '#d4af37';
                setTimeout(() => {
                    serviceSelect.style.borderColor = '';
                }, 1000);
                break;
            }
        }
    }

    // Заполняем поле комментария тарифом
    const commentField = document.querySelector('textarea[name="message"]');
    if (commentField && tariffName) {
        commentField.value = `Тариф "${tariffName}"`;
        // Добавляем визуальный эффект
        commentField.style.borderColor = '#d4af37';
        setTimeout(() => {
            commentField.style.borderColor = '';
        }, 1000);
    }

    // Фокус на поле имени
    const nameField = document.querySelector('input[name="name"]');
    if (nameField) {
        setTimeout(() => nameField.focus(), 800);
    }
}

// ТАБЫ ДЛЯ ТАРИФОВ

function initServiceTabs() {
    const tabBtns = document.querySelectorAll('.tab-btn');
    const pricingTabs = document.querySelectorAll('.pricing-tabs');

    tabBtns.forEach(btn => {
        btn.addEventListener('click', () => {
            // Убираем active у всех кнопок
            tabBtns.forEach(b => b.classList.remove('active'));
            // Добавляем active нажатой кнопке
            btn.classList.add('active');

            // Получаем целевой таб
            const target = btn.getAttribute('data-tab');
            
            // Скрываем все табы и показываем нужный
            pricingTabs.forEach(tab => {
                if (tab.id === target) {
                    tab.classList.remove('hidden');
                } else {
                    tab.classList.add('hidden');
                }
            });
        });
    });
}

// МОДАЛЬНЫЕ ОКНА
 
function openModal(modalId) {
    const modal = document.getElementById(modalId);
    if (modal) {
        modal.classList.add('active');
        document.body.style.overflow = 'hidden';
    }
}

function closeModal(modalId) {
    const modal = document.getElementById(modalId);
    if (modal) {
        modal.classList.remove('active');
        document.body.style.overflow = '';
    }
}

// Закрытие модального окна при клике вне его
window.addEventListener('click', (e) => {
    if (e.target.classList.contains('modal')) {
        e.target.classList.remove('active');
        document.body.style.overflow = '';
    }
});

// ФОРМАТТЕР ТЕЛЕФОНА
 
function initPhoneFormatter() {
    const phoneInputs = document.querySelectorAll('input[type="tel"]');
    phoneInputs.forEach(input => {
        input.addEventListener('input', (e) => {
            let value = e.target.value.replace(/\D/g, '');
            if (value.length > 11) value = value.substring(0, 11);

            let formatted = '+7';
            if (value.length > 0) formatted += ' (' + value.substring(0, 3);
            if (value.length > 3) formatted += ') ' + value.substring(3, 6);
            if (value.length > 6) formatted += '-' + value.substring(6, 8);
            if (value.length > 8) formatted += '-' + value.substring(8, 10);
            e.target.value = formatted;
        });
    });
}

// АККОРДЕОН
 
function toggleAccordion(header) {
    const item = header.parentElement;
    const isActive = item.classList.contains('active');

    document.querySelectorAll('.accordion-item').forEach(acc => {
        acc.classList.remove('active');
    });

    if (!isActive) {
        item.classList.add('active');
    }
}

// ИНИЦИАЛИЗАЦИЯ ПРИ ЗАГРУЗКЕ

document.addEventListener('DOMContentLoaded', function() {
    initServiceTabs();
    initPhoneFormatter();
    initAvitoButtons();
    console.log('DirectLine service.js: Скрипты инициализированы');
});

// ОБРАБОТЧИК ДЛЯ КНОПОК АВИТО И КОМПЛЕКС

function initAvitoButtons() {
    // Находим все кнопки в секции Авито
    const avitoSection = document.getElementById('avito');
    if (avitoSection) {
        const buttons = avitoSection.querySelectorAll('a[href="#contact"]');
        buttons.forEach(btn => {
            btn.addEventListener('click', (e) => {
                e.preventDefault();
                scrollToContactForm('Авито под ключ');
            });
        });
    }
    
    // Обработчик для кнопки "Комплекс" в карточке услуги
    const complexCards = document.querySelectorAll('.service-card');
    complexCards.forEach(card => {
        if (card.textContent.includes('Комплекс')) {
            const link = card.querySelector('a[href="#contact"]');
            if (link) {
                link.addEventListener('click', (e) => {
                    e.preventDefault();
                    scrollToContactForm('Комплекс');
                });
            }
        }
    });
}
