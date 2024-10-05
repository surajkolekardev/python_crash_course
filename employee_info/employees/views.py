# employees/views.py
from django.shortcuts import render, redirect
from .forms import EmployeeForm

def employee_create(request):
    """
    View to handle employee creation. 
    Displays a form and stores the employee's information in the database when the form is submitted.
    """
    if request.method == 'POST':
        form = EmployeeForm(request.POST)
        if form.is_valid():
            form.save()  # Save the data to the database
            return redirect('employee_success')  # Redirect to a success page
    else:
        form = EmployeeForm()

    return render(request, 'employees/employee_form.html', {'form': form})

def employee_success(request):
    """
    View to display a success message after the form is submitted.
    """
    return render(request, 'employees/success.html')
