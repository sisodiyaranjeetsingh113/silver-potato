from django.contrib.auth import views as auth_views
from . import views
from django.conf.urls import url
from django.urls import path
urlpatterns = [
    path('', views.home, name='home'), 
    path('login/', views.loginview, name='login'), 
     path('logout/', views.signout, name='logout'), 
    path('register/', views.register, name='register'), 
    url('viewsss/', views.Empview, name='viewsss'), 
    
    #...
]