
from django.shortcuts import render
from django.views import View
from store.models import Product


class Search(View):

    def post(self, request):
        product_name = request.POST.get("product_name")
        # print(product_name)
        product_list = Product.objects.filter(name=product_name)

        return render(request, 'store/search_item.html', {"product_list": product_list})





