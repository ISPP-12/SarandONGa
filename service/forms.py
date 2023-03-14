from django import forms
from .models import Service


class CreateNewService(forms.ModelForm):
    class Meta:
        model = Service
        exclude = ['id']

    # to remove the first empty choice '---------'
    def __init__(self, *args, **kwargs):
        super(CreateNewService, self).__init__(*args, **kwargs)
        self.fields['service_type'].choices = self.fields['service_type'].choices[1:]