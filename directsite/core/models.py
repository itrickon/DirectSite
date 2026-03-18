from django.db import models


class Lead(models.Model):
    """Заявка от клиента"""
    SERVICE_CHOICES = [
        ('lead_generation', 'Лидогенерация'),
        ('call_center', 'Call-центр'),
        ('avito', 'Авито'),
        ('recruiting', 'Рекрутинг'),
        ('lead_code', 'Лид-КОД'),
        ('complex', 'Комплекс'),
        ('other', 'Другое'),
    ]

    STATUS_CHOICES = [
        ('new', 'Новая'),
        ('contacted', 'В работе'),
        ('converted', 'Успешно'),
        ('rejected', 'Отказ'),
    ]

    name = models.CharField("Имя", max_length=100)
    phone = models.CharField("Телефон", max_length=20)
    email = models.EmailField("Email", blank=True, null=True)
    service = models.CharField("Услуга", max_length=50, choices=SERVICE_CHOICES, blank=True)
    message = models.TextField("Комментарий", blank=True)
    status = models.CharField("Статус", max_length=20, choices=STATUS_CHOICES, default='new')
    created_at = models.DateTimeField("Дата создания", auto_now_add=True)
    updated_at = models.DateTimeField("Дата обновления", auto_now=True)

    class Meta:
        verbose_name = "Заявка"
        verbose_name_plural = "Заявки"
        ordering = ['-created_at']

    def __str__(self):
        return f"{self.name} ({self.phone})"


class VacancyApplication(models.Model):
    """Отклик на вакансию"""
    POSITION_CHOICES = [
        ('manager', 'Менеджер по продажам'),
        ('call_operator', 'Оператор call-центра'),
        ('recruiter', 'Рекрутер'),
        ('info_collector', 'Сборщик информации'),
        ('other', 'Другое'),
    ]

    name = models.CharField("Имя", max_length=100)
    phone = models.CharField("Телефон", max_length=20)
    email = models.EmailField("Email", blank=True, null=True)
    position = models.CharField("Должность", max_length=50, choices=POSITION_CHOICES)
    experience = models.TextField("Опыт работы", blank=True)
    created_at = models.DateTimeField("Дата создания", auto_now_add=True)

    class Meta:
        verbose_name = "Отклик на вакансию"
        verbose_name_plural = "Отклики на вакансии"
        ordering = ['-created_at']

    def __str__(self):
        return f"{self.name} - {self.get_position_display()}"
