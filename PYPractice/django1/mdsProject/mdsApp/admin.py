
from django.contrib import admin 
from mdsApp.models import EMployee 
# Register your models here. 
class EmployeeAdmin(admin.ModelAdmin): 
    list_display=['eno','ename','esal','eaddr'] 
admin.site.register(EMployee,EmployeeAdmin)