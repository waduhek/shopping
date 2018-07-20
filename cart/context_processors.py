from django.core.exceptions import ObjectDoesNotExist

from .models import Cart, CartItem
from .views import _cart_id


def getRazorpayTotal(request):
    total = 0
    counter = 0

    try:
        cart = Cart.objects.get(cart_id=_cart_id(request))
        cart_items = CartItem.objects.filter(cart=cart, active=True)

        for cart_item in cart_items:
            total += (cart_item.quantity * cart_item.product.price)
            counter += cart_item.quantity

    except ObjectDoesNotExist:
        pass

    razorpay_total = total * 100

    return dict(
        counter=counter,
        razorpay_total=razorpay_total
    )
