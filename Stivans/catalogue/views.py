from django.shortcuts import render, redirect
from django.http import HttpResponse, JsonResponse
from .models import Item, Cart

# Create your views here.

def Home(request):
    return render(request, 'catalogue/home.html')



def About(request):
    return render(request, 'catalogue/about.html', context={'title':'About - Stivans'})



def Items(request):    
    items = Item.objects.all()
    for item in items:
        item.rating = round(item.rating, 0)
    return render(request, 'catalogue/products.html', context={'title':'Products - Stivans', 'items':items})



def ItemsAddToCart(request, pk):
    if request.method == 'POST':
        if request.user.is_authenticated:
            user = request.user
            print(user)
            item = Item.objects.get(id=pk)
            Cart.objects.create(user=user,item=item)
            return redirect('products')
        else:
            return redirect('login')
    

        


def ItemsDetail(request, pk):

    item = Item.objects.get(id=pk)

    return render(request, 'catalogue/item_detail.html', {'title':'Product item.id - Stivans', 'item':item})



def Carts(request):
    render(request, 'catalogue/cart.html', context={'title':'Cart - Stivans'})
