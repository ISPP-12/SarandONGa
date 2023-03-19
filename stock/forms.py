from django import forms
from .models import Stock

class CreateNewStock(forms.ModelForm):
    class Meta:
        model = Stock
        fields = ['name', 'quantity']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Nombre del producto', 'maxlength': '200', 'required': 'true'}),
            'quantity': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Cantidad'}),
            # 'file': forms.FileInput(attrs={'class': 'form-control-file'}),

        }

        #TODO: add file field to form (and model)
 