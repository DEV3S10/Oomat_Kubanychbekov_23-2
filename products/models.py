from django.db import models

# Create your models here.


class Category(models.Model):
    title = models.CharField(max_length=50)


class Product(models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField()
    price = models.IntegerField(max_length=7)
    category = models.ManyToManyField(Category)


class Review(models.Model):
    products = models.ForeignKey(Product, on_delete=models.CASCADE, null=True)
    text = models.TextField()
    created_date = models.DateField(auto_now=True)
    rate = models.FloatField()


