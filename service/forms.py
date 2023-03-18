from django import forms
from .models import Service


class CreateNewService(forms.ModelForm):
    class Meta:
        model = Service
        exclude = ['id']
        widgets = {
            'date': forms.DateInput(attrs={'type': 'date'}, format='%Y-%m-%d')
        }

    # to remove the first empty choice '---------'
    def __init__(self, *args, **kwargs):
        super(CreateNewService, self).__init__(*args, **kwargs)
        self.fields['service_type'].choices = self.fields['service_type'].choices[1:]
