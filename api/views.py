from django.http import JsonResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response
from store.models.customer import Customer
from .serializer import CustomerSerializer


@api_view(["GET"])
def get_customer(request):
    cl = Customer.objects.all()
    slzr_cl = CustomerSerializer(cl, many=True)
    return Response(slzr_cl.data)


