from django.db import models


class Order(models.Model):
    payment_id = models.CharField(max_length=255)
    total = models.DecimalField(max_digits=12, decimal_places=2, verbose_name='Order total (INR)')

    created = models.DateTimeField(auto_now_add=True)

    emailAddress = models.EmailField(max_length=255, verbose_name='E-mail Address')
    shippingName = models.CharField(max_length=255)
    shippingAddressLine1 = models.CharField(max_length=255)
    shippingAddressLine2 = models.CharField(max_length=255)
    shippingState = models.CharField(max_length=255)
    shippingCity = models.CharField(max_length=255)
    shippingPincode = models.CharField(max_length=50)

    class Meta:
        verbose_name = 'Order'
        verbose_name_plural = 'Orders'
        db_table = 'Order'
        ordering = ['created', ]

    def __str__(self):
        return str(self.id)


class OrderItem(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE)

    product = models.CharField(max_length=255)
    quantity = models.PositiveIntegerField()
    price = models.DecimalField(max_digits=12, decimal_places=2, verbose_name='Product Price (INR)')

    class Meta:
        db_table = 'OrderItem'
        verbose_name = 'Order Item'
        verbose_name_plural = 'Order Items'

    def sub_total(self):
        return self.quantity * self.price

    def __str__(self):
        return self.product
