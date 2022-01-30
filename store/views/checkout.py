from django.shortcuts import redirect
from django.views import View
from store.models import Product, Order, Customer


class CheckOut(View):

    def post(self, request):
        print("This is in post >>>>>>>>>>>>>>>>>>>> ", request.POST)

        address = request.POST.get("address")
        mob_no = request.POST.get("mob_no")

        customer_id = request.session.get("customer_id")

        cart = request.session.get('cart')

        products = Product.objects.filter(id__in=cart.keys())

        for product in products:
            order = Order(product=product,
                          customer=Customer.objects.get(id=customer_id),
                          address=address,
                          mob_no=mob_no,
                          quantity=cart.get(str(product.id)),
                          price=product.price)
            order.place_order()

        request.session['cart'] = {}

        return redirect("store:order")
