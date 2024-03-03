from django.shortcuts import render

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






    return render(request, 'products.html', context = context)