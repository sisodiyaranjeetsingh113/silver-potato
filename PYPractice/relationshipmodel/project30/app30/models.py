from django.db import models
# Create your models here.
class Shop(models.Model):
    shop_name=models.CharField(max_length=30)
    place=models.CharField(max_length=30)
    def __str__(self):
      return self.shop_name
class Color(models.Model):
    color_name=models.CharField(max_length=20)
    def __str__(self):
        return self.color_name
    class Meta:
        ordering = ['color_name']
class Shoes(models.Model):
    shoes_name = models.CharField(max_length=100,unique=True)
    order_date = models.DateField()
    shoes_color= models.ManyToManyField(Color)
    shoes_shop = models.ManyToManyField(Shop)
    def __str__(self):
        return self.shoes_name
    class Meta:
        ordering = ['shoes_name']
