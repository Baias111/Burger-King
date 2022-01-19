from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
from .models import Category, Product


# Create your views here.


def index(request):
    categories = Category.objects.all()
    return render(request, 'index.html', {'categories': categories})



def products_list(request, slug):
    # product = get_object_or_404(Product, pk=product_id)
    products = Product.objects.filter(category__slug=slug)
    return render(request, 'list.html', {'products': products})


def product_detail(request, product_id):
    product = Product.object.get(pk=product_id)
    return render(request, 'detail.html', locals())
