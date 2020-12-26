from django.db import models
from .employment import Employment

class Employee(models.Model):
    employee_id = models.AutoField(primary_key=True)
    employee_name = models.CharField(max_length=50, blank=False, null=False)
    employee_DOB = models.DateField()
    employee_email = models.EmailField(max_length=50)
    employee_phone = models.CharField(max_length=20)
    employee_address = models.TextField(blank=True, null=True)
    employee_position = models.ManyToManyField(Employment)

    class Meta:
        app_label = 'app'

    def __str__(self):
        return f'{self.employee_name} {self.employee_email}'