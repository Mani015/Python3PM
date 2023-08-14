from django.db import models

# Create your models here.
class Patient(models.Model):
    Firstname = models.CharField(max_length=30)
    Lastname = models.CharField(max_length=30)
    Age = models.IntegerField()

class ClinicalData(models.Model):
    COMPONENT_NAMES = [('HW','height/Weight'),('BP','Blood Pressure'),('HR','Heart Rate')]
    componentName = models.CharField(choices=COMPONENT_NAMES,max_length=30)
    componentValue = models.CharField(max_length=30)
    measureDateTime = models.DateTimeField(auto_now_add=True)
    Patient = models.ForeignKey(Patient,on_delete=models.CASCADE)
