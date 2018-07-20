from django.urls import re_path

from . import views

app_name = 'order'

urlpatterns = [
    re_path(r'^thank-you/(?P<order_id>\d+)/$', views.thankYou, name='thanks'),
    re_path(r'^order-history/$', views.orderHistory, name='order_history'),
    re_path(r'^order-history/view-order/(?P<order_id>\d+)/$', views.orderHistoryDetail, name='order_history_detail'),
]
