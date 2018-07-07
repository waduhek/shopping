from django.urls import re_path

from . import views

app_name = 'shop'

urlpatterns = [
    re_path(r'^(?P<category_slug>\w+)/$', views.allProds, name = 'products_by_category'),
    re_path(r'^(?P<category_slug>\w+)/(?P<product_slug>[\w-]+)/$', views.prodDetail, name = 'product_detail'),
    re_path(r'^$', views.allProds, name = 'home'),
]