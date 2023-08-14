from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.
def Welcome(request):
    return HttpResponse('<h1> Welcome to Django Frame work</h1>')

def Rakesh(request):
    return HttpResponse('<h2>Django is using for web Development</h2>')

