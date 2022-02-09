from django import forms
from .models import Shoes,Shop,Color
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class ShopForm(forms.ModelForm):
    class Meta:
        model=Shop
        fields = '__all__'

class ColorForm(forms.ModelForm):
    class Meta:
        model=Color
        fields = '__all__'

class ShoesForm(forms.ModelForm):
    class Meta:
        model=Shoes
        fields = '__all__'

class UserForm(UserCreationForm):
    first_name = forms.CharField()
    last_name = forms.CharField()
    email = forms.EmailField()
    class Meta:
        model = User
        fields = ('first_name','last_name', 'username', 'email', 'password1' ,'password2' )


