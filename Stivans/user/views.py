from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib import messages
from .forms import UserRegisterForm
from .models import CustomUser
# Create your views here.

def Register(request):
#    if request.user.is_authenticated():
#        return redirect()
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()

            username = form.cleaned_data.get('username')
            messages.success(request, f'Your account has been created! You are now able to log in')
            return redirect('login')
    else:
        form = UserRegisterForm()

    return render(request, 'user/register.html', {'form': form})

#def Login(request):
    #return HttpResponse('      ')