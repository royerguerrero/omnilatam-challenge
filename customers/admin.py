"""Customers Admin Configuration"""

# Django
from django.contrib import admin

# Models
from customers.models import Customer, ShippingAddress


@admin.register(Customer)
class CustomerModelAdmin(admin.ModelAdmin):
    pass


@admin.register(ShippingAddress)
class ShippingAddressModelAdmin(admin.ModelAdmin):
    pass
