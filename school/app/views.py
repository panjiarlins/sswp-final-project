from django.shortcuts import render
from django.http import HttpResponseRedirect
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
    return render(request, 'appTemp/covid_info.html', context)

from .models import Subject, Employee, Student
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