/**
 * DirectLine - Скрипты для страницы услуг
 * Специфичные функции для service.html
 */

// ТАБЫ ДЛЯ ТАРИФОВ
 
function initServiceTabs() {
    const tabBtns = document.querySelectorAll('.tab-btn');
    const pricingTabs = document.querySelectorAll('.pricing-tabs');

    tabBtns.forEach(btn => {
        btn.addEventListener('click', () => {
            tabBtns.forEach(b => b.classList.remove('active'));
            btn.classList.add('active');

            const target = btn.getAttribute('data-tab');
            pricingTabs.forEach(tab => {
                tab.classList.remove('active');
                if (tab.id === target) {
                    tab.classList.add('active');
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
    console.log('DirectLine service.js: Скрипты инициализированы');
});
