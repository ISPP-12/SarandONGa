from django import forms
from .models import Service


class CreateNewService(forms.ModelForm):
    class Meta:
        model = Service
        exclude = ['id', 'ong']
        widgets = {
            'date': forms.DateTimeInput(attrs={'type': 'datetime-local'}, format='%Y-%m-%d %H:%M')
        }

    # to remove the first empty choice '---------'
    def __init__(self, *args, **kwargs):
        super(CreateNewService, self).__init__(*args, **kwargs)
        self.fields['service_type'].choices = self.fields['service_type'].choices[1:]
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
        
        # filter payments by godfather or project
        self.fields['payment'].queryset = self.fields['payment'].queryset.filter(godfather__isnull=True) & self.fields['payment'].queryset.filter(project__isnull=True)
