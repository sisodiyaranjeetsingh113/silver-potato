from django.db import models



# Create your models here.
class Profile(models.Model):
    first_name=models.CharField(max_length=32)
    last_name=models.CharField(max_length=32)
    # image=models.ImageField(blank=True, null=True, upload_to='pics')
    about=models.TextField()
    def __str__(self):
        return self.first_name
    

    

