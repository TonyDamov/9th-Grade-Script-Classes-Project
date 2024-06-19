from django.shortcuts import render, redirect
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



def ItemsDetail(request, pk):
    if request.method == 'POST':
        if request.user.is_authenticated:
            user = request.user
            print(user)
            item = Item.objects.get(id=pk)
            Cart.objects.create(user=user,item=item)
            return redirect('products')
    
    elif request.method == 'GET':
        item = Item.objects.get(id=pk)

        return render(request, 'catalogue/item_detail.html', {'title':'Product item.id - Stivans', 'item':item})
    else:
        return redirect('products')

        

def CartsAddOrDel(request, pk):
    if request.method == 'POST':
        if request.user.is_authenticated:
            user = request.user
            print(user)
            item = Item.objects.get(id=pk)
            Cart.objects.create(user=user,item=item)
            return redirect('cart')
        else:
            return redirect('login')
    elif request.method == 'DELETE':
        if user.is_authenticated:
            user = request.user
            item_to_del = Cart.objects.filter(user=user, item=pk).first()
            item_to_del.delete()
            return redirect('cart')
        else:
            return redirect('login')
    else:
        return redirect('cart')


def Carts(request):
    user = request.user
    if user.is_authenticated:
        user_cart = Cart.objects.filter(user=user)

        all = []
        items = []
        counts = []
        ids = []
        for cart in user_cart:
            if cart.item.name not in items:
                items.append(cart.item.name)
                counts.append(1)
                item_id = cart.item.id
                ids.append(item_id)
            else:
                counts[items.index(cart.item.name)] += 1

        for j in range(len(items)):
            all.append({'item': items[j], 'count': counts[j], 'id' : ids[j]})

        return render(request, 'catalogue/cart.html', context={'title':'Cart - Stivans', 'all':all})
