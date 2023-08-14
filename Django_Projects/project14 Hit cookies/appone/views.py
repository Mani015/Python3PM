from django.shortcuts import render
from django.http import HttpResponse
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

    
