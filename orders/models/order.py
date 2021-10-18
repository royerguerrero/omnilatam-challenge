"""Orders Models"""

# Django
from django.db import models

# Models
from customers.models import Customer, ShippingAddress
from orders.models import Shipping 
from products.models import Product

# Utils
import uuid


class Order(models.Model):
    """Order Model"""
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    customer = models.ForeignKey(Customer, on_delete=models.SET_NULL, null=True)
    shipping_address = models.ForeignKey(ShippingAddress, on_delete=models.SET_NULL, null=True)

    products = models.ManyToManyField(Product, through='ProductOrder')
    split_payments = models.PositiveSmallIntegerField(default=0)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def get_order_price(self):
        """Returns the order's price"""
        total = 0
        products_through = self.products.through.objects.filter(order=self.id)

        for product_order in products_through:
            total += product_order.price * product_order.quantity

        return total


class ProductOrder(models.Model):
    """ProductOrder model"""
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    shipping = models.ForeignKey(Shipping, on_delete=models.CASCADE, null=True)

    quantity = models.PositiveIntegerField()
    price = models.FloatField()

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.quantity} {self.product} for {self.price}'
