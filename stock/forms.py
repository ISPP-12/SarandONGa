import datetime
from django import forms
from .models import Stock

class CreateNewStock(forms.Form):
    name = forms.CharField(max_length=200, required=True)
    quantity = forms.DecimalField(max_digits=10, decimal_places=2)
    file = forms.CharField(max_length=200)