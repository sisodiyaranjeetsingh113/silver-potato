from django.shortcuts import render 
from datetime import datetime
# Create your views here. 
def wish(request): 
    date1=datetime.now()
    ct= date1.strftime("%H:%M")
    msg='Hello Guest !!!! Very Very Good ' 
    h=int(date1.strftime('%H')) 
    if h<12: 
        msg +='Morning!!!' 
    elif h<16: 
        msg +='AfterNoon!!!' 
    elif h<21: 
        msg +='Evening!!!' 
    else: 
        msg='Hello Guest !!!! Very Very Good Night!!!' 
    my_dict={'time':ct,'message':msg} 
    return render(request,'index.html',context=my_dict)