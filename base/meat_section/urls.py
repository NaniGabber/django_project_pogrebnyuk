from django.urls import path
from . import views

urlpatterns = [
    path("/products", views.get_products, name = "product_view"),
    path("/sections", views.get_sections, name = "section_view")

]