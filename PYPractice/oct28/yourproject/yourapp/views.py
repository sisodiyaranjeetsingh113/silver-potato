from django.contrib.auth.decorators import login_required
from django.contrib import messages 
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import redirect,render
from django.contrib.auth import authenticate,login
from django.contrib.auth.forms import AuthenticationForm
#...

def loginview(request):
    if request.user.is_authenticated:
        return redirect('/')
    if request.method=='POST':
        # import pdb;
        # pdb.set_trace()
        username=request.POST['username']
        password=request.POST['password']
        user=authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('/')
        else:
            
            form=AuthenticationForm()
            return render(request, 'login.html', {'form':form})
    else:
        form=AuthenticationForm()
        return render(request, 'login.html', {'form':form})
        

def home(request):
    return render(request,'base.html')

def register(request):
    if request.user.is_authenticated:
        return redirect('/')
    if request.method == 'POST':
        f = UserCreationForm(request.POST)
        if f.is_valid():
            f.save()
            messages.success(request, 'Account created successfully')
            return redirect('/')


    else:
        f = UserCreationForm()
    return render(request, 'signup.html', {'form': f})
from django.contrib.auth import logout
def signout(request):
    logout(request)
    return redirect('/')