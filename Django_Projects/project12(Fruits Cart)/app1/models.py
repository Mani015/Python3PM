from django.db import models

# Create your models here.
class product(models.Model):
    name = models.CharField(max_length=30)
    price = models.FloatField()
    quantity = models.IntegerField()
    img_url = models.CharField(max_length=900)

class Offer(models.Model):
    code = models.CharField(max_length=30)
    discription = models.CharField(max_length=30)
    discount = models.FloatField()
