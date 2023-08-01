from django.shortcuts import render
from app1.models import product
# Create your views here.


def index(request):
    Product = product.objects.all()
    return render(request,'index.html',{'product':Product})
