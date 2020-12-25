from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.forms.models import model_to_dict
from django.contrib.auth.decorators import login_required
from app.models import Employee
from app.forms import EmployeeForm

def employee_list(request):
    context = {
        'employee_list' : Employee.objects.all(),
    }
    return render(request, 'appTemp/employee_list.html', context)

@login_required
def employee_add(request):
    if request.method == 'POST':
        form = EmployeeForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('employee'))
    else:
        form = EmployeeForm()
    context = {
        'form': form
    }
    return render(request, 'appTemp/employee_add.html', context)

@login_required
def employee_edit(request, employee_id):
    if request.method == 'POST':
        employee = Employee.objects.get(pk=employee_id)
        form = EmployeeForm(request.POST, instance=employee)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('employee'))
    else:
        employee = Employee.objects.get(pk=employee_id)
        fields = model_to_dict(employee)
        form = EmployeeForm(initial=fields, instance=employee)
    context = {
        'form': form,
        'type': 'edit',
    }
    return render(request, 'appTemp/employee_add.html', context)

@login_required
def employee_delete(request, employee_id):
    employee = Employee.objects.get(pk=employee_id)
    if request.method == 'POST':
        employee.delete()
        return HttpResponseRedirect(reverse('employee'))
    context = {
        'employee': employee
    }
    return render(request, 'appTemp/employee_delete.html', context=context)