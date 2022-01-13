from django.shortcuts import render, redirect
from django.contrib.auth.hashers import check_password
from store.models import Customer
from django.views import View


class Login(View):

    def get(self, request):
        return render(request, "store/login.html")

    def post(self, request):
        email = request.POST.get("email")
        password = request.POST.get("password")

        customer = None

        try:
            customer = Customer.objects.get(email=email)
        except:
            customer = None

        err_msg = ""
        if customer:
            flag = check_password(password, customer.password)
            if flag:
                return redirect("store:index")
            else:
                err_msg = "Invalid email or password"
        else:
            err_msg = "Invalid email or password"

        return render(request, "store/login.html", {'error': err_msg})


# def login(request):
#     if request.method == 'GET':
#         return render(request, "store/login.html")
#     else:
#         email = request.POST.get("email")
#         password = request.POST.get("password")
#
#         customer = None
#
#         try:
#             customer = Customer.objects.get(email=email)
#         except:
#             customer = None
#
#         err_msg = ""
#         if customer:
#             flag = check_password(password, customer.password)
#             if flag:
#                 return redirect("store:index")
#             else:
#                 err_msg = "Invalid email or password"
#         else:
#             err_msg = "Invalid email or password"
#
#         return render(request, "store/login.html", {'error': err_msg})


