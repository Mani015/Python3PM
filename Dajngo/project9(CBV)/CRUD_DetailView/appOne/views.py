from django.shortcuts import render
from appOne.models import Employee
from django.views.generic import ListView,DetailView
# Create your views here.

class EmployeeListView(ListView):
    model = Employee
    # By defualt template name is 'emp_list.html'
    # By default context_name is 'emp_list'

class EmployeeDetailView(DetailView):
    model = Employee
    # By default template name "employee_detail.html"
        # By default context_name 'employee'
