from django import forms
from .models import Service


class CreateNewService(forms.ModelForm):
    class Meta:
        model = Service
        exclude = ['id']