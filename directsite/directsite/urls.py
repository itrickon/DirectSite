"""
URL configuration for directsite project.
"""
from django.contrib import admin
from django.urls import path
from core import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name='index'),
    path('service/', views.service, name='service'),
    path('team/', views.team, name='team'),
    path('contacts/', views.contacts, name='contacts'),
    path('vacancy/', views.vacancy, name='vacancy'),
    path('calculator/', views.calculator, name='calculator'),
    path('privacy-policy/', views.privacy_policy, name='privacy_policy'),
    path('user-agreement/', views.user_agreement, name='user_agreement'),
]
