import datetime
from django import forms

from .models import Subsidy


class CreateNewSubsidy(forms.ModelForm):
    class Meta:
        model = Subsidy
        fields = ['date', 'amount', 'name']
        widgets = {
            'date': forms.DateInput(attrs={'class': 'form-control', 'value': datetime.date.today}, format='%Y-%m-%d'),
            'amount': forms.NumberInput(attrs={'class': 'form-control', 'step': "0.01"}),
        }
