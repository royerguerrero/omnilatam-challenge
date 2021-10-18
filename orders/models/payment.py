"""Payment Model"""

# Django
from django.db import models

# Models
from orders.models import Order

# Utils 
from ecommerce_flow.constants import CHOICES_PAYMENT_METHODS


class Payment(models.Model):
    """Payment Model"""
    order = models.ForeignKey(Order, on_delete=models.SET_NULL, null=True)

    payment_method = models.CharField(max_length=15, choices=CHOICES_PAYMENT_METHODS)
    approved = models.BooleanField(default=False)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        """Return the default order string representation."""
        return self.order
