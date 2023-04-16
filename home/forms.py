from django import forms
from .models import Home


class CreateHomeForm(forms.ModelForm):
    class Meta:
        model = Home
        exclude = ['id']
        widgets = {
            'start_date': forms.DateInput(attrs={'type': 'date'}, format='%Y-%m-%d'),
            'termination_date': forms.DateInput(attrs={'type': 'date'}, format='%Y-%m-%d'),
            'amount': forms.NumberInput(attrs={'step': "0.01"}),
        }
        error_messages = {
            'bank_account_number': {
                'required': 'Por favor ingrese su número de cuenta bancaria.',
            },
            'bank_account_reference': {
                'required': 'Por favor ingrese su referencia de cuenta bancaria.',
            },
            'bank_account_holder': {
                'required': 'Por favor ingrese el titular de la cuenta bancaria.',
            },
        }

    def __init__(self, *args, **kwargs):
        super(CreateHomeForm, self).__init__(*args, **kwargs)
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
                
class FilterHomeForm(forms.Form):
    qsearch = forms.CharField(max_length=100, required=False , label="Búsqueda")
    min_start_date = forms.DateField(required=False, widget=forms.DateInput(attrs={'type': 'date'}), label="Fecha de incio después del")
    max_start_date = forms.DateField(required=False, widget=forms.DateInput(attrs={'type': 'date'}), label="Fecha de incio antes del")
    min_termination_date = forms.DateField(required=False, widget=forms.DateInput(attrs={'type': 'date'}), label="Fecha de fin después del")
    max_termination_date = forms.DateField(required=False, widget=forms.DateInput(attrs={'type': 'date'}), label="Fecha de fin antes del")
    province = forms.CharField(max_length=100, required=False , label="Provincia")
    bank_account_holder = forms.CharField(max_length=100, required=False , label="Titular cuenta bancaria")
    bank_account_reference = forms.CharField(max_length=100, required=False , label="Referencia de cuenta bancaria")
    payment_method = forms.ChoiceField(choices=[('', '--Seleccione--'), ('T', 'Transferencia'),
    ('TB', 'Tarjeta Bancaria'), ('E', 'Efectivo')], required=False, label="Método de pago")
    frequency = forms.ChoiceField(choices=[('', '--Seleccione--'), ('A', 'Anual'),
    ('M', 'Mensual'), ('T', 'Trimestral'), ('S', 'Semestral')], required=False, label="Frecuencia de pago")
    amount_min = forms.IntegerField(required=False, label="Tamaño mínimo de cantidad")
    amount_max = forms.IntegerField(required=False, label="Tamaño máximo de cantidad")
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.method = "get"
        
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

