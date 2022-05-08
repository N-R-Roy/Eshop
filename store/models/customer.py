from django.db import models


class Customer(models.Model):
    first_name = models.CharField(max_length=250)
    last_name = models.CharField(max_length=250)
    image = models.ImageField(upload_to='upload/user/', blank=True, null=True, default="")
    address = models.CharField(max_length=250, default="")
    email = models.EmailField()
    password = models.CharField(max_length=500)

    def __str__(self):
        return self.first_name






