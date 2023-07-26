from django.shortcuts import render
from appOne.models import Employee
from django.views.generic import ListView
# Create your views here.

class EmployeeListView(ListView):
    model = Employee
    # By defualt template name is 'emp_list.html'
    # By default context_name is 'emp_list'
    
