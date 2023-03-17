from django import forms
from .models import Donation


class CreateNewDonation(forms.ModelForm):
    class Meta:
        model = Donation
        exclude = ['id']
        widgets = {
            'created_date': forms.DateInput(attrs={'type': 'date'}, format='%Y-%m-%d'),
        }
