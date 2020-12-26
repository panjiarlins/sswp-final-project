from django.db import models
from .employee import Employee
from .subject import Subject

class Class(models.Model):
    class_id = models.AutoField(primary_key=True)
    class_name = models.CharField(max_length=50, blank=False, null=False)
    class_batch = models.CharField(max_length=5, blank=False, null=False)
    class_advisor = models.ForeignKey(Employee, on_delete=models.CASCADE)
    class_subject = models.ManyToManyField(Subject)

    class Meta:
        app_label = 'app'
    
    def __str__(self):
        return f'{self.class_name} {self.class_batch}'