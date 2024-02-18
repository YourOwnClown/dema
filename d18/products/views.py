from django.shortcuts import render

def index(request):
    context ={
        'title':'Рублик'
    }
    return render(request, 'index.html',context=context)

def products(request):
    context = {
        'products': [
            {'image':"/static/vendor/img/products/Adidas-hoodie.png",
             'name':'100-летняя куртка деда',
             'price':'бесценно',
             'description':'Пахнет байкалом'},

        ]



    }
    return render(request, 'products.html', context = context)