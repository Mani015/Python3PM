from django.shortcuts import render

# Create your views here.
def UsingRender(request):
    return render(request,'template/basic.html')

def Student(request):
    student = {
        'first_name': 'John',
        'last_name': 'Doe',
        'roll_no' : 123
    }
    return render(request,'template/student.html',context=student)
