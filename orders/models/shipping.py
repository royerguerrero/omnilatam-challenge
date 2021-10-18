"""Shipping Model"""

# Django
from django.db import models

# Models
from customers.models import ShippingAddress

# Utils
from ecommerce_flow.constants import CHOICES_SHIPPING_STATUS

class Shipping(models.Model):
    """Shipping Model"""
    shipping_address = models.ForeignKey(ShippingAddress, on_delete=models.CASCADE)

    status = models.CharField(max_length=50, choices=CHOICES_SHIPPING_STATUS)
    observations = models.TextField()

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
