from django import forms
from .models import ASEMUSER_TYPE, CONDITION, MEMBER, STATUS, VOLUNTEER_TYPE, GodFather, ASEMUser, Worker, Child, SEX_TYPES, CORRESPONDENCE, Volunteer
from localflavor.es.forms import ESIdentityCardNumberField
from localflavor.generic.forms import IBANFormField
from localflavor.generic.countries.sepa import IBAN_SEPA_COUNTRIES
import re

PAYMENT_METHOD = (
    ('T', 'Transferencia'),
    ('TB', 'Tarjeta Bancaria'),
    ('E', 'Efectivo'),
)

class FilterAsemUserForm(forms.Form):
    qsearch = forms.CharField(max_length=100, required=False , label="Búsqueda")
    qsearch = forms.CharField(max_length=100, required=False , label="Búsqueda")
    birth_date_min = forms.DateField(required=False, widget=forms.DateInput(attrs={'type': 'date'}), label="Nacido/a después del")
    birth_date_max = forms.DateField(required=False, widget=forms.DateInput(attrs={'type': 'date'}), label="Nacido/a antes del")
    sex_choices = [('', '--Seleccione--')] + list(SEX_TYPES)
    sex = forms.ChoiceField(choices=sex_choices, required=False, label="Género")
    status_choices = [('', '--Seleccione--')] + list(STATUS)
    status = forms.ChoiceField(choices=status_choices, required=False, label="Estado civil")
    condition_choices = [('', '--Seleccione--')] + list(CONDITION)
    condition = forms.ChoiceField(choices=condition_choices, required=False, label="Condición")
    member_choices = [('', '--Seleccione--')] + list(MEMBER)
    member = forms.ChoiceField(choices=member_choices, required=False, label="Miembro")
    user_type_choices = [('', '--Seleccione--')] + list(ASEMUSER_TYPE)
    user_type = forms.ChoiceField(choices=user_type_choices, required=False, label="Tipo de usuario")

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.method = 'GET'
        for field in self.fields:
            if (isinstance(self.fields[field], forms.TypedChoiceField) or isinstance(self.fields[field], forms.ModelChoiceField)):
                self.fields[field].widget.attrs.update({'class': 'form-select', 'style': 'display:block'})
            elif (isinstance(self.fields[field], forms.BooleanField)):
                self.fields[field].widget.attrs.update({'class': 'form-check-input'})
            else:
                self.fields[field].widget.attrs.update({'class': 'form-control', 'style': 'display:block'})

        # We assign the values ​​of the filters as initial values
        self.fields['qsearch'].initial = self.data.get('qsearch')
        self.fields['birth_date_min'].initial = self.data.get('birth_date_min')
        self.fields['birth_date_max'].initial = self.data.get('birth_date_max')
        self.fields['sex'].initial = self.data.get('sex')
        self.fields['status'].initial = self.data.get('status')
        self.fields['condition'].initial = self.data.get('condition')
        self.fields['member'].initial = self.data.get('member')
        self.fields['user_type'].initial = self.data.get('user_type')

    
class FilterGodfatherForm(forms.Form):
    qsearch = forms.CharField(max_length=100, required=False , label="Búsqueda")
    qsearch = forms.CharField(max_length=100, required=False , label="Búsqueda")
    birth_date_min = forms.DateField(required=False, widget=forms.DateInput(attrs={'type': 'date'}), label="Nacido/a después del")
    birth_date_max = forms.DateField(required=False, widget=forms.DateInput(attrs={'type': 'date'}), label="Nacido/a antes del")
    sex_choices = [('', '--Seleccione--')] + list(SEX_TYPES)
    sex = forms.ChoiceField(choices=sex_choices, required=False, label="Género")
    status_choices = [('', '--Seleccione--')] + list(STATUS)
    status = forms.ChoiceField(choices=status_choices, required=False, label="Estado civil")

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.method = 'GET'
        for field in self.fields:
            if (isinstance(self.fields[field], forms.TypedChoiceField) or isinstance(self.fields[field], forms.ModelChoiceField)):
                self.fields[field].widget.attrs.update({'class': 'form-select', 'style': 'display:block'})
            elif (isinstance(self.fields[field], forms.BooleanField)):
                self.fields[field].widget.attrs.update({'class': 'form-check-input'})
            else:
                self.fields[field].widget.attrs.update({'class': 'form-control', 'style': 'display:block'})

        # We assign the values ​​of the filters as initial values
        self.fields['qsearch'].initial = self.data.get('qsearch')
        self.fields['birth_date_min'].initial = self.data.get('birth_date_min')
        self.fields['birth_date_max'].initial = self.data.get('birth_date_max')
        self.fields['sex'].initial = self.data.get('sex')
        self.fields['status'].initial = self.data.get('status')


