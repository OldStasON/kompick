from django.shortcuts import render


# Create your views here.

def index(request):
    context = {'title': 'Kompick', }
    return render(request, 'products/index.html', context)


def laptops(request):
    context = {'title': 'Ноутбуки', }
    return render(request, 'products/laptops.html', context)


def computers(request):
    context = {'title': 'Компьютеры', }
    return render(request, 'products/computers.html', context)


def services(request):
    context = {'title': 'Услуги', }
    return render(request, 'products/services.html', context)


def products(request):
    context = {'title': 'Все категории', }
    return render(request, 'products/products.html', context)
