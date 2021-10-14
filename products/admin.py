"""Products Admin Configuration"""

# Django
from django.contrib import admin

# Models
from products.models import Product, Category


@admin.register(Product)
class ProductAdminModel(admin.ModelAdmin):
    list_display = ('name', 'price', 'category', 'stock', 'published', 'created_at', 'updated_at')
    list_display_links = ('name', 'price', 'category', 'stock', 'published', 'created_at', 'updated_at')
    list_filter = ('category', 'published',)  
    readonly_fields = ('created_at', 'updated_at')
    search_fields = ('name', 'description')


@admin.register(Category)
class CatogoryModelAdmin(admin.ModelAdmin):
    list_display = ('name', 'description', 'created_at', 'updated_at')
    list_display_links = ('name', 'description', 'created_at', 'updated_at')
    readonly_fields = ('created_at', 'updated_at')
    search_fields = ('name', 'description')
