from django.db import models
from django.contrib import admin
class Student(models.Model):
	Name=models.CharField(max_length=100)
	Reference_Number=models.IntegerField()
	Gender=models.CharField(max_length=1)
	Department=models.CharField(max_length=10)
	Date_of_Birth=models.DateField()
	Phone_Number=models.IntegerField()
	marksPercentage=models.FloatField()
	email=models.EmailField()
class StudentAdmin(admin.ModelAdmin):
	list_display=["Name","Reference_Number","Gender","Department"]