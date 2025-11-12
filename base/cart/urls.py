from django.urls import path
from . import views

urlpatterns = [
    path("remove/<slug:slug>/", views.remove_from_cart, name="remove_from_cart"),
    path("add/<slug:slug>/", views.add_to_cart, name="add_to_cart"),
    path("cart/", views.get_cart, name="get_cart"),
    path('buy/', views.buy_cart, name="buy_cart")
]
