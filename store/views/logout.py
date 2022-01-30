
from django.shortcuts import redirect


def logout(request):
    request.session.clear()
    return redirect("store:login")








