from django.urls import path
from . import views


urlpatterns =[
    path('', views.home, name='home'), 
    path('add/', views.add, name='add'), 
    path('update/<id>', views.update_view, name='update'), 
]