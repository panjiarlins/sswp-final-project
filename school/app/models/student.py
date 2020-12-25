from django.db import models
from .Class import Class
from .extracurricular import Extracurricular

class Student(models.Model):
    student_id = models.AutoField(primary_key=True)
    student_name = models.CharField(max_length=50, blank=False, null=False)
    student_DOB = models.DateField()
    student_email = models.EmailField(max_length=50)
    student_phone = models.CharField(max_length=20)
    student_address = models.TextField(blank=True, null=True)
    student_class = models.ManyToManyField(Class)
    student_extracurricular = models.ManyToManyField(Extracurricular)

    def __str__(self):
        return f'{self.student_name} {self.student_DOB} {self.student_email} {self.student_phone} {self.student_address} {self.student_class} {self.student_extracurricular}'