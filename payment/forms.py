import datetime
from django import forms

from .models import Payment


class create_payment_form(forms.ModelForm):
    class Meta:
        model = Payment
        exclude = ['id']
        widgets = {
            'payday': forms.DateTimeInput(attrs={'type': 'datetime-local'}, format='%Y-%m-%d %H:%M'),
            'amount': forms.NumberInput(attrs={'step': "0.01"}),
            # Cuando esté padrino, descomentar la línea de abajo
            # 'godfather': forms.Select(attrs={'class': 'form-control'}),
        }
