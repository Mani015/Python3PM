from django.shortcuts import render

# Create your views here.
def Basic(request):
    return render(request,'basic.html')

def MSD(request):
    details = {
        'Name':'Mahendra singh dhoni',
        'Age': 42,
        'Networth':120000
    }
    return render(request,'thala.html',context=details)