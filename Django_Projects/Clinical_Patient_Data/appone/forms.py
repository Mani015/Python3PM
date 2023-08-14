from django import forms
from appone.models import Patient,ClinicalData

class PatientForm(forms.ModelForm):
    class Meta:
        model = Patient
        exclude = '__all__'
        # Include all fields from the Patient model
class ClinicalDataForm(forms.ModelForm):
    class Meta:
        model = ClinicalData
        exclude = '__all__'
