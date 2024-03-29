from django.shortcuts import render, redirect
from store.models import Product, Category, Customer
from django.views import View


class Index(View):
    def get(self, request):

        # request.session["Hello"] = "This is homepage"

        # print("This is method : ", request.method)
        # print("This is post : ", request.POST)
        # print("This is get : ", dict(request.GET))
        # print("This is session : ", dict(request.session))

        # print(">>>>>>>>>>>>>>>>>>>>>>", request.session['customer_email'])
        print(type(request))
        print(request)
        user = None
        if dict(request.session):
            if request.session.get("customer_email"):
                user = Customer.objects.get(email=request.session.get('customer_email'))
                print(request.session["customer_email"])
            else:
                print("In session email not set.")
        else:
            print("Session not set.")

        category_list = Category.get_all_category()

        category_id = request.GET.get('category')

        product_list = None
        category = None
        if category_id:
            product_list = Product.get_product_by_category_id(category_id)
            category = category_id
        else:
            product_list = Product.get_all_product()

        data = {"products": product_list,
                "categories": category_list,
                "sdata": dict(request.session),
                'category': category,
                'user': user}

        return render(request, "store/index.html", data)

    def post(self, request):
        # print("This is method : ", request.method)
        # print("This is post : ", request.POST)
        # print("This is get : ", dict(request.GET))
        # print("This is session : ", dict(request.session))
        product_id = request.POST.get("product_id")
        remove = request.POST.get("remove")
        category_id = request.POST.get("category_id")

        cart = request.session.get('cart')

        if cart:
            quantity = cart.get(product_id)
            if quantity:
                if remove:
                    if quantity == 1:
                        cart.pop(product_id)
                    else:
                        cart[product_id] = cart[product_id] - 1
                else:
                    cart[product_id] = cart[product_id] + 1
            else:
                cart[product_id] = 1
        else:
            cart = {product_id: 1}

        request.session['cart'] = cart

        if category_id != "None":
            # return redirect(f'/?category={category_id}')
            response = redirect("store:index")
            response['Location'] = response['Location'] + '?category='+str(category_id)
            return response
        else:
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








