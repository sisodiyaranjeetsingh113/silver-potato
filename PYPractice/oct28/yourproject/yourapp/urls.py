from django.contrib.auth import views as auth_views
from . import views
from django.conf.urls import url
from django.urls import path
urlpatterns = [
    path('', views.home, name='home'), 
    url('signup/', views.register, name='register'), 
    url('login/', views.loginview, name='login'), 
    url('logout/', views.signout, name='logout'), 
    
    #...
]