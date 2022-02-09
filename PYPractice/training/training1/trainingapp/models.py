from django.db import models

# Create your models here.
class contact(models.Model):
    firstname=models.CharField(max_length=50)
    lastname=models.CharField(max_length=50)
    username=models.CharField(max_length=81)
    password=models.CharField(max_length=20)
    email=models.EmailField()
    contact=models.IntegerField()

    def __str__(self):
        return self.email

    


