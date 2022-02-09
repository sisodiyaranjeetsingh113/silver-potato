from django.shortcuts import render,redirect
from django.contrib import messages
from django.contrib.auth.models import User, auth
# Create your views here.

def login(request):
    userE=""
    passwordE=""
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user =auth.authenticate(username=username,password=password)
        if user is not None:
            auth.login(request, user)
            return redirect("/")
        else :
            if User.objects.filter(username=username).exists() == False:
                userE='Invalid Username!'
                
            elif User.objects.filter(password=password).exists() == False:
                passwordE='Invalid password!'
            mydict={'userError':userE,'passwordError':passwordE}
            return render(request,'login.html',{'mydict':mydict})
    else :
        return render(request,'login.html')
def register(request):
    usernameE=""
    emailE=""
    passwordE=""
    if request.method == 'POST':
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        username = request.POST['username']
        password1 = request.POST['password1']
        password2 = request.POST['password2']
        email = request.POST['email']
        if password1 == password2:
            if User.objects.filter(username=username).exists():
                usernameE='Username exists!'
                return render(request,'register.html',{'userE':usernameE})
            elif User.objects.filter(email=email).exists():
                emailE='Email exists!'
                return render(request,'register.html',{'emailE':emailE})
            else: 
                user = User.objects.create_user(username=username, password=password1,email=email,first_name=first_name,last_name=last_name)
                user.save()
                print('User Create')  
                return redirect('login')          
        else :
            passwordE='password not matching...'
            return render(request,'register.html',{'passwordE':passwordE})
        return redirect('/')               
    else:
        return render(request,'register.html')

def logout(request):
    auth.logout(request)
    return redirect('/')