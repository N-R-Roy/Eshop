from django.shortcuts import render, redirect, HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth.hashers import check_password
from store.models import Customer
from django.views import View


class Login(View):
    request_url = None
    request_value = None
    address = None
    mob_no = None

    def get(self, request):
        print("Request Url =>>>>>>>>>>>> ", request.GET.get('request_url'))
        print("Request Value =>>>>>>>>>>>> ", request.GET.get('request_value'))
        # request_url = request.META["PATH_INFO"]
        # print("Request Url =>>>>>>>>>>>>", request_url)
        Login.request_url = request.GET.get('request_url')
        Login.request_value = request.GET.get('request_value')
        Login.address = request.GET.get('address')
        Login.mob_no = request.GET.get('mob')
        # print("In login : ", dict(request.session))
        # print("In login : ", request.method)
        return render(request, "store/login.html")

    def post(self, request):
        email = request.POST.get("email")
        password = request.POST.get("password")

        customer = None
        try:
            customer = Customer.objects.get(email=email)
        except Customer.DoesNotExist:
            customer = None

        err_msg = ""
        if customer:
            valid_customer = check_password(password, customer.password)
            if valid_customer:
                request.session['customer_id'] = customer.id
                request.session['customer_email'] = customer.email
                request.session['customer_name'] = customer.first_name

                print(Login.request_url)

                if Login.request_url == '/order/':
                    return HttpResponseRedirect('/order/')
                elif Login.request_url == '/check-out/':
                    # return HttpResponseRedirect('/check-out/')
                    # request.session["address"] = Login.address
                    # request.session["mob_no"] = Login.mob_no
                    # return redirect('store:cart')
                    return redirect(f"/check-out/?address={Login.address}&mob_no={Login.mob_no}")

                else:
                    # return redirect("store:index")
                    return HttpResponseRedirect(reverse('store:index'))
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








