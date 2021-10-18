"""Produts Models"""

# Django
from django.db import models


class Category(models.Model):
    """Category Model"""
    name = models.CharField(max_length=150)
    description = models.TextField(blank=True)
    picture = models.ImageField(upload_to='categories')

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name_plural = 'categories'

    def __str__(self):
        """Returns category name"""
        return str(self.name)


class Product(models.Model):
    """Product Model"""
    name = models.CharField(max_length=150)
    description = models.TextField(blank=True)
    price = models.FloatField()

    picture1 = models.ImageField(upload_to='products')
    picture2 = models.ImageField(upload_to='products')
    picture3 = models.ImageField(upload_to='products')
    # TODO: Add validator for youtube video
    video = models.URLField()

    category = models.ForeignKey(Category, on_delete=models.CASCADE)

    stock = models.PositiveIntegerField(default=0)
    published = models.BooleanField(default=False)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        """Returns product name"""
        return str(self.name)
