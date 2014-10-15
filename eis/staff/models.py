from django.db import models

# Create your models here

class Staff(models.Model):
    name= models.CharField(max_length=30)
    sex=models.IntegerField(max_length=1)
    age=models.IntegerField(max_length=3)
    workage=models.IntegerField(max_length=2)
    edu=models.CharField(max_length=100)
    salary=models.IntegerField(max_length=10)
    address=models.CharField(max_length=200)

