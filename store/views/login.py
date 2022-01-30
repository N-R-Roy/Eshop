from django.shortcuts import render, redirect, HttpResponseRedirect
from django.contrib.auth.hashers import check_password
from store.models import Customer
from django.views import View


class Login(View):

    request_url = None

    def get(self, request):
        print(request.GET.get('request_url'))
        Login.request_url = request.GET.get('request_url')
        # print("In login : ", dict(request.session))
        # print("In login : ", request.method)
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
                request.session['customer_id'] = customer.id
                request.session['customer_email'] = customer.email
                print(Login.request_url)
                if Login.request_url:
                    return HttpResponseRedirect('/order/')
                else:
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

# import datetime
#
# print(type(datetime.datetime.today()))
#
# print(datetime.datetime.today())
#
# print(datetime.datetime.today().date())
# print(datetime.datetime.today().time().hour)
# print(datetime.datetime.today().time().second)
# print(datetime.datetime.today().time().microsecond)





