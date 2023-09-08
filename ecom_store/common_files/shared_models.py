from django.db import models
from django.contrib.auth.models import User


# Create your models here.


# model for cars
class Products(models.Model):
    name = models.CharField(max_length=50)
    quantity = models.IntegerField()  # move this to productData
    price = models.FloatField()
    picture = models.ImageField()
    description = models.CharField(max_length=500)
    year = models.IntegerField()
    miles = models.IntegerField()

    class Meta:
        app_label = 'common_files'



# model for keeping track of what sells best who buys what etc...
class productData(models.Model):
    product = models.OneToOneField(Products, on_delete=models.CASCADE)
    num_sales = models.IntegerField()  # model fo

    class Meta:
        app_label = 'common_files'


# items in users cart
class cartItems(models.Model):
    product = models.ForeignKey(Products, on_delete=models.CASCADE)
    user = models.ForeignKey(User, null=True, on_delete=models.CASCADE, related_name='cart_items')
    session = models.CharField(max_length=200)

    class Meta:
        app_label = 'common_files'
