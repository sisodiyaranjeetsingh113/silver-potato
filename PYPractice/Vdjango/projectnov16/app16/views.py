from django.shortcuts import render,redirect
from .models import UserImage
from .forms import UserImageForm
from django.contrib import messages

# Create your views here.
def home(request):
    data=UserImage.objects.all()
    return render(request,'index.html',{'data':data})
def add(request):
    if request.method == 'POST':
        f = UserImageForm(request.POST,request.FILES)
        if f.is_valid():
            f.save()
            messages.success(request, 'Shoes added successfully')
        return redirect('/')
    else:
        f = UserImageForm()
    return render(request, 'add.html',{'form':f})
def update_view(request,id):
    if request.method == 'POST':
        userI = UserImage.objects.get(id=id)
        form=UserImageForm(request.POST,request.FILES,instance=userI)
        if form.is_valid():
            form.save()
            redirect('/')
    else:
        obj=UserImage.objects.get(pk=id)
        form=UserImageForm(request.POST or None,instance=obj)
    return render (request, 'update_view.html', {'form':form})


    

    
