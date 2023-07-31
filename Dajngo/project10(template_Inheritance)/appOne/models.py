from django.db import models
from django.urls import reverse
# Create your models here.

class Employee(models.Model):
    Firstname = models.CharField(max_length=20)
    Lastname = models.CharField(max_length=30)
    Email = models.CharField(max_length=30)
    Salary = models.IntegerField()

    def get_absolute_url(self):
        return reverse('emp',args={self.pk})
