
from django.shortcuts import redirect


def logout(request):
    # request.session.clear()
    request.session.pop("customer_id")
    request.session.pop("customer_email")
    return redirect("store:login")








