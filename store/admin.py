from django.contrib import admin
from .models.product import Product
from.models.category import Category
from .models.orders import Order
# Register your models here.

class AdminProduct(admin.ModelAdmin):
    list_display=['name','price','category']

class AdminCategory(admin.ModelAdmin):
    list_display=['name']

class AdminOrder(admin.ModelAdmin):
    list_display=['product','customer','price','quantity','date']

admin.site.register(Product,AdminProduct)
admin.site.register(Category,AdminCategory)
admin.site.register(Order,AdminOrder)