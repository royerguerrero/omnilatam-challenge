"""Ecommerce Flow URL Configuration"""

# Django
from django.contrib import admin
from django.urls import path, include

# Django Rest Framework
from rest_framework import permissions, routers

# DRF YASG (Swagger, Redoc)
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

# Views
from products import views as products_views


schema_view = get_schema_view(
    openapi.Info(
        title='Ecommerce Flow API',
        default_version='v1',
        contact=openapi.Contact(name='Royer Guerrero', email='royjuni3431@gmail.com'),
        license=openapi.License(name="MIT License")
    ),
    public=True,
    permission_classes=(permissions.AllowAny,)
)

router = routers.DefaultRouter()
router.register('products', products_views.ProductViewSet)
router.register('categories', products_views.CategoryViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),
    path('', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
]
