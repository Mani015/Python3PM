from django.shortcuts import render
from django.http import HttpResponse
from appone.forms import ProductForm
# Create your views here.
def page1(request):
    request.session.set_test_cookie()
    return HttpResponse('<h3>Set cookie</h3>')

def page2(request):
    if request.session.test_cookie_worked():
        print('Cookies are enabled')
        request.session.delete_test_cookie()
    return HttpResponse('<b>cookies are done</b>')


def countpage(request):
    if 'count' in request.COOKIES:
        count = int(request.COOKIES['count'])+1
    else:
        count = 1
    response = render(request,'count.html',{'count':count})
    response.set_cookie('count',count)
    return response


def index(request):
    raise Exception("Someting terrible has happen")
    return render(request,'index.html')

def additem(request):
    form = ProductForm()
    response = render(request, 'additem.html',{'form':form})
    if request.method == 'POST':
        form = ProductForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['ProductName']
            quantity = form.cleaned_data['ProductQuantity']
            response.set_cookie(name,quantity,60)
    return response

def showcookie(request):
    return render(request,'show.html')
