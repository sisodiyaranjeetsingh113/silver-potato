from django.urls import path
from . import views
urlpatterns = [
    path('',views.home, name='home'),
    path('profile/',views.Profileview, name='Profileview'),
    path('profile/add/',views.CreateView, name='add'),
    path('delete/<int:id>',views.delete_view, name='delete'),
    path('profile/<int:id>',views.detail_view, name='detail_view'),
    path('profile/update/<int:id>',views.update_view, name='update_view'), 
    path('login/',views.loginview, name='login'),
    path('signup/',views.register, name='signup'),
    path('logout/',views.signout, name='logout'),

]