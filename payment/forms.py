from django import forms

from .models import Payment


class CreatePaymentForm(forms.ModelForm):
    class Meta:
        model = Payment
        exclude = ['id', 'ong', 'godfather', 'project']
        widgets = {
            'payday': forms.DateInput(attrs={'type': 'date'}, format='%Y-%m-%d'),
            'amount': forms.NumberInput(attrs={'class': 'form-control', 'step': "0.01", "placeholder": "Escriba una cantidad"}),
            'concept': forms.TextInput(attrs={"placeholder": "Introduzca un concepto"}),
        }

    def __init__(self, *args, **kwargs):
        super(CreatePaymentForm, self).__init__(*args, **kwargs)
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
