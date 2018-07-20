from django.shortcuts import render, redirect, get_object_or_404
from django.core.exceptions import ObjectDoesNotExist
from django.contrib.auth.models import User

from .models import Cart, CartItem, Address
from .forms import AddressForm
from shop.models import Product
from order.models import Order, OrderItem


def _cart_id(request):
    cart = request.session.session_key

    if not cart:
        cart = request.session.create()

    return cart


def add_to_cart(request, product_id):
    product = Product.objects.get(id=product_id)

    try:
        cart = Cart.objects.get(cart_id=_cart_id(request))
    except Cart.DoesNotExist:
        cart = Cart.objects.create(cart_id=_cart_id(request))
        cart.save()

    try:
        cart_item = CartItem.objects.get(product=product, cart=cart)

        if cart_item.quantity < cart_item.product.stock:
            cart_item.quantity += 1

        cart_item.save()

    except CartItem.DoesNotExist:
        cart_item = CartItem.objects.create(
            product=product,
            quantity=1,
            cart=cart
        )

        cart_item.save()

    return redirect('cart:cart_detail')


def remove_from_cart(request, product_id):
    cart = Cart.objects.get(cart_id=_cart_id(request))
    product = get_object_or_404(Product, id=product_id)
    cart_item = CartItem.objects.get(product=product, cart=cart)

    if cart_item.quantity > 1:
        cart_item.quantity -= 1
        cart_item.save()

    else:
        cart_item.delete()

    return redirect('cart:cart_detail')


def delete_from_cart(request, product_id):
    cart = Cart.objects.get(cart_id=_cart_id(request))
    product = get_object_or_404(Product, id=product_id)
    cart_item = CartItem.objects.get(product=product, cart=cart)

    cart_item.delete()

    return redirect('cart:cart_detail')


def cart_detail(request, total=0, cart_items=None, address_id=None):
    try:
        cart = Cart.objects.get(cart_id=_cart_id(request))
        cart_items = CartItem.objects.filter(cart=cart, active=True)

        for cart_item in cart_items:
            total += (cart_item.quantity * cart_item.product.price)

    except ObjectDoesNotExist:
        pass

    if request.method == 'POST':
        print(request.POST)

        user = User.objects.get(username=request.user)
        emailAddress = user.email

        address = Address.objects.get(id=address_id)
        name = address.name
        addressLine1 = address.addressLine1
        addressLine2 = address.addressLine2
        state = address.state
        city = address.city
        pincode = address.pincode

        razorpay_payment_id = request.POST['razorpay_payment_id']

        new_order = Order.objects.create(
            payment_id=razorpay_payment_id,
            total=total,
            shippingName=name,
            shippingAddressLine1=addressLine1,
            shippingAddressLine2=addressLine2,
            shippingState=state,
            shippingCity=city,
            shippingPincode=pincode,
            emailAddress=emailAddress
        )
        new_order.save()

        for item in cart_items:
            order_item = OrderItem.objects.create(
                order=new_order,
                product=item.product.name,
                quantity=item.quantity,
                price=item.product.price
            )
            order_item.save()

            products = Product.objects.get(id=item.product.id)
            products.stock = int(item.product.stock - item.quantity)
            products.save()

            item.delete()

        return redirect('order:thanks', new_order.id)

    return render(request, 'cart.html', dict(
        cart_items=cart_items,
        total=total,
    ))


def addAddress(request):
    saved_addresses = None

    try:
        user = User.objects.get(username=request.user)
        saved_addresses = Address.objects.filter(user=user)
    except Exception:
        pass

    if request.method == "POST":
        new_address = AddressForm(request.POST)

        if new_address.is_valid():
            new_address.save(request)

    else:
        new_address = AddressForm()

    return render(request, 'address/address.html', dict(saved_addresses=saved_addresses, new_address=new_address))


def deleteAddress(request, address_id):
    user = User.objects.get(username=request.user)
    address = Address.objects.get(user=user, id=address_id)

    address.delete()

    return redirect('cart:add_address')
