from django.shortcuts import render, HttpResponse, redirect
from .models import Product, Category, Review
from .forms import ReviewCreateForm, ProductCreateForm
import datetime

# Create your views here.

PAGINATION_LIMIT = 3


def main_view(request):
    return render(request, 'layouts/index.html')


def products_view(request):
    if request.method == "GET":
        products = Product.objects.all()
        category_id = int(request.GET.get('category_id', 0))
        text = request.GET.get('text')
        page = int(request.GET.get('page', 1))

        if category_id:
            products = Product.objects.filter(hastsag_in=[category_id])
        else:
            post = Product.objects.all()
        if text:
            products = Product.objects.filter(title_icontains=text)

        max_page = products.__len__() / PAGINATION_LIMIT

        if round(max_page) < max_page:
            max_page = round(max_page) + 1

        max_page = int(max_page)
        products = products[PAGINATION_LIMIT * (page - 1):PAGINATION_LIMIT * page]

        return render(request, 'products/products.html', context={
            'products': products,
            'user': None if request.user.is_anonymous else request.user,
            'pages': range(1, max_page + 1)
        })


def product_review_view(request, id):
    if request.method == 'GET':
        product = Product.objects.get(id=id)
        form = ReviewCreateForm(data=request.POST)

        context = {
            'product': product,
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
                'category': product.hashtags.all(),
                'review_form': ReviewCreateForm
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
            author=request.user,
            name=request.POST.get('name'),
            description=request.POST.get('description'),
            price=request.POST.get('price')
        )
        return redirect('/products/')



