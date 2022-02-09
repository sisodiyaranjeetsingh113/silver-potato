from .models import UserImage
from django import forms
class UserImageForm(forms.ModelForm):
    class Meta:
        model=UserImage
        fields='__all__'


    