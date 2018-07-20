from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import login_required

from order.models import Order, OrderItem


def thankYou(request, order_id):
    if order_id:
        customer_order = get_object_or_404(Order, id=order_id)

    return render(request, 'thanks.html', {'customer_order': customer_order, })


@login_required(login_url='/signin/')
def orderHistory(request):
    email = str(request.user.email)
    order_list = Order.objects.filter(emailAddress=email)

    return render(request, 'order/order_list.html', {'order_list': order_list, })


@login_required(login_url='/signin/')
def orderHistoryDetail(request, order_id):
    email = str(request.user.email)
    order = Order.objects.get(id=order_id, emailAddress=email)
    order_detail = OrderItem.objects.filter(order=order)

    return render(request, 'order/order_detail.html', dict(order=order, order_detail=order_detail))
