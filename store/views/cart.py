from django.shortcuts import render, redirect
from django.contrib.auth.hashers import check_password
from store.models import Customer
from django.views import View
from store.models.products import Product


class Cart(View):

    def get(self, request):

        cart = request.session.get("cart")
        print("In cart >>>>>>>>>>>>>>>>> ", cart)

        products = None
        if cart:
            cart_id = cart.keys()
            products = Product.get_cart_product(cart_id)

        return render(request, "store/cart.html", {"products": products})



