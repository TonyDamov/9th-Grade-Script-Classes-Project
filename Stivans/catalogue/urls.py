from django.urls import path
from . import views as catalogue_views

urlpatterns = [
    path('', catalogue_views.Home, name='home'),
    path('products/', catalogue_views.Items, name='products'),
    path('products/<int:pk>/', catalogue_views.ItemsDetail, name='products-detail'),
    path('about/', catalogue_views.About, name='about'),
    path('cart/', catalogue_views.Carts, name='cart'),
    path('cart/<int:pk>/', catalogue_views.CartsAddOrDel, name='cart-functions'),
]