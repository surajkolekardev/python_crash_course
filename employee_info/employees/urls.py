# employees/urls.py
from django.urls import path
from .views import employee_create, employee_success

urlpatterns = [
    path('add/', employee_create, name='employee_create'),
    path('success/', employee_success, name='employee_success'),
]