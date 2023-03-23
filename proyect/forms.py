from django import forms
from proyect.models import Proyect

class CreateNewProyect(forms.ModelForm):
    class Meta:
        model = Proyect
        exclude = ['id']
        widgets = {
            'start_date': forms.DateInput(attrs={'type': 'date'}, format='%Y-%m-%d'),
            'end_date': forms.DateInput(attrs={'type': 'date'}, format='%Y-%m-%d'),
            'announcement_date': forms.DateInput(attrs={'type': 'date'}, format='%Y-%m-%d'),
        }

    def __init__(self, *args, **kwargs):
        super(CreateNewProyect, self).__init__(*args, **kwargs)
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
    
                
    def clean(self):
        cleaned_data = super().clean()
        fecha_inicio = cleaned_data.get('start_date')
        fecha_fin = cleaned_data.get('end_date')

        if fecha_inicio and fecha_fin:
            if fecha_fin < fecha_inicio:
                self.add_error('end_date', "La fecha de finalización debe ser posterior a la fecha de inicio")