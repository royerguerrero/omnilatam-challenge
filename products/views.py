"""Products views"""

# Django
from django.views.generic import DetailView

# Django Rest Framework
from rest_framework import viewsets, permissions

# Serializers
from products.serializers import ProductSerializer

# Models
from products.models import Product, Category


class ProductViewSet(viewsets.ModelViewSet):
    """Products API ViewSet"""
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    permission_classes = [permissions.IsAuthenticated]

    
class CategoryViewSet(viewsets.ModelViewSet):
    """Category API ViewSet"""
    queryset = Category.objects.all()
    serializer_class = Category
    permission_classes = [permissions.IsAuthenticated]


class CategoryDetailView(DetailView):
    model = Category
    template_name = 'products/category_detail.html'

    def get_context_data(self, **kwargs):   
        context = super(CategoryDetailView, self).get_context_data(**kwargs)
        context['products'] = Product.objects.filter(category=context['category'])
        return context
    