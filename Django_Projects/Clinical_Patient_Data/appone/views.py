from django.shortcuts import render,redirect
from appone.models import Patient,ClinicalData
from django.views.generic import ListView,CreateView,UpdateView,DeleteView
from django.urls import reverse_lazy
from appone.forms import ClinicalDataForm
# Create your views here.
class patientListView(ListView):
    model = Patient
    # By default template name is patient_list.html
    # By default context name is patien
class PatientCrateView(CreateView):
    model = Patient
    success_url = reverse_lazy('index')
    fields = ('Firstname','Lastname','Age')
     # By default template name is patient_form.html
    # By default context name is patient
class PatientUpdateView(UpdateView):
    model = Patient
    success_url = reverse_lazy('index')
    fields = ('Firstname','Lastname','Age')

class PatientDeleteView(DeleteView):
    model = Patient
    success_url = reverse_lazy('index')

def adddata(request,**kwargs):
    form = ClinicalDataForm()
    patient = Patient.objects.get(id=kwargs['pk'])
    if request.method == 'POST':
        form = ClinicalDataForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('/')
    return render(request,'appone/clinicaldata_form.html',{'form':form,'patient':patient})


def analyze(request,**kwargs):
    data = ClinicalData.objects.filter(id=kwargs['pk'])
    responseData = []
    for eachEntry in data:
        if eachEntry.componentName == 'HW':
            heightAndWeight = eachEntry.componentName.split('/')
            if len(heightAndWeight)>1:
                feetToMeters = float(heightAndWeight[0])* 0.4536
                BMI = (float(heightAndWeight[1]))/(feetToMeters*feetToMeters)
                bmiEntry = ClinicalData()
                bmiEntry.componentName = 'BMI'
                bmiEntry.componentValue = BMI
                responseData.append(bmiEntry)
        responseData.append(eachEntry)
    return render(request,'appone/generateReport.html',{'data':responseData})
