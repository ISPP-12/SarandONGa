from django import forms
from .models import Sponsorship
from datetime import date
from xml.dom import ValidationErr


class CreateSponsorshipForm(forms.ModelForm):
    class Meta:
        model = Sponsorship
        exclude = ['id', 'ong']
        widgets = {
            'sponsorship_date': forms.DateInput(attrs={'type': 'date', 'value': date.today()}, format='%Y-%m-%d'),
            'termination_date': forms.DateInput(attrs={'type': 'date', 'required': False}, format='%Y-%m-%d'),
            'home': forms.SelectMultiple(attrs={'required': False}),
            'godfather': forms.SelectMultiple(attrs={'required': False}),
        }

    def __init__(self, *args, **kwargs):
        super(CreateSponsorshipForm, self).__init__(*args, **kwargs)
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

    def validate_dates(self, sponsorship_date, termination_date, child):
        if sponsorship_date and termination_date and sponsorship_date > termination_date:
            self.add_error("sponsorship_date", ValidationErr(
                "La fecha de apadrinamiento no puede ser posterior a la fecha de baja del apadrinamiento."))
        if child.birth_date is not None:
            if sponsorship_date and child and sponsorship_date < child.birth_date:
                self.add_error("sponsorship_date", ValidationErr(
                    "La fecha de apadrinamiento no puede ser anterior a la fecha de nacimiento del niño"))

        if sponsorship_date and child and child.termination_date is not None and sponsorship_date > child.termination_date:
            self.add_error("sponsorship_date", ValidationErr(
                "La fecha de apadrinamiento no puede ser posterior a la fecha de baja del niño."))

    def validate_godfather(self, godfather, sponsorship_date, termination_date):
        for g in godfather:
            if g.termination_date is not None and sponsorship_date > g.termination_date:
                self.add_error("sponsorship_date", ValidationErr(
                    "La fecha de apadrinamiento no puede ser posterior a la fecha de baja del padrino."))

            if g.amount <= 0:
                self.add_error("godfather", ValidationErr(
                    "La cantidad donada por el padrino debe ser mayor que cero."))

            if g.termination_date is not None and termination_date is not None:
                if termination_date > g.termination_date:
                    self.add_error("termination_date", ValidationErr(
                        "La fecha de terminación del apadrinamiento no puede ser posterior a la fecha de baja del padrino."))

    def clean(self):
        cleaned_data = super().clean()
        sponsorship_date = cleaned_data.get("sponsorship_date")
        termination_date = cleaned_data.get("termination_date")
        child = cleaned_data.get("child")
        godfather = cleaned_data.get("godfather")
        home = cleaned_data.get("home")

        self.validate_dates(sponsorship_date, termination_date, child)
        if godfather:
            self.validate_godfather(
                godfather, sponsorship_date, termination_date)

        if home:
            for h in home:
                if h.termination_date is not None and termination_date is not None:
                    if termination_date > h.termination_date:
                        self.add_error("termination_date", ValidationErr(
                            "La fecha de terminación del apadrinamiento no puede ser posterior a la fecha de baja de la casa de acogida."))
        if not home and not godfather:
            self.add_error("home", ValidationErr(
                "Debe seleccionar al menos una casa de acogida o un padrino."))
        # There's another active sponsorship with the same child, besides the one is being created or updated:
        if Sponsorship.objects.filter(child=child, termination_date__isnull=True).exclude(id=self.instance.id).exists():
            self.add_error("child", ValidationErr(
                "Ya existe un apadrinamiento activo para este niño."))
