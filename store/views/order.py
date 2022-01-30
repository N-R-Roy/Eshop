from django.shortcuts import render
from django.views import View
from store.models.order import Order
from store.middlewares.auth import auth_middleware
from django.utils.decorators import method_decorator


class OrderView(View):

    # @method_decorator(auth_middleware)
    def get(self, request):
        customer_id = request.session.get("customer_id")

        orders = Order.objects.filter(customer=customer_id).order_by("-order_date")

        print(orders)

        return render(request, "store/order.html", {'orders': orders})
