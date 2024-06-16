from django.contrib import admin

# Register your models here.

from django.contrib import admin
from .models import CustomUser

@admin.register(CustomUser)
class CustomUserAdmin(admin.ModelAdmin):
    list_display = ['username', 'email', 'first_name', 'last_name', 'street_name', 'street_number', 'province', 'municipality', 'city', 'country']
    # Add any other details you want to display in the list
