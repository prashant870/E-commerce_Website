from django.db import models
from .category import Category
from .product import Product
from django.contrib.auth.models import User
import datetime
class Order(models.Model):
    product=models.ForeignKey(Product,on_delete=models.CASCADE)
    customer=models.ForeignKey(User,on_delete=models.CASCADE)
    quantity=models.IntegerField(default=1)
    price=models.IntegerField()
    address=models.CharField(max_length=200,default="")
    phone_number=models.CharField(max_length=10,default="")
    date=models.DateField(default=datetime.datetime.today)
    status=models.BooleanField(default=False)
