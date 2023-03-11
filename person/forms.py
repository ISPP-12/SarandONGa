import datetime
from django import forms
from .models import GodFather, ASEMUser

class CreateNewGodFather(forms.ModelForm):
    class Meta:
        model = GodFather
        fields = ['dni','name','surname','email','birth_date','sex','city',
                  'address','telephone','postal_code', 'payment_method',
                  'bank_account_number','bank_account_holder','bank_account_reference',
                  'amount','frequency','seniority','notes','status']
        widgets = {
            'birth_date': forms.DateInput(attrs={'class': 'form-control', 'value': datetime.date.today}, format='%Y-%m-%d'),
            'seniority': forms.DateInput(attrs={'class': 'form-control', 'value': datetime.date.today}, format='%Y-%m-%d'),
            'amount': forms.NumberInput(attrs={'class': 'form-control', 'step': "0.01"}),
        }

class CreateNewASEMUser(forms.ModelForm):
    class Meta:
        model = ASEMUser
        exclude = ['id']

