from django.urls import path
from . import views as catalogue_views

urlpatterns = [
    path('', catalogue_views.Home, name='home'),
    path('products/', catalogue_views.Items, name='products'),
    path('products/<int:pk>/', catalogue_views.ItemsAddToCart, name='add-to-cart'),
    path('products/<int:pk>/details/', catalogue_views.ItemsDetail, name='products-detail'),
    path('about/', catalogue_views.About, name='about'),
    path('cart/', catalogue_views.Cart, name='cart'),
]