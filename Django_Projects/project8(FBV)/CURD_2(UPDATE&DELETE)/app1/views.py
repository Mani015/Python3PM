from django.shortcuts import render,redirect
from app1.models import LapTop
from app1.forms import LaptopForm
# Create your views here.
def LaptopView(request):
    lap = LapTop.objects.all()
    return render(request,'laptop.html',{'laptop':lap})

def laptopForm(request):
    form = LaptopForm()
    if request.method == 'POST':
        form = LaptopForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('/')
    return render(request,'form.html',{"form":form})


def laptopupdate(request,id):
    lap = LapTop.objects.get(id=id)
    if request.method=='POST':
        form = LaptopForm(request.POST, instance=lap)
        if form.is_valid():
            form.save()
        return redirect('/')
    return render(request,'update.html',{'lap':lap})

def laptopdelete(request,id):
    lap = LapTop.objects.get(id=id)
    lap.delete()
    return redirect('/')




