from django.urls import re_path

from . import views

app_name = 'cart'

urlpatterns = [
    re_path(r'^add/(?P<product_id>\d+)/$', views.add_to_cart, name='add_to_cart'),
    re_path(r'^remove/(?P<product_id>\d+)/$', views.remove_from_cart, name='remove_from_cart'),
    re_path(r'^delete/(?P<product_id>\d+)/$', views.delete_from_cart, name='delete_from_cart'),
    re_path(r'^$', views.cart_detail, name='cart_detail'),
]
