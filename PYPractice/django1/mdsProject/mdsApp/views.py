from django.shortcuts import render 
from mdsApp.models import EMployee 
 # Create your views here. 
def empdata(request): 
    emp_list=EMployee.objects.all() 
    my_dict={'emp_list':emp_list} 
    return render(request, 'emp.html', context=my_dict) 



