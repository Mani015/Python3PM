from django.shortcuts import render
from appOne.models import Student

# Create your views here.

def Studnet_Info(request):
    details = Student.objects.all()
    return render(request,'info.html',{'student':details})


