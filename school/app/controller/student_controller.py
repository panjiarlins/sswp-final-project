from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.forms.models import model_to_dict
from django.contrib.auth.decorators import login_required
from app.models import Student
from app.forms import StudentForm

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