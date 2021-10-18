"""Ecommerce Flow URL Configuration"""

# Django
from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings
from django.contrib.auth.views import LogoutView, LoginView

# Django Rest Framework
from rest_framework import permissions, routers

# DRF YASG (Swagger, Redoc)
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

# Views
from ecommerce_flow import views
from products import views as products_views
from customers import views as customer_views
from orders import views as order_views

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
router.register('products', products_views.ProductViewSet, 'products_viewset')
router.register('categories', products_views.CategoryViewSet, 'categories_viewset')
router.register('customers', customer_views.CustomerViewSet, 'customers_viewset')
router.register('orders', order_views.OrderViewSet, 'orders_viewset')
router.register('payments', order_views.PaymentViewSet, 'payment_viewset')
router.register('shippings', order_views.ShippingViewSet, 'shipping_viewset')

urlpatterns = [
    path('api/', include(router.urls)),
    path('api/docs/', schema_view.with_ui('swagger', cache_timeout=0), name='docs-swagger'),
    path('api/docs/redoc', schema_view.with_ui('redoc', cache_timeout=0), name='docs-redoc'),
    path('admin/', admin.site.urls, name='admin'),
    path('', views.IndexView.as_view(), name='index'),
    path('login/', LoginView.as_view(template_name='login.html'), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('category/<int:pk>/', products_views.CategoryDetailView.as_view(), name='category_detail'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
