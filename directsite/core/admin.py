from django.contrib import admin
from .models import Lead, VacancyApplication


@admin.register(Lead)
class LeadAdmin(admin.ModelAdmin):
    list_display = ('name', 'phone', 'service', 'status', 'created_at')
    list_filter = ('service', 'status', 'created_at')
    search_fields = ('name', 'phone', 'email')
    list_editable = ('status',)
    readonly_fields = ('created_at', 'updated_at')
    ordering = ('-created_at',)


@admin.register(VacancyApplication)
class VacancyApplicationAdmin(admin.ModelAdmin):
    list_display = ('name', 'phone', 'position', 'created_at')
    list_filter = ('position', 'created_at')
    search_fields = ('name', 'phone', 'email')
    readonly_fields = ('created_at',)
    ordering = ('-created_at',)
