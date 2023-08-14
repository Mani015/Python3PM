from django.shortcuts import render

# Create your views here.

def Garments(request):
    d1 = {
        'Item1':'Product1',
        'Item2': 'product2',
        'Item3':'Product3'

    }
    return render(request,'dress.html',d1)


def Laptops(request):
    d1 = {
        'Item1': 'Product1',
        'Item2': 'product2',
        'Item3': 'Product3'

    }
    return render(request, 'dress.html', d1)


def Mobiles(request):
    d1 = {
        'Item1': 'Product1',
        'Item2': 'product2',
        'Item3': 'Product3'

    }
    return render(request, 'dress.html', d1)


def Index(request):
    return render(request,'index.html')



