from django.http import HttpResponse

class MiddleWareLifeCycle:
    def __init__(self,get_response):
        print('Init method')
        self.get_response = get_response

    def __call__(self,request):
        print('Before the view is excuted')
        response = self.get_response(request)
        print('After the view is excuted')
        return response


class ExceptionHandlingMiddleWare:
    def __init__(self,get_response):
        self.get_response = get_response

    def __call__(self,request):
        response = self.get_response(request)
        return response

    def process_exception(self,request,exception):
        print(exception.__class__.__name__)
        print(exception)
        return HttpResponse('<h3>We are currently facing the issuses, please check the back in fewminutes</h3>')
