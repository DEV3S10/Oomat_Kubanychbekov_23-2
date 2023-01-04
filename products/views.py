from django.shortcuts import render, HttpResponse, redirect
from .models import Product, Category
import datetime

# Create your views here.


def main_view(request):
    return render(request, 'layouts/index.html')


def products_view(request):
    if request.method == 'GET':
        products = Product.objects.all()

        return render(request, 'products/products.html', context={
            'products': products
        })


def product_review_view(request, id):
    if request.method == 'GET':
        product = Product.objects.get(id=id)

        return render(request, 'products/product_review.html', context={
            'product': product,
            'category': product.category.title
        })


def category_view(request):
    if request.method == "GET":
        categorys = Category.objects.all()

        return render(request, 'category/index.html', context={
            'categorys': categorys
        })
