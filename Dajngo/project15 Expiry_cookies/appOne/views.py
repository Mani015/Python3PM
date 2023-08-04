from django.shortcuts import render
from appOne.models import Employee
from django.views.generic import ListView,DetailView,CreateView,UpdateView,DeleteView
from django.urls import reverse_lazy
# Create your views here.

class EmployeeListView(ListView):
    model = Employee
    # By defualt template name is 'emp_list.html'
    # By default context_name is 'emp_list'

class EmployeeDetailView(DetailView):
    model = Employee
    # By default template name "employee_detail.html"
        # By default context_name 'employee'
class EmployeeCreateView(CreateView):
    model = Employee
    fields = ('Firstname','Lastname','Email','Salary')
    # fields = '__all__'
    # By default template name "employee_form.html"
        # By default context_name 'employee'

class EmployeeUpdateView(UpdateView):
    model = Employee
    fields = '__all__'
    # fields = ('Salary',)

class EmployeeDeleteView(DeleteView):
    model = Employee
    success_url = reverse_lazy('emp')
    # By defualt templatename is 'employee_confirm_delete.html'
