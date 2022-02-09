from django.shortcuts import (render, get_object_or_404,HttpResponseRedirect, redirect)
from .models import Profile
from .forms import ProfileForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate,login
from django.contrib.auth.forms import AuthenticationForm


# Create your views here.
def home(request):
    return render(request,'index.html')

@login_required(login_url='login')

def Profileview(request):
    form=Profile.objects.all()
    return render(request,'profile.html',{'form':form})
def detail_view(request,id):
    data=Profile.objects.get(id=id)
    return render(request,'detail.html',{'data':data})
def CreateView(request):
    if request.method=='POST':
        form=ProfileForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')
    else:
        form=ProfileForm()
    return render(request, 'add.html', {'form':form})

def update_view(request,id):
    if request.method=='POST':
        obj=Profile.objects.get(pk=id)
        form=ProfileForm(request.POST, instance=obj)
        if form.is_valid():
            form.save()
            return redirect('/')
    else:
        obj=Profile.objects.get(pk=id)
        form=ProfileForm(request.POST or None,instance=obj)
    return render (request, 'update_view.html', {'form':form})

def delete_view(request, id):
    if request.method=='POST':
        pi=Profile.objects.get(pk=id)
        pi.delete()
        return redirect('/')
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

