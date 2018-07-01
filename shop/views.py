from django.shortcuts import render

from .models import Category, Product

def index(request):
    return render(request, template_name = 'base.html')
