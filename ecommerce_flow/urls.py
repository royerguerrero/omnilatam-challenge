"""Ecommerce Flow URL Configuration"""

# Django
from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings
from django.contrib.auth.views import LogoutView

# Django Rest Framework
from rest_framework import permissions, routers

# DRF YASG (Swagger, Redoc)
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

# Views
from ecommerce_flow import views
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
    path('api/', include(router.urls)),
    path('api/docs/', schema_view.with_ui('swagger', cache_timeout=0), name='docs-swagger'),
    path('api/docs/redoc', schema_view.with_ui('redoc', cache_timeout=0), name='docs-redoc'),
    path('admin/', admin.site.urls, name='admin'),
    path('', views.IndexView.as_view(), name='index'),
    path('login/', views.SingInView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('category/<int:pk>/', products_views.CategoryDetailView.as_view(), name='category_detail'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
