from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.forms.models import model_to_dict
from django.contrib.auth.decorators import login_required
from app.models import Extracurricular
from app.forms import ExtracurricularForm
from django.core.paginator import Paginator

def extracurricular_list(request):
    if request.method == 'POST':
        searchby = request.POST['searchby']
        req = request.POST.dict()
        name = req['name']
        if searchby == 'extracurricular_name':
            extracurriculars = Extracurricular.objects.filter(extracurricular_name__icontains=name).order_by('extracurricular_name')
        elif searchby == 'extracurricular_description':
            extracurriculars = Extracurricular.objects.filter(extracurricular_description__icontains=name).order_by('extracurricular_name')
    else:
        extracurriculars = Extracurricular.objects.all().order_by('extracurricular_name')
    
    paginator = Paginator(extracurriculars, 5)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    context = {
        'extracurricular_list' : page_obj,
    }
    return render(request, 'appTemp/extracurricular/extracurricular_list.html', context)

@login_required
def extracurricular_add(request):
    if request.method == 'POST':
        form = ExtracurricularForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('extracurricular'))
    else:
        form = ExtracurricularForm()
    context = {
        'form': form
    }
    return render(request, 'appTemp/extracurricular/extracurricular_add.html', context=context)

@login_required
def extracurricular_edit(request, extracurricular_id):
    if request.method == 'POST':
        extracurriculars = Extracurricular.objects.get(pk=extracurricular_id)
        form = ExtracurricularForm(request.POST, instance=extracurriculars)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('extracurricular'))
    else:
        extracurriculars = Extracurricular.objects.get(pk=extracurricular_id)
        fields = model_to_dict(extracurriculars)
        form = ExtracurricularForm(initial=fields, instance=extracurriculars)
    context = {
        'form': form,
        'type': 'edit',
    }
    return render(request, 'appTemp/extracurricular/extracurricular_add.html', context)

@login_required
def extracurricular_delete(request, extracurricular_id):
    extracurriculars = Extracurricular.objects.get(pk=extracurricular_id)
    if request.method == 'POST':
        extracurriculars.delete()
        return HttpResponseRedirect(reverse('extracurricular'))
    context = {
        'extracurricular': extracurriculars
    }
    return render(request, 'appTemp/extracurricular/extracurricular_delete.html', context=context)