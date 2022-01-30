
from django.db import models
from .products import Product
from .customer import Customer
import datetime
from django.utils.timezone import now


class Order(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    address = models.CharField(max_length=100)
    mob_no = models.CharField(max_length=100)
    quantity = models.IntegerField(default=1)
    price = models.IntegerField()
    order_date = models.DateTimeField(default=now)
    status = models.BooleanField(default=False)

    def place_order(self):
        self.save()


