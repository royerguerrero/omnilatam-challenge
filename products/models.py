"""Produts Models"""

# Django
from django.db import models


class Category(models.Model):
    """Category Model"""
    name = models.CharField(max_length=150)
    description = models.TextField(blank=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name_plural = 'categories'

    def __str__(self):
        """Returs category name"""
        return str(self.name)


class Product(models.Model):
    """Product Model"""
    name = models.CharField(max_length=150)
    description = models.TextField(blank=True)
    price = models.FloatField()

    category = models.ForeignKey(Category, on_delete=models.CASCADE)

    stock = models.PositiveIntegerField(default=0)
    published = models.BooleanField(default=False)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        """Returs product name"""
        return str(self.name)
