from django import forms

from .models import ASEMUser, Worker


class CreateNewASEMUser(forms.ModelForm):
    class Meta:
        model = ASEMUser
        exclude = ['id']

class CreateNewWorker(forms.ModelForm):
    class Meta:
        model = Worker
        #Campos de admin y activo están excluidos en la creación porque
        #todos los trabajadores nuevos deben tenerlo marcado
        exclude = ['id', 'last_login', 'is_active','is_admin']

