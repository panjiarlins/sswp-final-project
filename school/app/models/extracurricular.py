from django.db import models
from .employee import Employee

class Extracurricular(models.Model):
    extracurricular_id = models.AutoField(primary_key=True)
    extracurricular_name = models.CharField(max_length=50, blank=False, null=False)
    extracurricular_advisor = models.OneToOneField(Employee, on_delete=models.CASCADE)
    extracurricular_description = models.TextField(blank=True, null=True)

    class Meta:
        app_label = 'app'
    
    def __str__(self):
        return f'{self.extracurricular_name} {self.extracurricular_advisor} {self.extracurricular_description}'