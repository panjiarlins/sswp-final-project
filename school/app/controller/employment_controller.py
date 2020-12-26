from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.forms.models import model_to_dict
from django.contrib.auth.decorators import login_required
from app.models import Employment
from app.forms import EmploymentForm
from django.core.paginator import Paginator

def employment_list(request):
    if request.method == 'POST':
        searchby = request.POST['searchby']
        req = request.POST.dict()
        name = req['name']
        if searchby == 'employment_name':
            employments = Employment.objects.filter(employment_name__contains=name).order_by('employment_name')
        else:
            employments = Employment.objects.filter(employment_description__contains=name).order_by('employment_name')
    else:
        employments = Employment.objects.all().order_by('employment_name')
    
    paginator = Paginator(employments, 5)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    context = {
        'employment_list' : page_obj,
    }
    return render(request, 'appTemp/employment/employment_list.html', context)

@login_required
def employment_add(request):
    if request.method == 'POST':
        form = EmploymentForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('employment'))
    else:
        form = EmploymentForm()
    context = {
        'form': form
    }
    return render(request, 'appTemp/employment/employment_add.html', context=context)

@login_required
def employment_edit(request, employment_id):
    if request.method == 'POST':
        employment = Employment.objects.get(pk=employment_id)
        form = EmploymentForm(request.POST, instance=employment)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('employment'))
    else:
        employment = Employment.objects.get(pk=employment_id)
        fields = model_to_dict(employment)
        form = EmploymentForm(initial=fields, instance=employment)
    context = {
        'form': form,
        'type': 'edit',
    }
    return render(request, 'appTemp/employment/employment_add.html', context)

@login_required
def employment_delete(request, employment_id):
    employment = Employment.objects.get(pk=employment_id)
    if request.method == 'POST':
        employment.delete()
        return HttpResponseRedirect(reverse('employment'))
    context = {
        'employment': employment
    }
    return render(request, 'appTemp/employment/employment_delete.html', context=context)