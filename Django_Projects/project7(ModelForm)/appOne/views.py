from django.shortcuts import render
from appOne.models import Student
from appOne.forms import StudentForm
# Create your views here.
def index(request):
    return render(request, 'template/index.html')

def listStudent(request):
    Studentform = Student.objects.all()
    return render(request, 'template/listStudent.html',{'student':Studentform})


def addStudent(request):
    form = StudentForm()
    if request.method == 'POST':
        form = StudentForm(request.POST)
        if form.is_valid():
            form.save()
        return index(request)
    return render(request, 'template/addStudent.html',{'form':form})
