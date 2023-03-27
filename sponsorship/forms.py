from django import forms
from .models import Sponsorship
from datetime import date


class CreateSponsorshipForm(forms.ModelForm):
    class Meta:
        model = Sponsorship
        exclude = ['id', 'ong']
        widgets = {
            'sponsorship_date': forms.DateInput(attrs={'class': 'form-control', 'type': 'date', 'value': date.today()}, format='%Y-%m-%d'),
            'termination_date': forms.DateInput(attrs={'class': 'form-control', 'type': 'date', 'value': date.today()}, format='%Y-%m-%d'),
        }


    def __init__(self, *args, **kwargs):
        super(CreateSponsorshipForm, self).__init__(*args, **kwargs)
        for field in self.fields:
            if (isinstance(self.fields[field], forms.TypedChoiceField) or isinstance(self.fields[field], forms.ModelChoiceField)):
                self.fields[field].widget.attrs.update(
                    {'class': 'form-select'})
            elif (isinstance(self.fields[field], forms.BooleanField)):
                self.fields[field].widget.attrs.update(
                    {'class': 'form-check-input'})
            else:
                self.fields[field].widget.attrs.update(
                    {'class': 'form-control'})
