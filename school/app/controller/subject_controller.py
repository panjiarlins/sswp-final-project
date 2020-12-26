from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.forms.models import model_to_dict
from django.contrib.auth.decorators import login_required
from app.models import Subject
from app.forms import SubjectForm

def subject_list(request):
    if request.method == 'POST':
        searchby = request.POST['searchby']
        req = request.POST.dict()
        name = req['name']
        if searchby == 'subject_name':
            subjects = Subject.objects.filter(subject_name__contains=name).order_by('subject_name')
        else:
            subjects = Subject.objects.filter(subject_description__contains=name).order_by('subject_name')
    else:
        subjects = Subject.objects.all().order_by('subject_name')
    context = {
        'subject_list' : subjects,
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