from django.db import models

# Create your models here.


class Product(models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField()
    price = models.IntegerField(max_length=7)

