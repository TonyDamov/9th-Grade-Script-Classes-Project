from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import Cart, Item

@admin.register(Cart)
class CartAdmin(admin.ModelAdmin):
    list_display = ['user', 'item']
    # Add any other details you want to display in the list



@admin.register(Item)
class ItemAdmin(admin.ModelAdmin):
    list_display = ['rating', 'image', 'name', 'description', 'price']
    # Add any other details you want to display in the list