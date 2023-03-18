import datetime
from django import forms

from .models import Subsidy


class CreateNewSubsidy(forms.ModelForm):
    class Meta:
        model = Subsidy
        exclude = ['id']
        widgets = {
            'presentation_date': forms.DateInput(attrs={'type': 'date'}, format='%Y-%m-%d'),
            'payment_date': forms.DateInput(attrs={'type': 'date'}, format='%Y-%m-%d'),
            'provisional_resolution': forms.DateInput(attrs={'type': 'date'}, format='%Y-%m-%d'),
            'final_resolution': forms.DateInput(attrs={'type': 'date'}, format='%Y-%m-%d'),
            'amount': forms.NumberInput(attrs={'step': "0.01"}),
        }
