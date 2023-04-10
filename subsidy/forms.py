from django import forms
from .models import Subsidy


class CreateNewSubsidy(forms.ModelForm):
    class Meta:
        model = Subsidy
        exclude = ['id','ong']
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
                    {'class': 'form-select'})
            elif (isinstance(self.fields[field], forms.BooleanField)):
                self.fields[field].widget.attrs.update(
                    {'class': 'form-check-input'})
            else:
                self.fields[field].widget.attrs.update(
                    {'class': 'form-control'})

class FilterSubsidyForm(forms.Form):
    qsearch = forms.CharField(max_length=100, required=False , label="Búsqueda")
    min_presentation_date = forms.DateField(required=False, widget=forms.DateInput(attrs={'type': 'date'}), label="Fecha de presentación después del")
    max_presentation_date = forms.DateField(required=False, widget=forms.DateInput(attrs={'type': 'date'}), label="Fecha de presentación antes del")
    min_payment_date = forms.DateField(required=False, widget=forms.DateInput(attrs={'type': 'date'}), label="Fecha de pago después del")
    max_payment_date = forms.DateField(required=False, widget=forms.DateInput(attrs={'type': 'date'}), label="Fecha de pago antes del")
    min_provisional_resolution_date = forms.DateField(required=False, widget=forms.DateInput(attrs={'type': 'date'}), label="Fecha de resolución provisional después del")
    max_provisional_resolution_date = forms.DateField(required=False, widget=forms.DateInput(attrs={'type': 'date'}), label="Fecha de resolución provisional antes del")
    min_final_resolution_date = forms.DateField(required=False, widget=forms.DateInput(attrs={'type': 'date'}), label="Fecha de resolución final después del")
    max_final_resolution_date = forms.DateField(required=False, widget=forms.DateInput(attrs={'type': 'date'}), label="Fecha de resolución final antes del")
    organism = forms.CharField(max_length=100, required=False , label="Organismo")
    name = forms.CharField(max_length=100, required=False , label="Nombre")
    ong = forms.CharField(max_length=100, required=False , label="Ong")
    status = forms.ChoiceField(choices=[('', '--Seleccione--'), ('Por presentar', 'Por presentar'),
    ('Presentada', 'Presentada'), ('Concedida', 'Concedida'), ('Denegada', 'Denegada')], 
    required=False, label="Método de pago")
    amount_min = forms.IntegerField(required=False, label="Tamaño mínimo de cantidad")
    amount_max = forms.IntegerField(required=False, label="Tamaño máximo de cantidad")

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.method = "get"