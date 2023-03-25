from django import forms
from .models import Donation


class CreateNewDonation(forms.ModelForm):
    class Meta:
        model = Donation
        exclude = ['id', 'ong']
        widgets = {
            'created_date': forms.DateInput(attrs={'type': 'datetime-local'}, format='%Y-%m-%d %H:%M'),
            'ong':forms.Select(attrs={'class': 'form-select w-100 mb-3', 'disabled': True}),
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
