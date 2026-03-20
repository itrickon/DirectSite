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

// ИНИЦИАЛИЗАЦИЯ ПРИ ЗАГРУЗКЕ

document.addEventListener('DOMContentLoaded', function() {
    console.log('DirectLine vacancy.js: Скрипты инициализированы');
});
