from django import forms
from .models import *


class PostalItemForm(forms.ModelForm):
    
    class Meta:
        model = PostalItem
        exclude = ('id', 'departure_date')


class LoginForm(forms.Form):
    username = forms.CharField(max_length=20)
    password = forms.CharField(widget=forms.PasswordInput)
