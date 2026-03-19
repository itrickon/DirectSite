/**
 * DirectLine - Основные JavaScript функции
 * Маркетинговое IT-агентство
 */

// ПРЕЛОАДЕР

function initPreloader() {
    const preloader = document.getElementById('preloader');
    if (preloader) {
        window.addEventListener('load', () => {
            setTimeout(() => {
                preloader.classList.add('hidden');
            }, 500);
        });
    }
}

// МОБИЛЬНОЕ МЕНЮ

function toggleMobileMenu() {
    const mobileMenu = document.getElementById('mobileMenu');
    if (mobileMenu) {
        mobileMenu.classList.toggle('active');
    }
}

// НАВИГАЦИЯ
 
function initNavbar() {
    const navbar = document.getElementById('navbar');
    if (navbar) {
        let lastScroll = 0;
        
        window.addEventListener('scroll', () => {
            const currentScroll = window.pageYOffset;
            
            if (currentScroll > 100) {
                navbar.classList.add('scrolled');
            } else {
                navbar.classList.remove('scrolled');
            }
            
            lastScroll = currentScroll;
        });
    }
}

// АНИМАЦИЯ ПРИ ПРОКРУТКЕ

function initScrollAnimations() {
    const fadeElements = document.querySelectorAll('.fade-in, .fade-in-left, .fade-in-right');
    
    if (fadeElements.length === 0) return;
    
    const observerOptions = {
        threshold: 0.1,
        rootMargin: '0px 0px -50px 0px'
    };
    
    const observer = new IntersectionObserver((entries) => {
        entries.forEach(entry => {
            if (entry.isIntersecting) {
                entry.target.classList.add('visible');
                observer.unobserve(entry.target);
            }
        });
    }, observerOptions);
    
    fadeElements.forEach(el => observer.observe(el));
}

// КНОПКА НАВЕРХ

function initBackToTop() {
    const backToTop = document.querySelector('.back-to-top');
    if (!backToTop) return;
    
    window.addEventListener('scroll', () => {
        if (window.pageYOffset > 300) {
            backToTop.classList.add('visible');
        } else {
            backToTop.classList.remove('visible');
        }
    });
    
    backToTop.addEventListener('click', (e) => {
        e.preventDefault();
        window.scrollTo({
            top: 0,
            behavior: 'smooth'
        });
    });
}


// ПЛАВНЫЙ СКРОЛЛ К ЯКОРЯМ

function initSmoothScroll() {
    document.querySelectorAll('a[href^="#"]').forEach(anchor => {
        anchor.addEventListener('click', function (e) {
            const href = this.getAttribute('href');
            if (href === '#' || href === '') return;
            
            const target = document.querySelector(href);
            if (target) {
                e.preventDefault();
                target.scrollIntoView({
                    behavior: 'smooth',
                    block: 'start'
                });
            }
        });
    });
}

