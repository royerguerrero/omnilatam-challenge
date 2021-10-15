"""Orders Admin Configuration"""

# Django
from django.contrib import admin

# Models
from orders.models import Order, ProductOrder, Shipping, Payment


@admin.register(Order)
class OrderModelAdmin(admin.ModelAdmin):
    pass


@admin.register(Shipping)
class ShippingModelAdmin(admin.ModelAdmin):
    pass


@admin.register(Payment)
class PaymentModelAdmin(admin.ModelAdmin):
    pass

