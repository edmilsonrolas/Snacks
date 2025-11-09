from django.shortcuts import render, redirect
from django import forms

menu = [
    {"id": 1, "name": "Pão com ovo", "price": 25},
    {"id": 2, "name": "Pão com Chouriço", "price": 30},
    {"id": 3, "name": "Bolo de amendoim", "price": 30},
    {"id": 4, "name": "Bolo de Milho", "price": 25},
    {"id": 5, "name": "Sumo Natural", "price": 40},
    {"id": 6, "name": "Chamuças", "price": 10}
]

# class AddToCartForm(forms.Form):
#     snack_id

# Create your views here.
def index(request):
    return render(request, "menu/index.html", {
        "menu": menu
    })

def cart(request):
    return render(request, "menu/cart.html", {
        "cart": request.session["cart"]
    })

def add_to_cart(request, snack_id):
    cart = request.session.get("cart", [])  #obtem a key "cart" ou uma lista vazia []
    snack = next((item for item in menu if snack_id == item["id"]), None)
    if snack:
        cart.append(snack)
        request.session["cart"] = cart
    return redirect("menu:cart")