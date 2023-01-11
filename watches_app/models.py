from django.db import models

# Create your models here.
from django.db import models
from django.contrib.auth.models import User
class Product(models.Model):
    product_id = models.AutoField(primary_key=True)
    product_name = models.CharField(max_length=100)
    strap_color = models.CharField(max_length=20)
    highlights = models.CharField(max_length=200)
    price = models.FloatField()
    status = models.BooleanField(blank=True,null=True)


class Cart(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product_name = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    quantity = models.PositiveIntegerField(default=1)
