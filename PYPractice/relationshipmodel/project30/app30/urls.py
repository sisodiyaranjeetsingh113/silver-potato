from django.urls import path
from . import views

urlpatterns = [
    path('',views.home, name='home'),
    path('login/',views.loginview, name='login'),
    path('signup/',views.register, name='signup'),
    path('logout/',views.signout, name='logout'),
    path('profile/',views.profileview, name='profile'),
    path('profile/add/',views.add_shoesview, name='add'),
    path('profile/<int:id>/',views.updateview, name='update'),
    path('profile/delete/<int:id>/',views.delete_view, name='delete'),

]