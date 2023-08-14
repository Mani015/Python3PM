from django.contrib import admin
from appOne.models import Student
# Register your models here.


class StudentPage(admin.ModelAdmin):
    data = ['Student_no','Student_Fname','Student_Lname']




admin.site.register(Student,StudentPage)

