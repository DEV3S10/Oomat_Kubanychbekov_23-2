from django.shortcuts import render, HttpResponse, redirect
from .models import Product, Category, Review
from .forms import ReviewCreateForm, ProductCreateForm
import datetime

# Create your views here.


def main_view(request):
    return render(request, 'layouts/index.html')


def products_view(request):
    if request.method == 'GET':
        products = Product.objects.all()
        category_id = int(request.GET.get('category', 0))
        text = request.GET.get('text')

        if category_id:
            products = Product.objects.filter(category_in=[category_id])
        else:
            product = Product.objects.all()
        if text:
            products = Product.objects.filter(title_icontains=text)

        return render(request, 'products/products.html', context={
            'products': products
        })


def product_review_view(request, id):
    if request.method == 'GET':
        product = Product.objects.get(id=id)
        form = ReviewCreateForm(data=request.POST)

        context = {
            'post': product,
            'review': product.comment.set.all(),
            'category': product.hashtags.all(),
            'comment form': ReviewCreateForm
        }

        return render(request, 'products/product_review.html', context=context)

    if request.method == 'POST':
        product = Product.objects.get(id=id)
        form = ReviewCreateForm(date=request.POST)

        if form.is_valid():
            Review.objects.create(
                product_id=id,
                text=form.cleaned_data.get('text')
            )
            return redirect(f'/products/{id}/')
        else:
            return render(request, 'products/product_review.html', context={
                'product': product,
                'comments': product.comment_set.all(),
                'hastahs': product.hashtags.all(),
                'comment form': ReviewCreateForm
            })


def category_view(request):
    if request.method == "GET":
        categorys = Category.objects.all()

        return render(request, 'category/index.html', context={
            'categorys': categorys
        })


def product_create_view(request):
    if request.method == 'GET':
        return render(request, 'products/create.html', context={
            'form': ProductCreateForm
        })

    if request.method == "POST":
        errors = {}

        if len(request.POST.get('name')) < 1:
            errors['name_error'] = 'min length is 1'

        if len(request.POST.get('description')) < 1:
            errors['description_error'] = 'min length is 1'

        if len(errors.keys()) > 0:
            return render(request, 'products/create.html', context=errors)

        Product.objects.create(
            name=request.POST.get('name'),
            description=request.POST.get('description'),
            price=request.POST.get('price')
        )
        return redirect('/products/')



