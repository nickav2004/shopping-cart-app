from django.db import models


# Create your models here.
class Item(models.Model):
    name = models.CharField(max_length=32, default="")
    price = models.FloatField(null=False, default=1)
    type = models.CharField(max_length=32, default="")
    brand = models.CharField(max_length=32, default="")