class FilterVolunteerForm(forms.Form):
    qsearch = forms.CharField(max_length=100, required=False , label="Búsqueda")
    birth_date_min = forms.DateField(required=False, widget=forms.DateInput(attrs={'type': 'date'}), label="Nacido/a después del")
    birth_date_max = forms.DateField(required=False, widget=forms.DateInput(attrs={'type': 'date'}), label="Nacido/a antes del")
    sex_choices = [('', '--Seleccione--')] + list(SEX_TYPES)
    sex = forms.ChoiceField(choices=sex_choices, required=False, label="Género")
    volunteer_type_choices = [('', '--Seleccione--')] + list(VOLUNTEER_TYPE)
    volunteer_type = forms.ChoiceField(choices=volunteer_type_choices, required=False, label="Tipo de voluntario")

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.method = 'GET'
        for field in self.fields:
            if (isinstance(self.fields[field], forms.TypedChoiceField) or isinstance(self.fields[field], forms.ModelChoiceField)):
                self.fields[field].widget.attrs.update({'class': 'form-select', 'style': 'display:block'})
            elif (isinstance(self.fields[field], forms.BooleanField)):
                self.fields[field].widget.attrs.update({'class': 'form-check-input'})
            else:
                self.fields[field].widget.attrs.update({'class': 'form-control', 'style': 'display:block'})

        # We assign the values ​​of the filters as initial values
        self.fields['qsearch'].initial = self.data.get('qsearch')
        self.fields['birth_date_min'].initial = self.data.get('birth_date_min')
        self.fields['birth_date_max'].initial = self.data.get('birth_date_max')
        self.fields['sex'].initial = self.data.get('sex')
        self.fields['volunteer_type'].initial = self.data.get('volunteer_type')


class CreateNewGodFather(forms.ModelForm):

    class Meta:
        model = GodFather
        exclude = ['id', 'ong']
        widgets = {
            'birth_date': forms.DateInput(attrs={'type': 'date'}, format='%Y-%m-%d'),
            'start_date': forms.DateInput(attrs={'type': 'date'}, format='%Y-%m-%d'),
            'termination_date': forms.DateInput(attrs={'type': 'date'}, format='%Y-%m-%d'),
            'amount': forms.NumberInput(attrs={'step': "0.01"}),
            'sex': forms.Select(attrs={'step': "0.01"}),
            'payment_method': forms.Select(choices=PAYMENT_METHOD),
        }
        error_messages = {
            'bank_account_number': {
                'required': 'Por favor ingrese su número de cuenta bancaria.',
            },
            'bank_account_reference': {
                'required': 'Por favor ingrese su referencia de cuenta bancaria.',
            },
            'bank_account_holder': {
                'required': 'Por favor ingrese el titular de la cuenta bancaria.',
            },
        }

        dni = ESIdentityCardNumberField(only_nif=True)
        bank_account_number = IBANFormField(
            include_countries=IBAN_SEPA_COUNTRIES)

    def __init__(self, *args, **kwargs):
        super(CreateNewGodFather, self).__init__(*args, **kwargs)
        self.fields['bank_account_number'].required = False
        self.fields['bank_account_reference'].required = False
        self.fields['bank_account_holder'].required = False
        self.fields['email'].required = True
        self.fields['bank_account_number'].widget.attrs.update({'class': 'form-control'})
        self.fields['bank_account_reference'].widget.attrs.update({'class': 'form-control'})
        self.fields['bank_account_holder'].widget.attrs.update({'class': 'form-control'})
        self.fields['payment_method'].widget.attrs.update({'class': 'form-control', 'id': 'id_payment_method'})
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


