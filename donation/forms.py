from django import forms
from .models import Donation


class CreateNewDonation(forms.ModelForm):
    class Meta:
        model = Donation
        exclude = ['id']
        widgets = {
            'created_date': forms.DateInput(attrs={'type': 'date'}, format='%Y-%m-%d'),
        }

    def __init__(self, *args, **kwargs):
        super(CreateNewDonation, self).__init__(*args, **kwargs)
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
