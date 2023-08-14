from django.db import models

# Create your models here.
#  The Model class typically provides methods for querying, creating, updating, and deleting data in the underlying database,
#  making it easier to perform these operations without having to write complex SQL queries manually.
class Student(models.Model):
    Student_no = models.IntegerField()
    Student_Fname = models.CharField(max_length=30)
    Student_Lname = models.CharField(max_length=25)



