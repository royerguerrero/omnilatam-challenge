"""Shipping Model"""

# Django
from django.db import models

# Models
from customers.models import ShippingAddress

class Shipping(models.Model):
    """Shipping Model"""
    shipping_address = models.ForeignKey(ShippingAddress, on_delete=models.CASCADE)
    
    CHOICES_TYPE = [
        ('awaiting_payment', 'Waiting for payment'),
        ('failed_payment', 'Failed payment'),
        ('preparing_shipment', 'Preparing shipment'),
        ('on_the_way', 'On the way'),
        ('delivery_refused', 'Returned order'),
        ('delivered', 'Delivered'),
    ]

    status = models.CharField(max_length=50, choices=CHOICES_TYPE)
    observations = models.TextField()

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
