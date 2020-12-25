from django.contrib import admin

# Register your models here.

from .models import Subject, Employement, Employee, Student, Extracurricular, Class
admin.site.register(Subject)
admin.site.register(Employement)
admin.site.register(Employee)
admin.site.register(Student)
admin.site.register(Class)
admin.site.register(Extracurricular)