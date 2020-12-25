from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from django.urls import reverse
from django.forms.models import model_to_dict
from django.contrib.auth.decorators import login_required

# Create your views here.
import requests, ast
def covid_info(request):
    url = 'https://api.kawalcorona.com/indonesia/'
    response = requests.get(url)
    data = response.json()
    if str(data)[0] == '[' :
        context = ast.literal_eval(str(data)[1:-1])
    else:
        context = ast.literal_eval(str(data))
    #return HttpResponse(result)
    #return JsonResponse(data, safe=False)
    return render(request, 'appTemp/covid_info.html', context)

from .models import Subject, Employee, Student
from .forms import SubjectForm, EmployeeForm, StudentForm
def index(request):
    # we check the session with key ‘num_visits’, if doesn’t exist we set to 1
    num_visits = request.session.get('num_visits', 1)
    request.session['num_visits'] = num_visits + 1  # add everytime we reload
    context = {
        'num_subject' : Subject.objects.all().count(),
        'num_employee' : Employee.objects.all().count(),
        'num_student' : Student.objects.all().count(),
        'total_visit': num_visits,
    }
    return render(request, 'appTemp/index.html', context)

def subject_list(request):
    context = {
        'subject_list' : Subject.objects.all(),
    }
    return render(request, 'appTemp/subject_list.html', context)

@login_required
def subject_add(request):
    if request.method == 'POST':
        form = SubjectForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('subject'))
    else:
        form = SubjectForm()
    context = {
        'form': form
    }
    return render(request, 'appTemp/subject_add.html', context=context)

@login_required
def subject_edit(request, subject_id):
    if request.method == 'POST':
        subject = Subject.objects.get(pk=subject_id)
        form = SubjectForm(request.POST, instance=subject)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('subject'))
    else:
        subject = Subject.objects.get(pk=subject_id)
        fields = model_to_dict(subject)
        form = SubjectForm(initial=fields, instance=subject)
    context = {
        'form': form,
        'type': 'edit',
    }
    return render(request, 'appTemp/subject_add.html', context)

@login_required
def subject_delete(request, subject_id):
    subject = Subject.objects.get(pk=subject_id)
    if request.method == 'POST':
        subject.delete()
        return HttpResponseRedirect(reverse('subject'))
    context = {
        'subject': subject
    }
    return render(request, 'appTemp/subject_delete.html', context=context)

# --------------------------EMPLOYEE---------------------------
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

def student_list(request):
    context = {
        'student_list' : Student.objects.all(),
    }
    return render(request, 'appTemp/student_list.html', context)

@login_required
def student_add(request):
    if request.method == 'POST':
        form = StudentForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('student'))
    else:
        form = StudentForm()
    context = {
        'form': form
    }
    return render(request, 'appTemp/student_add.html', context=context)

@login_required
def student_edit(request, student_id):
    if request.method == 'POST':
        student = Student.objects.get(pk=student_id)
        form = StudentForm(request.POST, instance=student)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('student'))
    else:
        student = Student.objects.get(pk=student_id)
        fields = model_to_dict(student)
        form = StudentForm(initial=fields, instance=student)
    context = {
        'form': form,
        'type': 'edit',
    }
    return render(request, 'appTemp/student_add.html', context=context)

@login_required
def student_delete(request, student_id):
    student = Student.objects.get(pk=student_id)
    if request.method == 'POST':
        student.delete()
        return HttpResponseRedirect(reverse('student'))
    context = {
        'student': student
    }
    return render(request, 'appTemp/student_delete.html', context=context)