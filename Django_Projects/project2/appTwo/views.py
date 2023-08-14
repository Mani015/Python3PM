from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.

def Employee(request):
    return HttpResponse('<h2>Zero is better than copy</h2>')