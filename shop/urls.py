from django.urls import re_path

from . import views

app_name = 'shop'

urlpatterns = [
    re_path(r'^$', views.allProds, name = 'home'),
]