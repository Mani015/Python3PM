from django.shortcuts import render
import datetime
from django.http import HttpResponse
# Create your views here.

def DateTime(request):
    dt = datetime.datetime.now()
    s = '<b>Current date and TIme:</b>' + str(dt)
    return HttpResponse(s)





