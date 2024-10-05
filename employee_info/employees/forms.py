# employees/forms.py
from django import forms
from .models import Employee

class EmployeeForm(forms.ModelForm):
    """
    Form for employee input.
    """
    class Meta:
        model = Employee
        fields = ['name', 'city', 'contact', 'email']
