from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.forms.models import model_to_dict
from django.contrib.auth.decorators import login_required
from app.models import Student
from app.forms import StudentForm
from django.core.paginator import Paginator

def student_list(request):
    if request.method == 'POST':
        searchby = request.POST['searchby']
        req = request.POST.dict()
        name = req['name']
        if searchby == 'student_name':
            students = Student.objects.filter(student_name__contains=name).order_by('-student_DOB')
        elif searchby == 'student_email':
            students = Student.objects.filter(student_email__contains=name).order_by('-student_DOB')
        elif searchby == 'student_phone':
            students = Student.objects.filter(student_phone__contains=name).order_by('-student_DOB')
        elif searchby == 'student_address':
            students = Student.objects.filter(student_address__contains=name).order_by('-student_DOB')
    else:
        students = Student.objects.all().order_by('-student_DOB')
    
    paginator = Paginator(students, 10)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    context = {
        'student_list' : page_obj,
    }
    return render(request, 'appTemp/student/student_list.html', context)

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
    return render(request, 'appTemp/student/student_add.html', context=context)

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
    return render(request, 'appTemp/student/student_add.html', context=context)

@login_required
def student_delete(request, student_id):
    student = Student.objects.get(pk=student_id)
    if request.method == 'POST':
        student.delete()
        return HttpResponseRedirect(reverse('student'))
    context = {
        'student': student
    }
    return render(request, 'appTemp/student/student_delete.html', context=context)