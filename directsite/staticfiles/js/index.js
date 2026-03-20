/**
 * DirectLine - Скрипты для главной страницы
 * Специфичные функции для index.html
 */

// МНОГОШАГОВАЯ ФОРМА

let currentStep = 1;
const totalSteps = 3;

function nextStep() {
    const currentStepElement = document.getElementById(`step${currentStep}`);
    const inputs = currentStepElement.querySelectorAll('input[required]');
    let isValid = true;

    inputs.forEach(input => {
        if (!input.value.trim()) {
            isValid = false;
            input.classList.add('border-red-500');
        } else {
            input.classList.remove('border-red-500');
        }
    });

    if (!isValid) return;

    document.getElementById(`step${currentStep}`).classList.add('hidden');
    currentStep++;

    if (currentStep <= totalSteps) {
        document.getElementById(`step${currentStep}`).classList.remove('hidden');
        updateProgressBar();
        updateStepIndicators();
    }
}

function updateProgressBar() {
    const progress = ((currentStep - 1) / totalSteps) * 100;
    document.getElementById('progressFill').style.width = `${progress}%`;
}

function updateStepIndicators() {
    for (let i = 1; i <= totalSteps; i++) {
        const indicator = document.getElementById(`step${i}Indicator`);
        if (i < currentStep) {
            indicator.classList.add('completed');
            indicator.classList.remove('active');
        } else if (i === currentStep) {
            indicator.classList.add('active');
            indicator.classList.remove('completed');
        } else {
            indicator.classList.remove('active', 'completed');
        }
    }
}

function submitForm() {
    document.getElementById(`step${currentStep}`).classList.add('hidden');
    document.getElementById('successStep').classList.remove('hidden');
    document.getElementById('progressFill').style.width = '100%';
    document.getElementById('step3Indicator').classList.add('completed');
    document.getElementById('step3Indicator').classList.remove('active');
}
 
// АНИМАЦИЯ ЧИСЕЛ

function animateCounter(element, target, suffix = '') {
    const duration = 1000; // 1 секунда
    const startTime = performance.now();
    
    function animate(currentTime) {
        const elapsed = currentTime - startTime;
        const progress = Math.min(elapsed / duration, 1);
        
        // Easing function (ease-out)
        const easeProgress = 1 - Math.pow(1 - progress, 3);
        const current = Math.floor(target * easeProgress);
        
        element.textContent = current + suffix;
        
        if (progress < 1) {
            requestAnimationFrame(animate);
        } else {
            element.textContent = target + suffix;
        }
    }
    
    requestAnimationFrame(animate);
}

// ИНИЦИАЛИЗАЦИЯ ПРИ ЗАГРУЗКЕ

document.addEventListener('DOMContentLoaded', function() {
    // Counter Animation for stats - запускаем сразу для всех элементов
    const statNumbers = document.querySelectorAll('.stat-number');

    statNumbers.forEach(num => {
        const value = parseInt(num.getAttribute('data-value') || num.textContent.replace(/\D/g, ''), 10);
        const suffix = num.getAttribute('data-suffix') || num.textContent.replace(/[\d]/g, '').trim();
        // Устанавливаем начальное значение
        num.textContent = '0' + suffix;
        // Запускаем анимацию с небольшой задержкой для каждого элемента
        setTimeout(() => {
            animateCounter(num, value, suffix);
        }, parseInt(num.getAttribute('data-delay') || '0', 10));
    });

    // Фиксация позиции Floating Action Button на мобильных
    const floatingBtn = document.getElementById('floatingContactBtn') || document.querySelector('.floating-contact-btn');
    if (floatingBtn) {
        // Принудительно устанавливаем стили после загрузки
        floatingBtn.style.setProperty('position', 'fixed', 'important');
        floatingBtn.style.setProperty('bottom', '24px', 'important');
        floatingBtn.style.setProperty('right', '20px', 'important');
        floatingBtn.style.setProperty('z-index', '99', 'important');
        
        // Исправляем позицию при изменении размера окна
        let resizeTimeout;
        window.addEventListener('resize', function() {
            clearTimeout(resizeTimeout);
            resizeTimeout = setTimeout(function() {
                floatingBtn.style.setProperty('bottom', '24px', 'important');
                floatingBtn.style.setProperty('right', '20px', 'important');
            }, 100);
        });
    }

    console.log('DirectLine index.js: Скрипты инициализированы');
});
