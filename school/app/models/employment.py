from django.db import models

class Employment(models.Model):
    employment_id = models.AutoField(primary_key=True)
    employment_name = models.CharField(max_length=50, blank=False, null=False)
    employment_description = models.TextField(blank=True, null=True)

    class Meta:
        app_label = 'app'
        
    def __str__(self):
        return f'{self.employment_name} {self.employment_description}'