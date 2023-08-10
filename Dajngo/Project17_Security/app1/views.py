from django.shortcuts import render,redirect
from app1.models import LapTop
from app1.forms import LaptopForm
from django.contrib.auth.decorators import login_required
# Create your views here.
@login_required
def LaptopView(request):
    lap = LapTop.objects.all()
    return render(request,'laptop.html',{'laptop':lap})
@login_required
def laptopForm(request):
    form = LaptopForm()
    if request.method == 'POST':
        form = LaptopForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('/')
    return render(request,'form.html',{"form":form})

@login_required
def laptopupdate(request,id):
    lap = LapTop.objects.get(id=id)
    if request.method=='POST':
        form = LaptopForm(request.POST, instance=lap)
        if form.is_valid():
            form.save()
        return redirect('/')
    return render(request,'update.html',{'lap':lap})
@login_required
def laptopdelete(request,id):
    lap = LapTop.objects.get(id=id)
    lap.delete()
    return redirect('/')

def logout(request):
    return render(request,'logout.html')
