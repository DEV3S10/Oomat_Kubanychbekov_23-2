from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Category(models.Model):
    title = models.CharField(max_length=50)


class Product(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    name = models.CharField(max_length=50)
    description = models.TextField()
    price = models.IntegerField(max_length=7)
    category = models.ManyToManyField(Category)


class Review(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    products = models.ForeignKey(Product, on_delete=models.CASCADE, null=True)
    text = models.TextField()
    created_date = models.DateField(auto_now=True)
    rate = models.FloatField()


