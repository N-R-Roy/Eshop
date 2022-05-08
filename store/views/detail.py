
from django.shortcuts import render
from django.views import View
from store.models import Product


class Detail(View):

    def get(self, request, p_id):
        product = Product.objects.get(pk=p_id)
        return render(request, "store/detail.html", {"product": product})




