from django.urls import re_path

from . import views

app_name = 'signin'

urlpatterns = [
    re_path(r'^$', views.signinView, name = 'login'),
    re_path(r'^signup/$', views.signupView, name = 'signup'),
    re_path(r'^signout/$', views.signoutView, name = 'signout'),
]