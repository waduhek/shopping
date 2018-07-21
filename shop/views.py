from django.shortcuts import render, get_object_or_404

from .models import Category, Product


def allProds(request, category_slug=None):
    product_list = None
    category_page = None

    if category_slug is not None:
        category_page = get_object_or_404(Category, slug=category_slug)
        product_list = Product.objects.filter(category=category_page, available=True)

    else:
        product_list = Product.objects.all().filter(available=True).order_by('-created')[:9]

    return render(request, 'shop/category.html', {'category': category_page, 'product_list': product_list})


def prodDetail(request, category_slug, product_slug):
    try:
        product = Product.objects.get(category__slug=category_slug, slug=product_slug)
    except Exception as e:
        raise e

    return render(request, 'shop/product-detail.html', {'product': product})
