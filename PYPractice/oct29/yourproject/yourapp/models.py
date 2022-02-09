from django.db import models

# Create your models here.
class Emp(models.Model):
    employeename=models.CharField(max_length=50)
    salary=models.IntegerField()
    department=models.CharField(max_length=50)


    