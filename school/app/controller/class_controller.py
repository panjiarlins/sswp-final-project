from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.forms.models import model_to_dict
from django.contrib.auth.decorators import login_required
from app.models import Class
from app.forms import ClassForm

def class_list(request):
    if request.method == 'POST':
        searchby = request.POST['searchby']
        req = request.POST.dict()
        name = req['name']
        if searchby == 'class_name':
            classes = Class.objects.filter(class_name__contains=name).order_by('-class_batch')
        elif searchby == 'class_batch':
            classes = Class.objects.filter(class_batch__contains=name).order_by('-class_batch')
    else:
        classes = Class.objects.all().order_by('-class_batch')
    context = {
        'class_list' : classes,
    }
    return render(request, 'appTemp/class/class_list.html', context)

@login_required
def class_add(request):
    if request.method == 'POST':
        form = ClassForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('class'))
    else:
        form = ClassForm()
    context = {
        'form': form
    }
    return render(request, 'appTemp/class/class_add.html', context=context)

@login_required
def class_edit(request, class_id):
    if request.method == 'POST':
        classes = Class.objects.get(pk=class_id)
        form = ClassForm(request.POST, instance=classes)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('class'))
    else:
        classes = Class.objects.get(pk=class_id)
        fields = model_to_dict(classes)
        form = ClassForm(initial=fields, instance=classes)
    context = {
        'form': form,
        'type': 'edit',
    }
    return render(request, 'appTemp/class/class_add.html', context)

@login_required
def class_delete(request, class_id):
    classes = Class.objects.get(pk=class_id)
    if request.method == 'POST':
        classes.delete()
        return HttpResponseRedirect(reverse('class'))
    context = {
        'class': classes
    }
    return render(request, 'appTemp/class/class_delete.html', context=context)