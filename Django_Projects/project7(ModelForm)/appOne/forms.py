from django import forms
from appOne.models import Student
class StudentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = '__all__'

    # here student is a model classname(object)
    # this telss all the fields to be included  Here





# creating model form by extend the ModelFormclass
# class studentform extends modelForm
# we will be implementing meta data here
# It informs django which all the fields to be includeded here and import model that you want
