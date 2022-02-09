from django.shortcuts import (render, get_object_or_404,HttpResponseRedirect, redirect)
from django.contrib import messages
from .forms import UserForm,ShoesForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate,login
from django.contrib.auth.forms import AuthenticationForm
from .models import Shop, Shoes, Color


# Create your views here.
def home(request):
    return render(request,'index.html')

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

def register(request):
    if request.user.is_authenticated:
        return redirect('/')
    if request.method == 'POST':
        f = UserForm(request.POST)
        if f.is_valid():
            f.save()
            messages.success(request, 'Account created successfully')
            return redirect('/login')
    else:
        f = UserForm()
    return render(request, 'signup.html', {'form':f})


from django.contrib.auth import logout
def signout(request):
    logout(request)
    return redirect('/')
@login_required(login_url=('/login'))
def profileview(request):
    shoes_data = Shoes.objects.all()
    return render(request,'profile.html',{'shoes_data':shoes_data})
def add_shoesview(request):
    if request.method == 'POST':
        f = ShoesForm(request.POST)
        if f.is_valid():
            f.save()
            messages.success(request, 'Shoes added successfully')
            return redirect('/profile/')
    else:
        f = ShoesForm()
    return render(request, 'add.html', {'form':f})
def updateview(request,id):
    if request.method=='POST':
        obj=Shoes.objects.get(pk=id)
        form=ShoesForm(request.POST, instance=obj)
        if form.is_valid():
            form.save()
            return redirect('/profile/')
    else:
        obj=Shoes.objects.get(pk=id)
        form=ShoesForm(request.POST,instance=obj)
    return render (request, 'update_view.html', {'form':form})    
            
def delete_view(request, id):
    if request.method=='POST':
        pi=Shoes.objects.get(pk=id)
        pi.delete()
        return redirect('/profile/')

