from django.urls import path
from . import views
urlpatterns = [
    path('signup/', views.register, name="show_form_data" ),
    # path('login/', views.login_form_data, name="login_form_data"),
    # path('', views.index, name="index"),
]