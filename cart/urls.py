from django.urls import re_path

from . import views

app_name = 'cart'

urlpatterns = [
    re_path(r'^add/(?P<product_id>\d+)/$', views.add_to_cart, name='add_to_cart'),
    re_path(r'^remove/(?P<product_id>\d+)/$', views.remove_from_cart, name='remove_from_cart'),
    re_path(r'^delete/(?P<product_id>\d+)/$', views.delete_from_cart, name='delete_from_cart'),
    re_path(r'^checkout/add-address/$', views.addAddress, name='add_address'),
    re_path(r'^checkout/add-address/(?P<address_id>\d+)', views.cart_detail, name='checkout_success'),
    re_path(r'^checkout/delete-address/(?P<address_id>\d+)/$', views.deleteAddress, name='delete_address'),
    re_path(r'^$', views.cart_detail, name='cart_detail'),
]
