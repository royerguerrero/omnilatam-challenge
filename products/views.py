"""Products views"""

# Django
from django.views.generic import DetailView

# Django Rest Framework
from rest_framework import viewsets, permissions, filters
from django_filters.rest_framework import DjangoFilterBackend

# Serializers
from products.serializers import ProductSerializer

# Models
from products.models import Product, Category


class ProductViewSet(viewsets.ModelViewSet):
    """Products API ViewSet"""
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    permission_classes = [permissions.IsAuthenticated, permissions.IsAdminUser]
    filter_backends = [DjangoFilterBackend, filters.SearchFilter]
    filterset_fields = ['category', 'published', 'stock', 'created_at', 'updated_at',]
    search_fields = ['name', 'description', 'category__name', 'category__description', 'stock']

    
class CategoryViewSet(viewsets.ModelViewSet):
    """Category API ViewSet"""
    queryset = Category.objects.all()
    serializer_class = Category
    permission_classes = [permissions.IsAuthenticated, permissions.IsAdminUser]
    filter_backends = [DjangoFilterBackend, filters.SearchFilter]
    filterset_fields = ['created_at', 'updated_at',]
    search_fields = ['name', 'description',] 

class CategoryDetailView(DetailView):
    model = Category
    template_name = 'products/category_detail.html'

    def get_context_data(self, **kwargs):   
        context = super(CategoryDetailView, self).get_context_data(**kwargs)
        context['products'] = Product.objects.filter(category=context['category'])
        return context
    