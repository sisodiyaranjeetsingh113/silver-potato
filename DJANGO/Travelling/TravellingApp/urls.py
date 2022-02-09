import django
from django.urls import path
from . import views

urlpatterns=[
    path('', views.index,name='index'),
    path('contact/', views.contact, name='contact'), 
    path('destinations1/', views.destinations1, name='destinations1'),
    path('destinations2/', views.destinations2, name='destinations2'),
    path('destinations3/', views.destinations3, name='destinations3'),
    path('destinations4/', views.destinations4, name='destinations4'),
    path('destinations5/', views.destinations5, name='destinations5'),
    path('destinations6/', views.destinations6, name='destinations6'),
    path('profile/', views.profile, name='profile'),
]