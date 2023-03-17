import datetime
from django import forms

from .models import Subsidy


class CreateNewSubsidy(forms.ModelForm):
    class Meta:
        model = Subsidy
        fields = ['presentation_date', 'payment_date', 'organism', 'provisional_resolution', 'final_resolution',
                  'amount', 'name']
        widgets = {
            'presentation_date': forms.DateInput(attrs={'class': 'form-control', 'value': datetime.date.today}, format='%Y-%m-%d'),
            'payment_date': forms.DateInput(attrs={'class': 'form-control'}, format='%Y-%m-%d'),
            'organism': forms.TextInput(attrs={'class': 'form-control'}),
            'provisional_resolution': forms.DateInput(attrs={'class': 'form-control'}, format='%Y-%m-%d'),
            'final_resolution': forms.DateInput(attrs={'class': 'form-control'}, format='%Y-%m-%d'),
            'amount': forms.NumberInput(attrs={'class': 'form-control', 'step': "0.01"}),
        }
