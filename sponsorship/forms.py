from django import forms
from .models import Sponsorship
from datetime import datetime


class create_sponsorship_form(forms.ModelForm):
    class Meta:
        model = Sponsorship
        exclude = ['id']
        widgets = {
            'sponsorship_date': forms.DateInput(attrs={'class': 'form-control', 'value': datetime.today()}, format='%Y-%m-%d'),
            'termination_date': forms.DateInput(attrs={'class': 'form-control', 'value': datetime.today()}, format='%Y-%m-%d'),
        }
