
from django.shortcuts import render, redirect
from store.models import Product, Category
from django.views import View
from django.views.decorators.csrf import csrf_exempt


class Index(View):

    def get(self, request):

        if dict(request.session):
            if request.session.get("customer_email"):
                print(request.session["customer_email"])
            else:
                print("In session email not set.")
        else:
            print("Session not set.")

        category_list = Category.get_all_category()

        category_id = request.GET.get('category')

        product_list = None
        if category_id:
            product_list = Product.get_product_by_category_id(category_id)
        else:
            product_list = Product.get_all_product()

        data = {"products": product_list,
                "categories": category_list,
                "sdata": dict(request.session)}

        return render(request, "store/index.html", data)

    @csrf_exempt
    def post(self, request):
        product_id = request.POST.get("product_id")

        cart = request.session.get('cart')

        if cart:
            quantity = cart.get(product_id)
            if quantity:
                cart[product_id] = cart[product_id] + 1
            else:
                cart[product_id] = 1
        else:
            cart = {product_id: 1}

        request.session['cart'] = cart

        return redirect("store:index")


# def index(request):
#     # print(dict(request.session))
#     if dict(request.session):
#         print(request.session["customer_email"])
#     else:
#         print("Session not set")
#     # print(dict(request.session))
#     category_list = Category.get_all_category()
#
#     category_id = request.GET.get('category')
#
#     product_list = None
#     if category_id:
#         product_list = Product.get_product_by_category_id(category_id)
#     else:
#         product_list = Product.get_all_product()
#
#     data = {"products": product_list, "categories": category_list}
#
#     return render(request, "store/index.html", data)



