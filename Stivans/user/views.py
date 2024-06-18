from django.shortcuts import render, redirect
from .models import CustomUser
from django.http import HttpResponse
from django.contrib import messages
from .forms import UserRegisterForm, UserUpdateForm, UserLoginForm
from django.contrib.auth.views import LoginView
from django.contrib.auth import authenticate, login
from django.contrib.auth.hashers import check_password


# Create your views here.

def Register(request):
    if request.user.is_authenticated:
        return redirect('home')
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()

            username = form.cleaned_data.get('username')
            messages.success(request, f'Your account has been created! You are now able to log in')
            return redirect('login')
    else:
        form = UserRegisterForm()

    return render(request, 'user/register.html', {'form': form, 'title':'Register - Stivans'})

def EditUser(request):
    if request.method == 'POST':
        form = UserUpdateForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            messages.success(request, f'Your account has been edited!')
            return redirect('profile')
    else:
        form = UserUpdateForm(instance=request.user)

    return render(request, 'user/profile.html', {'form' : form, 'title':'User profile - Stivans'})