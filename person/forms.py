import datetime
from django import forms

from .models import ASEMUser


class CreateNewASEMUser(forms.ModelForm):
    class Meta:
        model = ASEMUser
        exclude = ['id']
