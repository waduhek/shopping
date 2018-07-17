from django.shortcuts import render, redirect, get_object_or_404
from django.core.exceptions import ObjectDoesNotExist

from .models import Cart, CartItem, Address
from .forms import AddressForm
from shop.models import Product


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


def cart_detail(request, total=0, counter=0, cart_items=None):
    try:
        cart = Cart.objects.get(cart_id=_cart_id(request))
        cart_items = CartItem.objects.filter(cart=cart, active=True)

        for cart_item in cart_items:
            total += (cart_item.quantity * cart_item.product.price)
            counter += cart_item.quantity

    except ObjectDoesNotExist:
        pass

    razorpay_total = total * 100

    if request.method == 'POST':
        print(request.POST)

    return render(request, 'cart.html', dict(
        cart_items=cart_items,
        total=total,
        counter=counter,
        razorpay_total=razorpay_total
    ))


def addAddress(request):
    saved_addresses = None

    try:
        saved_addresses = Address.objects.get(user__username=request.user)
    except ObjectDoesNotExist:
        pass

    if request.method == "POST":
        new_address = AddressForm(request.POST)

        if new_address.is_valid():
            new_address.save()

    else:
        new_address = AddressForm()

    return render(request, 'address/address.html', dict(saved_addresses=saved_addresses, new_address=new_address))


def deleteAddress(request, address_id):
    address = Address.objects.get(user__username=request.user, id=address_id)

    address.delete()

    return redirect('cart:add_address')
