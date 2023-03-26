from django import forms
from .models import Sponsorship
from datetime import date


class create_sponsorship_form(forms.ModelForm):
    class Meta:
        model = Sponsorship
        exclude = ['id']
        widgets = {
            'sponsorship_date': forms.DateInput(attrs={'class': 'form-control', 'type': 'date', 'value': date.today()}, format='%Y-%m-%d'),
            'termination_date': forms.DateInput(attrs={'class': 'form-control', 'type': 'date', 'value': date.today()}, format='%Y-%m-%d'),
        }
