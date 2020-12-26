from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.forms.models import model_to_dict
from django.contrib.auth.decorators import login_required
from app.models import Employee
from app.forms import EmployeeForm
from django.core.paginator import Paginator

def employee_list(request):
    if request.method == 'POST':
        searchby = request.POST['searchby']
        req = request.POST.dict()
        name = req['name']
        if searchby == 'employee_name':
            employees = Employee.objects.filter(employee_name__contains=name).order_by('-employee_DOB')
        elif searchby == 'employee_email':
            employees = Employee.objects.filter(employee_email__contains=name).order_by('-employee_DOB')
        elif searchby == 'employee_phone':
            employees = Employee.objects.filter(employee_phone__contains=name).order_by('-employee_DOB')
        elif searchby == 'employee_address':
            employees = Employee.objects.filter(employee_address__contains=name).order_by('-employee_DOB')
    else:
        employees = Employee.objects.all().order_by('-employee_DOB')
    
    paginator = Paginator(employees, 10)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    context = {
        'employee_list' : page_obj,
    }
    return render(request, 'appTemp/employee/employee_list.html', context)

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
    return render(request, 'appTemp/employee/employee_add.html', context)

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
    return render(request, 'appTemp/employee/employee_add.html', context)

@login_required
def employee_delete(request, employee_id):
    employee = Employee.objects.get(pk=employee_id)
    if request.method == 'POST':
        employee.delete()
        return HttpResponseRedirect(reverse('employee'))
    context = {
        'employee': employee
    }
    return render(request, 'appTemp/employee/employee_delete.html', context=context)