# Django
from django.db import models

# Models
from customers.models import Customer

# Utils
from ecommerce_flow.constants import NOTIFICATION_METHOD_CHOICES 

class Notification(models.Model):
    """Notification Model"""
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    content = models.TextField()

    notification_method = models.CharField(max_length=5, choices=NOTIFICATION_METHOD_CHOICES)

    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)