class CreateNewASEMUser(forms.ModelForm):
    class Meta:
        model = ASEMUser
        exclude = ['id', 'ong']  # ong should be ASEM
        widgets = {
            'birth_date': forms.DateInput(attrs={'type': 'date'}, format='%Y-%m-%d'),
        }

    def __init__(self, *args, **kwargs):
        super(CreateNewASEMUser, self).__init__(*args, **kwargs)
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


class CreateNewWorker(forms.ModelForm):
    """A form for creating new users. Includes all the required
    fields, plus a repeated password."""
    password1 = forms.CharField(label='Contraseña', widget=forms.PasswordInput)
    password2 = forms.CharField(
        label='Confirmar contraseña', widget=forms.PasswordInput)
    photo = forms.ImageField(required=False)

    class Meta:
        model = Worker
        exclude = ['id', 'last_login', 'is_active',
                   'is_admin', 'password', 'ong']

        widgets = {
            'birth_date': forms.DateInput(attrs={'type': 'date'}, format='%Y-%m-%d'),
        }

    def __init__(self, *args, **kwargs):
        super(CreateNewWorker, self).__init__(*args, **kwargs)

        for field in self.fields:
            if (isinstance(self.fields[field], forms.TypedChoiceField) or isinstance(self.fields[field], forms.ModelChoiceField)):
                self.fields[field].widget.attrs.update(
                    {'class': 'form-select mb-3'})
            elif (isinstance(self.fields[field], forms.BooleanField)):
                self.fields[field].widget.attrs.update(
                    {'class': 'form-check-input mb-3'})
            else:
                self.fields[field].widget.attrs.update(
                    {'class': 'form-control mb-3'})

    def clean_password2(self):
        # Check that the two password entries match and meet the validation requirements
        password1 = self.cleaned_data.get("password1")
        password2 = self.cleaned_data.get("password2")
        regex = r"^(?=.*[A-Za-z]).{8,}$"
        if password1 and password2 and password1 != password2:
            raise forms.ValidationError("Las contraseñas no coinciden.")
        
        if re.match(regex, password2):
            return password2
        else:
            raise forms.ValidationError("La contraseña debe tener 8 caracteres o más, y no debe ser exclusivamente numérica.")
        
    def save(self, commit=True):
        # Save the provided password in hashed format
        user = super(CreateNewWorker, self).save(commit=False)
        user.set_password(self.cleaned_data["password1"])
        if commit:
            user.save()
        return user


class UpdateWorker(forms.ModelForm):

    class Meta:
        model = Worker
        exclude = ['id', 'last_login', 'is_active',
                   'is_admin', 'password', 'ong']
        widgets = {
            'birth_date': forms.DateInput(attrs={'type': 'date'}, format='%Y-%m-%d')
        }

    def __init__(self, *args, **kwargs):
        super(UpdateWorker, self).__init__(*args, **kwargs)
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

    def save(self, commit=True):
        # Save the provided password in hashed format
        user = super(UpdateWorker, self).save(commit=False)
        if commit:
            user.save()
        return user

