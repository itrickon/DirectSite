/**
 * DirectLine - Скрипты для страницы вакансий
 * Специфичные функции для vacancy.html
 */

// ФУНКЦИЯ ПРОКРУТКИ К ФОРМЕ С ВЫБОРОМ ВАКАНСИИ

function selectVacancy(vacancyName) {
    // Находим форму
    const formSection = document.getElementById('apply');
    if (!formSection) {
        console.error('Форма с id="apply" не найдена');
        return;
    }

    // Прокручиваем к форме
    formSection.scrollIntoView({ behavior: 'smooth', block: 'start' });

    // Выбираем вакансию в выпадающем списке
    const vacancySelect = document.querySelector('select[name="position"]');
    if (vacancySelect) {
        // Точное совпадение по значению
        for (let option of vacancySelect.options) {
            if (option.value === vacancyName) {
                vacancySelect.value = option.value;
                // Добавляем визуальный эффект
                vacancySelect.style.borderColor = '#d4af37';
                setTimeout(() => {
                    vacancySelect.style.borderColor = '';
                }, 1000);
                break;
            }
        }
    }

    // Фокус на поле имени
    const nameField = document.querySelector('input[name="name"]');
    if (nameField) {
        setTimeout(() => nameField.focus(), 800);
    }
    
    // Предотвращаем переход по ссылке
    return false;
}

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

// ИНИЦИАЛИЗАЦИЯ ПРИ ЗАГРУЗКЕ

document.addEventListener('DOMContentLoaded', function() {
    initPhoneFormatter();
    console.log('DirectLine vacancy.js: Скрипты инициализированы');
});
