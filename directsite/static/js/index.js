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
    let current = 0;
    const increment = target / 50;
    const timer = setInterval(() => {
        current += increment;
        if (current >= target) {
            element.textContent = target + suffix;
            clearInterval(timer);
        } else {
            element.textContent = Math.ceil(current) + suffix;
        }
    }, 30);
}

// ИНИЦИАЛИЗАЦИЯ ПРИ ЗАГРУЗКЕ
 
document.addEventListener('DOMContentLoaded', function() {
    // Counter Animation for stats
    const counterObserver = new IntersectionObserver((entries) => {
        entries.forEach(entry => {
            if (entry.isIntersecting) {
                const statNumbers = entry.target.querySelectorAll('.stat-number');
                statNumbers.forEach(num => {
                    const text = num.textContent;
                    const value = parseInt(text.replace(/\D/g, ''));
                    const suffix = text.replace(/[\d]/g, '');
                    num.textContent = '0' + suffix;
                    animateCounter(num, value, suffix);
                });
                counterObserver.unobserve(entry.target);
            }
        });
    }, { threshold: 0.5 });

    const statsSection = document.querySelector('#hero .grid');
    if (statsSection) {
        counterObserver.observe(statsSection);
    }
    
    console.log('DirectLine index.js: Скрипты инициализированы');
});