// CSRF TOKEN
function getCookie(name) {
    let cookieValue = null;
    if (document.cookie && document.cookie !== '') {
        const cookies = document.cookie.split(';');
        for (let i = 0; i < cookies.length; i++) {
            const cookie = cookies[i].trim();
            if (cookie.substring(0, name.length + 1) === (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}

// ФОРМА ОБРАТНОЙ СВЯЗИ

function initContactForm() {
    const forms = document.querySelectorAll('#contactForm, #vacancyForm');
    
    forms.forEach(form => {
        if (!form) return;

        form.addEventListener('submit', async function(e) {
            e.preventDefault();

            const submitBtn = form.querySelector('button[type="submit"]');
            const originalText = submitBtn ? submitBtn.innerHTML : '';
            
            // Блокируем кнопку
            if (submitBtn) {
                submitBtn.disabled = true;
                submitBtn.innerHTML = '<i class="fas fa-spinner fa-spin"></i> Отправка...';
            }

            const formData = new FormData(form);
            const csrftoken = getCookie('csrftoken');

            try {
                const response = await fetch(window.location.href, {
                    method: 'POST',
                    headers: {
                        'X-Requested-With': 'XMLHttpRequest',
                        'X-CSRFToken': csrftoken,
                    },
                    body: formData,
                });

                const data = await response.json();

                if (response.ok && data.success) {
                    // Показываем сообщение об успехе
                    showNotification(data.message, 'success');
                    form.reset();
                    
                    // Если есть шаг успеха (для multi-step формы)
                    const successStep = document.getElementById('successStep');
                    if (successStep) {
                        document.querySelectorAll('.step').forEach(step => step.classList.add('hidden'));
                        successStep.classList.remove('hidden');
                    }
                } else {
                    showNotification('Ошибка при отправке. Проверьте правильность заполнения полей.', 'error');
                    if (data.errors) {
                        Object.keys(data.errors).forEach(field => {
                            const fieldElement = form.querySelector(`[name="${field}"]`);
                            if (fieldElement) {
                                fieldElement.classList.add('border-red-500');
                            }
                        });
                    }
                }
            } catch (error) {
                console.error('Error:', error);
                showNotification('Произошла ошибка. Попробуйте позже.', 'error');
            } finally {
                // Разблокируем кнопку
                if (submitBtn) {
                    submitBtn.disabled = false;
                    submitBtn.innerHTML = originalText;
                }
            }
        });
    });
}

// Уведомления
function showNotification(message, type = 'success') {
    const notification = document.createElement('div');
    notification.className = `fixed top-24 right-6 z-50 px-6 py-4 rounded-sm shadow-lg transform transition-all duration-300 translate-x-full ${
        type === 'success' ? 'bg-green-600' : 'bg-red-600'
    } text-white`;
    notification.innerHTML = `
        <div class="flex items-center gap-3">
            <i class="fas ${type === 'success' ? 'fa-check-circle' : 'fa-exclamation-circle'}"></i>
            <span>${message}</span>
        </div>
    `;
    
    document.body.appendChild(notification);
    
    // Анимация появления
    setTimeout(() => {
        notification.classList.remove('translate-x-full');
    }, 100);
    
    // Удаление через 5 секунд
    setTimeout(() => {
        notification.classList.add('translate-x-full');
        setTimeout(() => notification.remove(), 300);
    }, 5000);
}

function resetForm() {
    const forms = document.querySelectorAll('#contactForm, #vacancyForm');
    
    forms.forEach(form => {
        if (form) {
            form.reset();
            // Сброс multi-step формы
            document.querySelectorAll('.step').forEach(step => {
                step.classList.add('hidden');
            });
            const step1 = document.getElementById('step1');
            if (step1) {
                step1.classList.remove('hidden');
            }
        }
    });
}

// КАЛЬКУЛЯТОР

function initCalculator() {
    // Синхронизация input и range
    function syncInputs(numberId, rangeId) {
        const numberInput = document.getElementById(numberId);
        const rangeInput = document.getElementById(rangeId);

        if (numberInput && rangeInput) {
            rangeInput.addEventListener('input', () => {
                numberInput.value = rangeInput.value;
            });

            numberInput.addEventListener('input', () => {
                rangeInput.value = numberInput.value;
            });
        }
    }

    syncInputs('clientsCount', 'clientsCountRange');
    syncInputs('averageCheck', 'averageCheckRange');
    syncInputs('conversionRate', 'conversionRateRange');
    syncInputs('growthRate', 'growthRateRange');

    // Функция расчета
    function calculateProfit() {
        const clientsCount = parseFloat(document.getElementById('clientsCount').value) || 0;
        const averageCheck = parseFloat(document.getElementById('averageCheck').value) || 0;
        const conversionRate = parseFloat(document.getElementById('conversionRate').value) || 0;
        const growthRate = parseFloat(document.getElementById('growthRate').value) || 0;

        console.log('Input values:', { clientsCount, averageCheck, conversionRate, growthRate });

        // Текущая выручка
        const currentRevenue = clientsCount * averageCheck;

        // Новые клиенты
        const newClients = Math.round(clientsCount * (growthRate / 100));

        // Дополнительная выручка
        const additionalRevenue = newClients * averageCheck;

        // Итоговая выручка
        const totalRevenue = currentRevenue + additionalRevenue;

        // Форматирование чисел
        const formatNumber = (num) => {
            return num.toLocaleString('ru-RU');
        };

        const formatCurrency = (num) => {
            return num.toLocaleString('ru-RU') + ' ₽';
        };

        // Отображение результатов
        const currentRevenueEl = document.getElementById('currentRevenue');
        const newClientsEl = document.getElementById('newClients');
        const additionalRevenueEl = document.getElementById('additionalRevenue');
        const totalRevenueEl = document.getElementById('totalRevenue');
        const resultsEl = document.getElementById('results');

        if (currentRevenueEl && newClientsEl && additionalRevenueEl && totalRevenueEl && resultsEl) {
            currentRevenueEl.textContent = formatCurrency(currentRevenue);
            newClientsEl.textContent = formatNumber(newClients);
            additionalRevenueEl.textContent = formatCurrency(additionalRevenue);
            totalRevenueEl.textContent = formatCurrency(totalRevenue);

            // Показываем результаты
            resultsEl.classList.remove('hidden');

            // Плавный скролл к результатам
            setTimeout(() => {
                resultsEl.scrollIntoView({
                    behavior: 'smooth',
                    block: 'start'
                });
            }, 100);
        }
    }

    // Расчет по кнопке
    const calculateBtn = document.getElementById('calculateBtn');
    if (calculateBtn) {
        calculateBtn.addEventListener('click', calculateProfit);
    }
}

// АККОРДЕОН

function initAccordion() {
    const accordionItems = document.querySelectorAll('.accordion-item');
    
    accordionItems.forEach(item => {
        const header = item.querySelector('.accordion-header');
        if (!header) return;
        
        header.addEventListener('click', () => {
            const isActive = item.classList.contains('active');
            
            // Закрываем все остальные
            accordionItems.forEach(otherItem => {
                if (otherItem !== item) {
                    otherItem.classList.remove('active');
                }
            });
            
            // Переключаем текущий
            item.classList.toggle('active');
        });
    });
}

// ТАБЫ

function initTabs() {
    const tabButtons = document.querySelectorAll('.tab-btn');
    
    tabButtons.forEach(btn => {
        btn.addEventListener('click', () => {
            const tabGroup = btn.getAttribute('data-tab-group');
            const tabTarget = btn.getAttribute('data-tab');
            
            if (!tabGroup || !tabTarget) return;
            
            // Удаляем активный класс у всех кнопок в группе
            document.querySelectorAll(`.tab-btn[data-tab-group="${tabGroup}"]`).forEach(b => {
                b.classList.remove('active');
            });
            
            // Скрываем все табы
            document.querySelectorAll(`[data-tab-content="${tabGroup}"]`).forEach(content => {
                content.classList.remove('active');
            });
            
            // Активируем текущий
            btn.classList.add('active');
            const targetContent = document.querySelector(`[data-tab-content="${tabTarget}"]`);
            if (targetContent) {
                targetContent.classList.add('active');
            }
        });
    });
}

// АНИМАЦИЯ ЧИСЕЛ

function animateNumber(element, target, suffix = '', duration = 1000) {
    const startTime = performance.now();
    
    function animate(currentTime) {
        const elapsed = currentTime - startTime;
        const progress = Math.min(elapsed / duration, 1);
        
        // Easing function (ease-out)
        const easeProgress = 1 - Math.pow(1 - progress, 3);
        const current = Math.floor(target * easeProgress);
        
        element.textContent = current.toLocaleString('ru-RU') + suffix;
        
        if (progress < 1) {
            requestAnimationFrame(animate);
        } else {
            element.textContent = target.toLocaleString('ru-RU') + suffix;
        }
    }
    
    requestAnimationFrame(animate);
}

function initStatsAnimation() {
    const statNumbers = document.querySelectorAll('.stat-number');
    if (statNumbers.length === 0) return;

    const observer = new IntersectionObserver((entries) => {
        entries.forEach(entry => {
            if (entry.isIntersecting) {
                const text = entry.target.textContent.trim();
                const target = parseInt(text.replace(/\D/g, ''), 10);
                const suffix = text.replace(/[\d]/g, '').trim();
                animateNumber(entry.target, target, suffix);
                observer.unobserve(entry.target);
            }
        });
    }, { threshold: 0.5 });

    statNumbers.forEach(stat => observer.observe(stat));
}
 
// ИНИЦИАЛИЗАЦИЯ ПРИ ЗАГРУЗКЕ
 
document.addEventListener('DOMContentLoaded', function() {
    initPreloader();
    initNavbar();
    initScrollAnimations();
    initBackToTop();
    initSmoothScroll();
    initContactForm();
    initAccordion();
    initTabs();
    initStatsAnimation();

    // Инициализация калькулятора если он есть на странице
    if (document.getElementById('profitCalculator')) {
        initCalculator();
    }

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

    console.log('DirectLine: Все скрипты инициализированы');
});
