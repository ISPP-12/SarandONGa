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

    def __init__(self, *args, **kwargs):
        super(CreateNewSubsidy, self).__init__(*args, **kwargs)
        for field in self.fields:
            if (isinstance(self.fields[field], forms.TypedChoiceField) or isinstance(self.fields[field], forms.ModelChoiceField)):
                self.fields[field].widget.attrs.update(
                    {'class': 'form-select border-class'})
            elif (isinstance(self.fields[field], forms.BooleanField)):
                self.fields[field].widget.attrs.update(
                    {'class': 'form-check-input border-class'})
            else:
                self.fields[field].widget.attrs.update(
                    {'class': 'form-control border-class'})
