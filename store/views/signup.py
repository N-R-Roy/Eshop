from django.shortcuts import render, redirect
from django.contrib.auth.hashers import make_password
from store.models import Customer
from django.views import View
from django.core.files.storage import FileSystemStorage


def validate_user(customer):
    err_msg = ""
    if not customer.first_name:
        err_msg = "Enter first name"
    elif not customer.last_name:
        err_msg = "Enter last name"
    elif not customer.password:
        err_msg = "Enter password"
    elif customer.password and len(customer.password) < 8:
        err_msg = "Password character length must be 8 or higher"
    elif Customer.objects.filter(email=customer.email):
        err_msg = "This email already exist"

    return err_msg


def register_user(request):
    data = request.POST

    fname = data.get("fname")
    lname = data.get("lname")
    address = data.get("address")
    email = data.get("email")
    password = data.get("password")

    uimg = request.FILES['uimg']

    fs = FileSystemStorage(location='media/upload/user')

    filename = fs.save(uimg.name, uimg)

    value = {
        'fname': fname,
        'lname': lname,
        'address': address,
        'email': email,
    }

    customer_obj = Customer(first_name=fname,
                            last_name=lname,
                            image='upload/user/'+str(filename),
                            address=address,
                            email=email,
                            password=make_password(password))

    err_msg = validate_user(customer_obj)

    data2 = {
        "error": err_msg,
        "val": value,
    }

    if not err_msg:
        customer_obj.save()

        request.session['customer_id'] = customer_obj.id
        request.session['customer_email'] = customer_obj.email
        request.session['customer_name'] = customer_obj.first_name

        return redirect('store:index')
    else:
        # return render(request, 'store/signup.html', {"error": err_msg})
        return render(request, 'store/signup.html', data2)


class Signup(View):
    def get(self, request):
        return render(request, 'store/signup.html')

    def post(self, request):
        return register_user(request)


# def signup(request):
#     if request.method == "GET":
#         return render(request, 'store/signup.html')
#     else:
#         return register_user(request)

