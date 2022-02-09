from django.shortcuts import render 
from django.contrib.auth.models import User, auth
from .models import Destination, UserProfile
# Create your views here.
def index(request):
    dest1=Destination.objects.get(pk=2)
    dest2=Destination.objects.get(pk=3)
    dest3=Destination.objects.get(pk=4)
    dest4=Destination.objects.get(pk=5)
    dest5=Destination.objects.get(pk=6)
    dest6=Destination.objects.get(pk=7)
    return render(request,'index.html',{'dest1':dest1,'dest2':dest2,'dest3':dest3,'dest4':dest4,'dest5':dest5,'dest6':dest6})
def contact(request):
    return render(request,'contact.html')
def destinations1(request):
    dests1=Destination.objects.get(pk=2)
    
    return render(request,'destinations1.html',{'dests1':dests1})
def destinations2(request):
    dests1=Destination.objects.get(pk=3)
    
    return render(request,'destinations2.html',{'dests1':dests1})
def destinations3(request):
    dests1=Destination.objects.get(pk=4)
    
    return render(request,'destinations3.html',{'dests1':dests1})
def destinations4(request):
    dests1=Destination.objects.get(pk=5)
    
    return render(request,'destinations4.html',{'dests1':dests1})
def destinations5(request):
    dests1=Destination.objects.get(pk=6)
    
    return render(request,'destinations5.html',{'dests1':dests1})
def destinations6(request):
    dests1=Destination.objects.get(pk=7)
    
    return render(request,'destinations6.html',{'dests1':dests1})
def profile(request):
    
    return render(request,'profile.html')