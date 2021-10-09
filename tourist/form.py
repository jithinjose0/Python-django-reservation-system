
from django import forms
from django.db.models import fields
from myapp.models import tourist
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class touristForm(forms.ModelForm):
    class Meta:
        model=tourist
        fields='__all__'


class RegisterForm(UserCreationForm):
    email = forms.EmailField(label = "Email")
    first_name = forms.CharField(label = "First name")

    class Meta:
        model = User
        fields = ("username", "first_name", "email",'password1','password2' )