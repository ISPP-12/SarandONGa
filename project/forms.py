from django import forms
from project.models import Project


class FilterProjectForm(forms.Form):
    qsearch = forms.CharField(max_length=100, required=False, label="Búsqueda")
    start_date_min = forms.DateField(required=False, widget=forms.DateInput(
        attrs={'type': 'date'}), label="Con fecha de inicio mínima")
    start_date_max = forms.DateField(required=False, widget=forms.DateInput(
        attrs={'type': 'date'}), label="Con fecha de inicio máxima")
    end_date_min = forms.DateField(required=False, widget=forms.DateInput(
        attrs={'type': 'date'}), label="Con fecha de fin mínima")
    end_date_max = forms.DateField(required=False, widget=forms.DateInput(
        attrs={'type': 'date'}), label="Con fecha de fin máxima")
    number_of_beneficiaries_min = forms.IntegerField(
        required=False, label="Tamaño mínimo de unidad familiar", widget=forms.NumberInput(attrs={'min': 0}))
    number_of_beneficiaries_max = forms.IntegerField(
        required=False, label="Tamaño máximo de unidad familiar", widget=forms.NumberInput(attrs={'min': 0}))
    amount_min = forms.FloatField(
        required=False, label="Cantidad mínima", widget=forms.NumberInput(attrs={'min': 0}))
    amount_max = forms.FloatField(
        required=False, label="Cantidad máxima", widget=forms.NumberInput(attrs={'min': 0}))
    announcement_date_min = forms.DateField(required=False, widget=forms.DateInput(
        attrs={'type': 'date'}), label="Con fecha de anuncio mínima")
    announcement_date_max = forms.DateField(required=False, widget=forms.DateInput(
        attrs={'type': 'date'}), label="Con fecha de anuncio máxima")

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.method = 'GET'
        for field in self.fields:
            if (isinstance(self.fields[field], forms.TypedChoiceField) or isinstance(self.fields[field], forms.ChoiceField)):
                self.fields[field].widget.attrs.update(
                    {'class': 'form-select', 'style': 'display:block'})
            elif (isinstance(self.fields[field], forms.BooleanField)):
                self.fields[field].widget.attrs.update(
                    {'class': 'form-check-input'})
            else:
                self.fields[field].widget.attrs.update(
                    {'class': 'form-control', 'style': 'display:block'})

        self.fields['qsearch'].initial = self.data.get('qsearch')
        self.fields['start_date_min'].initial = self.data.get('start_date_min')
        self.fields['start_date_max'].initial = self.data.get('start_date_max')
        self.fields['end_date_min'].initial = self.data.get('end_date_min')
        self.fields['end_date_max'].initial = self.data.get('end_date_max')
        self.fields['number_of_beneficiaries_min'].initial = self.data.get(
            'number_of_beneficiaries_min')
        self.fields['number_of_beneficiaries_max'].initial = self.data.get(
            'number_of_beneficiaries_max')
        self.fields['amount_min'].initial = self.data.get('amount_min')
        self.fields['amount_max'].initial = self.data.get('amount_max')
        self.fields['announcement_date_min'].initial = self.data.get(
            'announcement_date_min')
        self.fields['announcement_date_max'].initial = self.data.get(
            'announcement_date_max')


class CreateNewProject(forms.ModelForm):
    class Meta:
        model = Project
        exclude = ['id', 'ong']
        widgets = {
            'start_date': forms.DateInput(attrs={'type': 'date'}, format='%Y-%m-%d'),
            'end_date': forms.DateInput(attrs={'type': 'date'}, format='%Y-%m-%d'),
            'announcement_date': forms.DateInput(attrs={'type': 'date'}, format='%Y-%m-%d'),
            'amount': forms.NumberInput(attrs={'step': '0.1', 'min': 1}),
            'number_of_beneficiaries': forms.NumberInput(attrs={'min': 0}),
        }

    def __init__(self, *args, **kwargs):
        super(CreateNewProject, self).__init__(*args, **kwargs)
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

    def clean(self):
        cleaned_data = super().clean()
        fecha_inicio = cleaned_data.get('start_date')
        fecha_fin = cleaned_data.get('end_date')

        if fecha_inicio and fecha_fin:
            if fecha_fin < fecha_inicio:
                self.add_error(
                    'end_date', "La fecha de finalización debe ser posterior a la fecha de inicio")
