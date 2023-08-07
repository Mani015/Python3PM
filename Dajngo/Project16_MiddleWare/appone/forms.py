from django import forms

class ProductForm(forms.Form):
    ProductName = forms.CharField()
    ProductQuantity = forms.IntegerField()
