from django.db import models

# Create your models here.
class UserImage(models.Model):
    user_image=models.ImageField(upload_to='pics')
    