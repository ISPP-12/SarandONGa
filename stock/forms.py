from django import forms
from .models import Stock


class CreateNewStock(forms.ModelForm):
    class Meta:
        model = Stock
        exclude = ['id', 'ong']
        widgets = {
            'name': forms.TextInput(attrs={'placeholder': 'Nombre del producto', 'maxlength': '200', 'required': 'true'}),
            'quantity': forms.NumberInput(attrs={'placeholder': 'Cantidad', 'step': '1'}),
            # 'file': forms.FileInput(attrs={'class': 'form-control-file'}),

        }

    def __init__(self, *args, **kwargs):
        super(CreateNewStock, self).__init__(*args, **kwargs)
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

        # TODO: add file field to form (and model)
