from django.shortcuts import render
from .models import Subject, Employee, Student, Class, Employment, Extracurricular, Contact

def index(request):
    # we check the session with key ‘num_visits’, if doesn’t exist we set to 1
    num_visits = request.session.get('num_visits', 1)
    request.session['num_visits'] = num_visits + 1  # add everytime we reload
    context = {
        'num_subject' : Subject.objects.all().count(),
        'num_class' : Class.objects.all().count(),
        'num_employment' : Employment.objects.all().count(),
        'num_extracurricular' : Extracurricular.objects.all().count(),
        'num_employee' : Employee.objects.all().count(),
        'num_student' : Student.objects.all().count(),
        'total_visit': num_visits,
    }
    return render(request, 'appTemp/index/index.html', context)

def contact(request):
    if request.method=="POST":
        contact = Contact()
        name = request.POST.get('name')
        email = request.POST.get('email')
        msg = request.POST.get('msg')
        contact.name = name
        contact.email = email
        contact.msg = msg
        contact.save()
    return render(request, 'appTemp/contact/contact.html')