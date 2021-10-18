# Django
from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver 

# Models
from customers.models import Customer
from orders.models import Order, Payment, Shipping, ProductOrder

# Utils
from ecommerce_flow.constants import NOTIFICATION_METHOD_CHOICES 

class Notification(models.Model):
    """Notification Model"""
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    content = models.TextField()

    notification_method = models.CharField(max_length=5, choices=NOTIFICATION_METHOD_CHOICES)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


@receiver(post_save, sender=Shipping)
def send_user_notification_shipment(sender, instance, **kwargs):
    customer = instance.shipping_address.customer
    order = ProductOrder.objects.filter(shipping=instance).select_related('order').first().order

    Notification.objects.create(
        customer=customer,
        title='Your shipment has been updated!',
        content=f'For details go to www.ecomerceflow.com/{order}/track_order/',
        notification_method='email'
    )