from django.shortcuts import render


# Create your views here.

def index(request):
    context = {'title': 'Kompick',}
    return render(request, 'products/index.html', context)


def products(request):
    return render(request, 'products/products.html')


def laptops(request):
    return render(request, 'products/laptops.html')


def computers(request):
    return render(request, 'products/computers.html')


def services(request):
    return render(request, 'products/services.html')
