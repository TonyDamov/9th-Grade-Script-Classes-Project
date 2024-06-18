from django import forms
from .models import CustomUser
from django.contrib.auth.forms import UserCreationForm


class UserLoginForm(forms.ModelForm):
    username = forms.CharField(max_length=150)
    password = forms.CharField(widget=forms.PasswordInput())

    class Meta:
        model = CustomUser
        fields = ['username', 'password']


class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()
    first_name = forms.CharField(max_length=150)
    last_name = forms.CharField(max_length=150)
    street_name = forms.CharField(max_length=128)
    street_number = forms.IntegerField()
    province = forms.CharField(max_length=256)
    municipality = forms.CharField(max_length=256)
    city = forms.CharField(max_length=256)
    country = forms.CharField(max_length=64)

    class Meta(UserCreationForm):
        model = CustomUser
        fields = ['username', 'email', 'password1', 'password2', 'first_name', 'last_name', 'street_name', 'street_number', 'province', 'municipality', 'city', 'country']



class UserUpdateForm(forms.ModelForm):
    class Meta:

        model = CustomUser
        fields = ['first_name', 'last_name', 'street_name', 'street_number', 'province', 'municipality', 'city', 'country']
