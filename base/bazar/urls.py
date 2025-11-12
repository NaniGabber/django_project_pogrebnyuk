from django.urls import path
from . import views
from cart.views import get_cart

urlpatterns = [
    path("products", views.get_products, name = "product_view"),
    path("sections", views.get_sections, name = "section_view"),
    
    path("products/create", views.create_product, name="product_create"),
    path("sections/create", views.create_section, name="section_create"),
    
    path("products/<slug:slug>", views.ProductDetailView.as_view(), name = 'product_detail'),
    path("sections/<slug:slug>", views.SectionDetailView.as_view(), name = 'section_detail'),

    path("products/update/<slug:slug>", views.ProductUpdateView.as_view(), name="product_update"),
    path("sections/update/<slug:slug>", views.SectionUpdateView.as_view(), name="section_update"),

    path("products/delete/<slug:slug>", views.ProductDeleteView.as_view(), name = 'product_delete'),
    path("sections/delete/<slug:slug>", views.SectionDeleteView.as_view(), name = "section_delete"),

]