from django.shortcuts import render
from appone import forms
# Create your views here.
def UserRegistration(request):
    form = forms.UserForm()
    if request.method=='POST':
        form = forms.UserForm(request.POST)
        if form.is_valid():
            print('forms is success')
            print('Firstname:', form.cleaned_data['firstname'])
            print('Larstname:', form.cleaned_data['lastname'])
            print('email:', form.cleaned_data['email'])

    return render(request,'user.html',{'form': form})


