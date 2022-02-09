from django.contrib import admin

# Register your models here.
from .models import product,Employee,UserReg
admin.site.register(product)
admin.site.register(Employee)
admin.site.register(UserReg)
