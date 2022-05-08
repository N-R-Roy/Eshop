
from django.db import models
from .category import Category


class Product(models.Model):
    name = models.CharField(max_length=250)
    price = models.IntegerField(default=0)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, default=1)
    description = models.CharField(max_length=400, default="")
    image = models.ImageField(upload_to='upload/products/')

    def __str__(self):
        return str(self.id)

    @staticmethod
    def get_all_product():
        return Product.objects.all()

    @staticmethod
    def get_product_by_category_id(category_id):
        return Product.objects.filter(category=category_id)

    @staticmethod
    def get_cart_product(ids):
        return Product.objects.filter(id__in=ids)

