from django.contrib import admin
from django.urls import path
from . import views
urlpatterns = [
    path("",views.index,name='Home'),
    path("about",views.about,name='about'),
    path("insert",views.insert,name='insert'),
    path("contact",views.contact,name='contact'),
    path("reg",views.registation,name='reg'),
    path("reg_insert",views.reg_insert,name='reg_insert'),
    path("more",views.more,name='more'),
    path("more_data",views.more_data,name='more'),
    path("more_update",views.more_update,name="more_update"),
    path("loginuser",views.loginuser,name='login'),
    path("userlogout",views.userlogout,name='logout'),
    path("agg",views.agg,name='agg'),
    path("ajax", views.ajax, name='ajax'),
    path("ajax1", views.ajax1, name='ajax1'),
    path("ajax2", views.ajax2, name='ajax2'),
    path("st",views.st_load,name='st'),
    path("demo/<int:id>/",views.demo,name="url1")
]