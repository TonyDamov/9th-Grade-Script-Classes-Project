from django import forms
from .models import CustomUser
from django.contrib.auth.forms import UserCreationForm



class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()
    first_name = forms.CharField(max_length=150, required=False)
    last_name = forms.CharField(max_length=150, required=False)
    street_name = forms.CharField(max_length=128, required=False)
    street_number = forms.IntegerField(required=False)
    province = forms.CharField(max_length=256, required=False)
    municipality = forms.CharField(max_length=256, required=False)
    city = forms.CharField(max_length=256, required=False)
    country = forms.CharField(max_length=64, required=False)

    class Meta(UserCreationForm):
        model = CustomUser
        fields = ['username', 'email', 'password1', 'password2', 'first_name', 'last_name', 'street_name', 'street_number', 'province', 'municipality', 'city', 'country']