from .models import *
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class RegisterForm(UserCreationForm):
    email = forms.EmailField(label = "Email")
    first_name = forms.CharField(label = "First name")

    class Meta:
        model = User
        fields = ("username", "first_name", "email",'password1','password2' )

class travelForm(forms.ModelForm):
    class Meta:
        model=Bus
        fields='__all__'