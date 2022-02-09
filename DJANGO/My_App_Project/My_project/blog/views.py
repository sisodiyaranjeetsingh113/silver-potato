from django.db.models import Max,Min,Avg,Sum,Count
from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import product,Employee,UserReg
#from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
# Create your views here.
def index(request):
        products=product.objects.all()
        params={'product1':products}
        return render(request, "blog/home.html",params)
def contact(request):
    return render(request, "blog/contact.html")
def about(request):
    return render(request, "blog/about.html")
def insert(request):
    ename = request.GET.get("ename", "No Name")
    eloc = request.GET.get("eloc", "Mumbai")
    esal = request.GET.get("esal", "0")
    data = Employee(ename=ename, eloc=eloc, esal=esal)
    data.save()
    param={"result":"Your Record Inserted"}
    return render(request, "blog/about.html",param)
def registation(request):
    return render(request,'blog/reg.html')
def reg_insert(request):
    btn=request.GET.get("sub")
    if(btn=="Submit"):
        u_name=request.GET.get("uname","No name")
        password=request.GET.get("pass","")
        email=request.GET.get("email","")
        cont=request.GET.get("cont","")
        fname=request.GET.get("fname","")
        lname=request.GET.get("lname","")
        city=request.GET.get("city","")
        data=UserReg(uname=u_name,password=password,email=email,contact=cont,fname=fname,lname=lname,city=city)
        data.save()
        param={"msg":"Your Registration Successfull..."}
        return render(request,'blog/reg.html',param)
    if(btn=="Display"):
        record=UserReg.objects.all()
        param={"data":record}
        return render(request,"blog/reg.html",param)
def more(request):
    record=UserReg.objects.all()
    param={"data2":record}
    return render(request,"blog/more.html",param)
def more_data(request):
    btn=request.GET.get("sub")
    if(btn=="Display"):
        uname=request.GET.get("uname")
        #record=UserReg.objects.get(uname=uname)
        record = UserReg.objects.get(uname__contains=uname)
        record1 = UserReg.objects.all()
        param={"data":record,"data2":record1}
        return render(request,"blog/more.html",param)
    if(btn=="Delete"):
        name=request.GET.get("uname")
        UserReg.objects.filter(uname=name).delete()
        record1 = UserReg.objects.all()
        param={"data":"Record Deleted Successfully...","data2": record1}
        return render(request,"blog/more.html",param)
    if(btn=="Edit"):
        uname = request.GET.get("uname")
        record = UserReg.objects.get(uname=uname)
        param = {"data": record}
        return render(request, "blog/more_edit.html", param)
def more_update(request):
    u_name = request.GET.get("uname", "No name")
    password = request.GET.get("pass", "")
    email = request.GET.get("email", "")
    cont = request.GET.get("cont", "")
    fname = request.GET.get("fname", "")
    lname = request.GET.get("lname", "")
    city = request.GET.get("city", "")
    data=UserReg.objects.get(uname=u_name)
    data.password=password
    data.email=email
    data.contact=cont
    data.fname=fname
    data.lname=lname
    data.city=city
    data.save()
    record1 = UserReg.objects.all()
    param={"data1":"Record Updated Successfully....","data2":record1}
    return render(request,"blog/more.html",param)
def loginuser(request):
    if request.method=="POST":
        uname=request.POST['uname']
        password=request.POST['pass']
        #user=authenticate(request,username=uname,password=password)
        #user=UserReg.objects.get(uname=uname,password=password)
        user=UserReg.objects.filter(uname=uname,password=password).count()
        if user>0:
            #login(request,user)
            request.session['usession'] = uname
            u_session=request.session['usession']
            products = product.objects.all()
            data={"msg":"Login Successfully ...","session":u_session,'product1': products}
            return render(request,"blog/home.html",data)
            #return redirect("/blog/")
        else:
            data={"msg":"Uname and password doesnt match try again.."}
            return render(request, "blog/home.html",data)
    else:
        return render(request,"blog/home.html")
    return HttpResponse("<h1>This is my Blog-Login-Page...</h1>")
def st_load(request):
    return render(request,"blog/st_load.html")
def userlogout(request):
    del request.session['usession']
    return redirect("/blog/")
def agg(request):
    products = product.objects.all().aggregate(Count('product_price'))
    params = {'product1': products}
    return render(request, "blog/aggr.html", params)
def ajax(request):
    return render(request, "blog/ajax.html")
def ajax1(request):
    u_name = request.GET.get("uname", "No name")
    password = request.GET.get("pass", "")
    email = request.GET.get("email", "")
    cont = request.GET.get("cont", "")
    fname = request.GET.get("fname", "")
    lname = request.GET.get("lname", "")
    city = request.GET.get("city", "")
    data = UserReg(uname=u_name, password=password, email=email, contact=cont, fname=fname, lname=lname, city=city)
    data.save()
    pass
def ajax2(request):
    record = UserReg.objects.all()
    param = {"data": record}
    return render(request, "blog/display.html", param)
def demo(request,id):
    param={"name":id}
    return render(request, "blog/display.html", param)

