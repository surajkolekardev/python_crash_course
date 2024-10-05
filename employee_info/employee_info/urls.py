# employee_info/urls.py
from django.contrib import admin
from django.urls import path, include
from employees.views import employee_create

urlpatterns = [
    path('admin/', admin.site.urls),
    path('employees/', include('employees.urls')),  # Existing employee app URL pattern
    path('', employee_create, name='home'),  # Redirect the base URL ('') to the employee form
]