class FilterWorkerForm(forms.Form):
    qsearch = forms.CharField(max_length=100, required=False , label="Búsqueda")
    birth_date_min = forms.DateField(required=False, widget=forms.DateInput(attrs={'type': 'date'}), label="Nacido/a después del")
    birth_date_max = forms.DateField(required=False, widget=forms.DateInput(attrs={'type': 'date'}), label="Nacido/a antes del")
    sex_choices = [('', '--Seleccione--')] + list(SEX_TYPES)
    sex = forms.ChoiceField(choices=sex_choices, required=False, label="Género")

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.method = 'GET'
        for field in self.fields:
            if (isinstance(self.fields[field], forms.TypedChoiceField) or isinstance(self.fields[field], forms.ModelChoiceField)):
                self.fields[field].widget.attrs.update({'class': 'form-select', 'style': 'display:block'})
            elif (isinstance(self.fields[field], forms.BooleanField)):
                self.fields[field].widget.attrs.update({'class': 'form-check-input'})
            else:
                self.fields[field].widget.attrs.update({'class': 'form-control', 'style': 'display:block'})

        # We assign the values ​​of the filters as initial values
        self.fields['qsearch'].initial = self.data.get('qsearch')
        self.fields['birth_date_min'].initial = self.data.get('birth_date_min')
        self.fields['birth_date_max'].initial = self.data.get('birth_date_max')
        self.fields['sex'].initial = self.data.get('sex')


class CreateNewChild(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        self.fields['email'].required = False

    class Meta:
        model = Child
        exclude = ['id', 'ong']
        widgets = {
            'birth_date': forms.DateInput(attrs={'type': 'date'}, format='%Y-%m-%d'),
            'start_date': forms.DateInput(attrs={'type': 'date'}, format='%Y-%m-%d'),
            'termination_date': forms.DateInput(attrs={'type': 'date'}, format='%Y-%m-%d'),
            'number_brothers_siblings': forms.NumberInput(attrs={'min': 0}),
        }

    def __init__(self, *args, **kwargs):
        super(CreateNewChild, self).__init__(*args, **kwargs)
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

class FilterChildForm(forms.Form):
    qsearch = forms.CharField(max_length=100, required=False , label="Búsqueda")
    qsearch = forms.CharField(max_length=100, required=False , label="Búsqueda")
    birth_date_min = forms.DateField(required=False, widget=forms.DateInput(attrs={'type': 'date'}), label="Nacido/a después del")
    birth_date_max = forms.DateField(required=False, widget=forms.DateInput(attrs={'type': 'date'}), label="Nacido/a antes del")
    sex_choices = [('', '--Seleccione--')] + list(SEX_TYPES)
    sex = forms.ChoiceField(choices=sex_choices, required=False, label="Género")
    is_older = forms.ChoiceField(choices=[('', '--Seleccione--'), ('S', 'Sí'), ('N', 'No')], required=False, label="¿Es mayor de edad?")
    is_sponsored = forms.ChoiceField(choices=[('', '--Seleccione--'), ('S', 'Sí'), ('N', 'No')], required=False, label="¿Está apadrinado/a?")

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.method = 'GET'
        for field in self.fields:
            if (isinstance(self.fields[field], forms.TypedChoiceField) or isinstance(self.fields[field], forms.ModelChoiceField)):
                self.fields[field].widget.attrs.update({'class': 'form-select', 'style': 'display:block'})
            elif (isinstance(self.fields[field], forms.BooleanField)):
                self.fields[field].widget.attrs.update({'class': 'form-check-input'})
            else:
                self.fields[field].widget.attrs.update({'class': 'form-control', 'style': 'display:block'})

        # We assign the values ​​of the filters as initial values
        self.fields['qsearch'].initial = self.data.get('qsearch')
        self.fields['birth_date_min'].initial = self.data.get('birth_date_min')
        self.fields['birth_date_max'].initial = self.data.get('birth_date_max')
        self.fields['sex'].initial = self.data.get('sex')
        self.fields['is_older'].initial = self.data.get('is_older')
        self.fields['is_sponsored'].initial = self.data.get('is_sponsored')


class CreateNewVolunteer(forms.ModelForm):

    class Meta:
        model = Volunteer
        exclude = ['id', 'ong']  # ong is added in the view
        widgets = {
            'birth_date': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}, format='%Y-%m-%d'),
            'contract_start_date': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}, format='%Y-%m-%d'),
            'contract_end_date': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}, format='%Y-%m-%d'),
            'dedication_time': forms.NumberInput(attrs={'step': "0.01", 'min': 0}),
        }

    def __init__(self, *args, **kwargs):
        super(CreateNewVolunteer, self).__init__(*args, **kwargs)
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
