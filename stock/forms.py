from django import forms
from .models import Stock


class CreateNewStock(forms.ModelForm):
    class Meta:
        model = Stock
        exclude = ['id', 'ong']
        widgets = {
            'name': forms.TextInput(attrs={'placeholder': 'Nombre del producto', 'maxlength': '200', 'required': 'true'}),
            'model': forms.TextInput(attrs={'placeholder': 'Modelo del producto', 'maxlength': '200'}),
            'quantity': forms.NumberInput(attrs={'placeholder': 'Cantidad', 'step': '1','required': 'true'}),
            'amount': forms.NumberInput(attrs={'placeholder': 'Precio','step': "0.01"}),
            'notes': forms.TextInput(attrs={'placeholder': 'Observaciones'})
            # 'file': forms.FileInput(attrs={'class': 'form-control-file'}),

        }

    def __init__(self, *args, **kwargs):
        super(CreateNewStock, self).__init__(*args, **kwargs)
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

        # TODO: add file field to form (and model)
