from django.shortcuts import render
from .models import Destination
# Create your views here.
def index(request):
    dest1=Destination()
    dest1.name = "Mumbai"
    dest1.img = "destination_1.jpg"
    dest1.description = "City Of Dreams...."
    dest1.price = 7000
    dest1.offer= False
    dest2=Destination()
    dest2.name="Ujjain"
    dest2.img = "destination_2.jpg"
    dest2.description="City Of Gods...."
    dest2.price=100
    dest2.offer = True
    dest3=Destination()
    dest3.img = "destination_3.jpg"
    dest3.name = "Bangaluru"
    dest3.description = "Silicon city...."
    dest3.price = 7000
    dest3.offer = False
    dest4=Destination()
    dest4.img = "destination_4.jpg"
    dest4.name="Indore"
    dest4.description="City Of Employeement...."
    dest4.price=100
    dest4.offer = False
    dest5=Destination()
    dest5.img = "destination_5.jpg"
    dest5.name = "Lukhnau"
    dest5.description = "City Of Bhadshaah...."
    dest5.price = 5000
    dest5.offer = False
    dest6=Destination()
    dest6.img = "destination_6.jpg"
    dest6.name="Rajesthan"
    dest6.description="City of Forts...."
    dest6.price=700
    dest6.offer= False
    dests=[dest1,dest2,dest3,dest4,dest5,dest6]
    return render(request,'index.html',{'dests':dests})