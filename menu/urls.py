from django.urls import path
from . import views

app_name = "menu"
urlpatterns = [
    path("", views.index, name="index"),
    path("cart", views.cart, name="cart"),
    path("add/<int:snack_id>", views.add_to_cart, name="add_to_cart")
]