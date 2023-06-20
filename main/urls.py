from django.urls import path
from .views import IndexView, ProductDetailView
from .api import ProductViewSet, CategoryViewSet
from rest_framework import routers

router = routers.DefaultRouter()

router.register('api/categoty', CategoryViewSet, basename='category')
router.register('api/product', ProductViewSet, basename='product')


urlpatterns = [
    path('', IndexView, name='index'),
    path('product/<slug:slug>/', ProductDetailView, name='product_detail'),
]

urlpatterns += router.urls