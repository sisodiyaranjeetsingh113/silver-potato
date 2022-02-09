from django.db import models
 
# Create your models here.
class EmployeeProfile(models.Model):
    first_name=models.CharField(max_length=32)
    last_name=models.CharField(max_length=32)
    image=models.ImageField(upload_to='pics')
    description=models.TextField()

     