from django.db import models
from django.db.models import BigAutoField

# Create your models here.
class product(models.Model):
    product_id = models.AutoField
    product_name = models.CharField(max_length=50)
    product_category = models.CharField(max_length=100, default="")
    product_subcategory = models.CharField(max_length=100, default="")
    product_price = models.IntegerField(default=0)
    product_discription = models.CharField(max_length=500)
    product_date = models.DateField()
    product_image = models.ImageField(upload_to='blog/images', default="")
    def __str__(self):
        return self.product_name
class Employee(models.Model):
    eid=models.AutoField
    ename=models.CharField(max_length=50,default="no name")
    eloc=models.CharField(max_length=50,default="")
    esal=models.IntegerField(default=0)
    def __str__(self):
        return self.ename
class UserReg(models.Model):
    uid=models.AutoField
    uname=models.CharField(max_length=20,default="no user name")
    password=models.CharField(max_length=30,default="")
    email=models.CharField(max_length=50,default="")
    contact=models.CharField(max_length=13,default="")
    fname=models.CharField(max_length=20,default="")
    lname=models.CharField(max_length=20,default="")
    city=models.CharField(max_length=20,default="Mumbai")
    def __str__(self):
        return self.uname