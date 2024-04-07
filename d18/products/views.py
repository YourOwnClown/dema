from django.shortcuts import render,HttpResponseRedirect,reverse

from .models import *


def index(request):
    context ={
        'title':'Рублик'
    }
    return render(request, 'index.html',context=context)

def products(request):
    context = {
            'title':'magazik',
            'products' : Product.objects.all(),
            'categories': ProductCategory.objects.all(),

        }
    return render(request, 'products.html', context=context)

def basket_add(request, product_id:id):
    product = Product.objects.get(id = product_id)
    baskets = Basket.objects.filter(user = request.user, product=product)

    if not baskets.exists():
        Basket.objects.create(user = request.user, product = product, quantity = 1)
    else:
        basket = baskets.first()
        basket.quantity += 1
        basket.save()

    return HttpResponseRedirect(request.META['HTTP_REFERER'])

def basket_remove(request, basket_id):
    basket = Basket.objects.get(id = basket_id)
    basket.delete()
    return HttpResponseRedirect(request.META['HTTP_REFERER'])






