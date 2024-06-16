from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def Home(request):
    return render(request, 'catalogue/home.html')

def Products(request):
    return render(request, 'catalogue/products.html')

def About(request):
    return render(request, 'catalogue/about.html')