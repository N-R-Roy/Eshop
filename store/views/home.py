
from django.shortcuts import render
from store.models import Product, Category
from django.views import View


# class Index(View):
#
#     def get(self, request):
#         category_list = Category.get_all_category()
#
#         category_id = request.GET.get('category')
#
#         product_list = None
#         if category_id:
#             product_list = Product.get_product_by_category_id(category_id)
#         else:
#             product_list = Product.get_all_product()
#
#         data = {"products": product_list, "categories": category_list}
#
#         return render(request, "store/index.html", data)


def index(request):
    category_list = Category.get_all_category()

    category_id = request.GET.get('category')

    product_list = None
    if category_id:
        product_list = Product.get_product_by_category_id(category_id)
    else:
        product_list = Product.get_all_product()

    data = {"products": product_list, "categories": category_list}

    return render(request, "store/index.html", data)


