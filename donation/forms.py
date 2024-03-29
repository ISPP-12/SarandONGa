from django import forms
from .models import Donation


class FilterDonationForm(forms.Form):
    qsearch = forms.CharField(max_length=100, required=False, label="Búsqueda")
    min_date = forms.DateField(required=False, widget=forms.DateInput(
        attrs={'type': 'date'}), label="Donación registrada después del")
    max_date = forms.DateField(required=False, widget=forms.DateInput(
        attrs={'type': 'date'}), label="Donación registrada antes del")
    min_amount = forms.FloatField(required=False, widget=forms.NumberInput(
        attrs={'min': 0}), label="Precio mínimo de donación")
    max_amount = forms.FloatField(required=False, widget=forms.NumberInput(
        attrs={'min': 0}), label="Precio máximo de donación")

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.method = 'GET'
        for field in self.fields:
            if (isinstance(self.fields[field], forms.TypedChoiceField) or isinstance(self.fields[field], forms.ChoiceField)):
                self.fields[field].widget.attrs.update(
                    {'class': 'form-select', 'style': 'display:block'})
            elif (isinstance(self.fields[field], forms.BooleanField)):
                self.fields[field].widget.attrs.update(
                    {'class': 'form-check-input'})
            else:
                self.fields[field].widget.attrs.update(
                    {'class': 'form-control', 'style': 'display:block'})

        # Asignamos los valores de los filtros como valores iniciales
        self.fields['qsearch'].initial = self.data.get('qsearch')
        self.fields['min_date'].initial = self.data.get('min_date')
        self.fields['max_date'].initial = self.data.get('max_date')
        self.fields['min_amount'].initial = self.data.get('min_amount')
        self.fields['max_amount'].initial = self.data.get('max_amount')


class CreateNewDonation(forms.ModelForm):
    class Meta:
        model = Donation
        exclude = ['id', 'ong']
        widgets = {
            'created_date': forms.DateInput(attrs={'type': 'date'}, format='%Y-%m-%d'),
            'ong': forms.Select(attrs={'class': 'form-select w-100 mb-3', 'disabled': True}),
            'amount': forms.NumberInput(attrs={'class': 'form-control', 'step': "0.01", "min": 0.1, "placeholder": "Escriba una cantidad"}),
        }

    def __init__(self, *args, **kwargs):
        super(CreateNewDonation, self).__init__(*args, **kwargs)
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
