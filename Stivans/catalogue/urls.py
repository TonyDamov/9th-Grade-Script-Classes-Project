from django.urls import path
from . import views as catalogue_views

urlpatterns = [
    path('', catalogue_views.Home, name='home'),
    path('products/', catalogue_views.Products, name='products'),
    path('about/', catalogue_views.About, name='about'),

]