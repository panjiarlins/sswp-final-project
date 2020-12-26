from django.db import models

class Subject(models.Model):
    subject_id = models.AutoField(primary_key=True)
    subject_name = models.CharField(max_length=50, blank=False, null=False)
    subject_description = models.TextField(blank=True, null=True)

    class Meta:
        app_label = 'app'
    
    def __str__(self):
        return f'{self.subject_name}'