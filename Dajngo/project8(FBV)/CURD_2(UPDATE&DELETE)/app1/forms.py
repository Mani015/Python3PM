from django import forms
from app1.models import LapTop

class LaptopForm(forms.ModelForm):
    class Meta:
        model = LapTop
        fields = "__all__"
