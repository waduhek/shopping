from django.db import models
from django.contrib.auth.models import User

from shop.models import Product


class Cart(models.Model):
    cart_id = models.CharField(max_length=250, blank=True)
    date_added = models.DateField(auto_now_add=True)

    class Meta:
        db_table = 'Cart'

    def __str__(self):
        return self.cart_id


class CartItem(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField()
    active = models.BooleanField(default=True)

    class Meta:
        db_table = 'CartItem'

    def subTotal(self):
        return self.quantity * self.product.price

    def __str__(self):
        return self.product


class Address(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    addressLine1 = models.CharField(max_length=255)
    addressLine2 = models.CharField(max_length=255)
    state = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    pincode = models.CharField(max_length=50)

    class Meta:
        db_table = 'Address'

    def __str__(self):
        return "Address:", self.user.name
