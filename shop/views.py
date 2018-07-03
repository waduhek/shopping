from django.shortcuts import render, get_object_or_404

from .models import Category, Product

def allProds(request, cat_slug = None):
    product_list = None
    cat_page = None

    if cat_slug != None:
        cat_page = get_object_or_404(Category, slug = cat_slug)
        product_list = Product.objects.all().filter(category = cat_page, available = True)

    else:
        product_list = Product.objects.all().filter(available = True)

    return render(request, 'shop/category.html')
