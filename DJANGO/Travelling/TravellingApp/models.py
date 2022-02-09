from django.db import models
# Create your models here.
class Destination(models.Model):
    name = models.CharField(max_length=100)
    img = models.ImageField(upload_to='pics')
    description = models.TextField()
    price = models.IntegerField()
    offer = models.BooleanField(default=False)
class UserProfile(models.Model):
    name=models.CharField(max_length=100)
    contact=models.IntegerField()
    email=models.EmailField()
    img=models.ImageField(upload_to='pics')
    address=models.CharField (max_length=150)
    






