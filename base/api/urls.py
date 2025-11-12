from django.urls import path
from .views import ProductListAPIView, ProductDetailAPIView

urlpatterns = [
    path('product/', ProductListAPIView.as_view(), name='product-list'),
    path('product/<int:pk>/', ProductDetailAPIView.as_view(), name='product-detail'),
]
