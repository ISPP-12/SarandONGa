import datetime
from django import forms

from .models import Payment

class create_payment_form(forms.ModelForm):
    class Meta:
        model = Payment
        fields = ['amount', 'payday']
        widgets = {
            'payday': forms.DateInput(attrs={'class': 'form-control', 'value': datetime.date.today}, format='%Y-%m-%d'),
            'amount': forms.NumberInput(attrs={'class': 'form-control', 'step': "0.01", "placeholder": "Escriba una cantidad"}),
            # Cuando esté padrino, descomentar la línea de abajo
            #'godfather': forms.Select(attrs={'class': 'form-control'}),
        }

