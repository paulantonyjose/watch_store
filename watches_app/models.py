from django.db import models

# Create your models here.
from django.db import models

class Product(models.Model):
    product_id = models.AutoField(primary_key=True)
    product_name = models.CharField(max_length=100)
    strap_color = models.CharField(max_length=20)
    highlights = models.CharField(max_length=200)
    price = models.FloatField()
    status = models.BooleanField(blank=True,null=True)
