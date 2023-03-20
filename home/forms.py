from django import forms
from .models import Home
from datetime import date

class create_home_form(forms.ModelForm):
    class Meta:
        model = Home
        fields = ['name','payment_method',
                  'bank_account_number','bank_account_holder','bank_account_reference',
                  'amount','frequency','seniority','notes']
        widgets = {
            'seniority': forms.DateInput(attrs={'class': 'form-control','type': 'date', 'value': date.today()}, format='%Y-%m-%d'),
            'amount': forms.NumberInput(attrs={'class': 'form-control','type': 'date', 'step': "0.01"}),
        }