from django.db import models
from django.contrib import admin
class product(models.Model):
	product_Name=models.CharField(max_length=100)
	product_id=models.IntegerField()
	category=models.CharField(max_length=100)
	brand=models.CharField(max_length=100)
	price=models.FloatField()
	stock=models.IntegerField()
    rating=models.FloatField()
class ProductAdmin(admin.ModelAdmin):
    list_display=[
        "product_name",
        "product_id",
        "category",
        "brand",
        "price",
        "stocks",
        "rating"]