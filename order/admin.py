from django.contrib import admin

from .models import Order, OrderItem


class OrderItemAdmin(admin.TabularInline):
    model = OrderItem

    fieldsets = [
        ('Product', {'fields': ['product', ], }, ),
        ('Quantity', {'fields': ['quantity', ], }, ),
        ('Price', {'fields': ['quantity', ], }, ),
    ]

    readonly_fields = ['product', 'quantity', 'price', ]
    can_delete = False
    max_num = 0

    template = 'admin/order/tabular.html'


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = [
        'id',
        'shippingName',
        'shippingState',
        'shippingCity',
        'shippingPincode',
        'emailAddress',
        'created',
    ]
    list_display_links = ['id', 'shippingName', ]
    search_fields = ['id', 'shippingName', ]
    readonly_fields = [
        'id',
        'payment_id',
        'created',
        'total',
        'emailAddress',
        'shippingName',
        'shippingAddressLine1',
        'shippingAddressLine2',
        'shippingState',
        'shippingCity',
        'shippingPincode',
    ]

    fieldsets = [
        ('ORDER INFORMATION', {'fields': ['id', 'payment_id', 'total', 'created', ], }, ),
        ('SHIPPING INFORMATION', {'fields': ['shippingName', 'shippingAddressLine1', 'shippingAddressLine2', 'shippingState', 'shippingCity', 'shippingPincode', 'emailAddress', ], }, ),
    ]

    inlines = [
        OrderItemAdmin,
    ]

    def has_delete_permission(self, request, obj=None):
        return False

    def has_add_permission(self, request):
        return False
