from django.shortcuts import render, redirect
from django.contrib.auth.models import User, auth
from .models import contact
# Create your views here.
def index(request):
    return render(request,'index.html')
def login(request):
    emailE=""
    passwordE=""
    print(request.method)
    if request.method == 'POST':
        email = request.POST['email']
        password = request.POST['password']
        user = Signup.objects.filter(email=email,password=password)
        if user is not None:
            return redirect("/")
        else :
            if Signup.objects.filter(email=email).exists() == False:
                emailE='Invalid Email!'
                print('Invalid Email!')
                return render(request,'login.html',{'emailE':emailE})
    
                
            elif Signup.objects.filter(password=password).exists() == False:
                passwordE='Invalid password!'
                print('Invalid password!')
                return render(request,'login.html',{'passwordE':passwordE})
    else :     
        print('last Else')
        return render(request,'login.html')
def signup(request):
    usernameE=""
    emailE=""
    passwordE=""
    usernameE=""
    contactE=""
    if request.method == 'POST':
        firstname = request.POST['firstname']
        lastname = request.POST['lastname']
        username = request.POST['username']
        password1 = request.POST['password1']
        password2 = request.POST['password2']
        email = request.POST['email']
        contact =request.POST['contact']
        if firstname == "" or lastname == "" or password1 == "" or email == "" or contact == "":
            if contact == "":
                contactE='contact is empty!'
                return render(request,'signup.html',{'contactE':contactE})
            if email == "":
                emailE='Email is empty!'
                return render(request,'signup.html',{'emailE':emailE})
            
            if firstname == "":
                firstnameE='Firstname is empty!'
                return render(request,'signup.html',{'firstnameE':firstnameE})
            if lastname == "":
                lastnameE='Lastname is empty!'
                return render(request,'signup.html',{'lastnameE':lastnameE})
            if password1 == "":
                passwordE = "Password is empty!"
                return render(request,'signup.html',{'password1E':passwordE})
        else:
            if password1 == password2:
                if Signup.objects.filter(username=username).exists():
                    usernameE='Username exists!'
                    return render(request,'signup.html',{'userE':usernameE})
                elif Signup.objects.filter(email=email).exists():
                    emailE='Email exists!'
                    return render(request,'signup.html',{'emailE':emailE})
                else: 
                    user = Signup(username=username, password=password1,email=email,firstname=firstname,lastname=lastname,contact=contact)
                    user.save()
                    print('User Create')  
                    return redirect('login')          
            else :
                passwordEE='password not matching...'
                return render(request,'signup.html',{'passwordEE':passwordEE})
            return redirect('/')               
    else:

        return render(request,'signup.html',)

def logout(request):
    auth.logout(request)
    return redirect('/')
