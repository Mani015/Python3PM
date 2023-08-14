from django.db import models

# Create your models here.
class LapTop(models.Model):
    Brandname = models.CharField(max_length=20)
    Brandcolor = models.CharField(max_length=20)
    Brandprice = models.IntegerField()
