from django import forms
from .models import GodFather, ASEMUser, Worker, Child, SEX_TYPES, CORRESPONDENCE, Volunteer
from localflavor.es.forms import ESIdentityCardNumberField
from localflavor.generic.forms import IBANFormField
from localflavor.generic.countries.sepa import IBAN_SEPA_COUNTRIES

class FilterAsemUserForm(forms.Form):
    qsearch = forms.CharField(max_length=100, required=False , label="Búsqueda")
    min_date = forms.DateField(required=False, widget=forms.DateInput(attrs={'type': 'date'}), label="Nacido/a después del")
    max_date = forms.DateField(required=False, widget=forms.DateInput(attrs={'type': 'date'}), label="Nacido/a antes del")
    sex = forms.ChoiceField(choices=[('', '--Seleccione--'), ('F', 'Femenino'), ('M', 'Masculino'), ('O', 'Otro')], required=False, label="Género")
    condition = forms.ChoiceField(choices=[('', '--Seleccione--'), ('EM', 'Esclerosis múltiple'), ('ICTUS', 'Ictus'), ('ELA', 'Esclerosis lateral amiotrófica'), ('OTROS', 'Otros')], required=False, label="Condición")
    member = forms.ChoiceField(choices=[('', '--Seleccione--'), ('EM', 'Esclerosis múltiple'), ('ICTUS', 'Ictus'), ('ELA', 'Esclerosis lateral amiotrófica'), ('OTROS', 'Otros'), ('UNA', 'Usuario no asociado')], required=False, label="Miembro")
    user_type = forms.ChoiceField(choices=[('', '--Seleccione--'), ('SACC', 'Socio ASEM con cuota de socio'), ('UCC', 'Usuario con cuota de socio'), ('USC', 'Usuario sin cuota de socio')], required=False, label="Tipo de usuario")
    correspondence = forms.ChoiceField(choices=[('', '--Seleccione--'), ('E', 'Email'), ('CC', 'Carta con logo'), ('CS', 'Carta sin logo'), ('SR', 'Solo revista'), ('N', 'Ninguna')], required=False, label="Correspondencia")
    status = forms.ChoiceField(choices=[('', '--Seleccione--'), ('C', 'Casado/a'), ('F', 'Fallecido/a'), ('V', 'Viudo/a'), ('S', 'Soltero/a'), ('D', 'Divorciado/a')], required=False, label="Estado civil")
    fam_size_min = forms.IntegerField(required=False, label="Tamaño mínimo de unidad familiar")
    fam_size_max = forms.IntegerField(required=False, label="Tamaño máximo de unidad familiar")
    own_home = forms.ChoiceField(choices=[('', '--Seleccione--'), ('VC', 'Vivienda compartida'), ('VP', 'Vivienda propia')], required=False, label="Tipo de vivienda")
    own_vehicle = forms.ChoiceField(choices=[('', '--Seleccione--'), (True, 'Sí'), (False, 'No')], required=False,label= "Posee vehículo")

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.method = "get"


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
        }
        dni = ESIdentityCardNumberField(only_nif=True)
        bank_account_number = IBANFormField(
            include_countries=IBAN_SEPA_COUNTRIES)

    def __init__(self, *args, **kwargs):
        super(CreateNewGodFather, self).__init__(*args, **kwargs)
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
        # Check that the two password entries match
        password1 = self.cleaned_data.get("password1")
        password2 = self.cleaned_data.get("password2")
        if password1 and password2 and password1 != password2:
            raise forms.ValidationError("Las contraseñas no coinciden")
        return password2

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
    email = forms.CharField(max_length=100, required=False , label="Búsqueda por email")
    name = forms.CharField(max_length=100, required=False , label="Búsqueda por nombre")
    surname = forms.CharField(max_length=100, required=False , label="Búsqueda por apellido")
    birth_date_min = forms.DateField(required=False, widget=forms.DateInput(attrs={'type': 'date'}), label="Nacido/a después del")
    birth_date_max = forms.DateField(required=False, widget=forms.DateInput(attrs={'type': 'date'}), label="Nacido/a antes del")
    sex = forms.ChoiceField(choices=[('', '--Seleccione--'), ('F', 'Femenino'), ('M', 'Masculino'), ('O', 'Otro')], required=False, label="Género")
    city = forms.CharField(max_length=100, required=False, label="Búsqueda por ciudad")
    address = forms.CharField(max_length=100, required=False, label="Búsqueda por dirección")
    telephone = forms.IntegerField(required=False, label="Búsqueda por teléfono", widget=forms.NumberInput(attrs={'min': 0}))
    postal_code = forms.IntegerField(required=False, label="Búsqueda por código postal", widget=forms.NumberInput(attrs={'min': 0}))

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.method = 'GET'

        # Asignamos los valores de los filtros como valores iniciales

        self.fields['email'].initial = self.data.get('email')
        self.fields['name'].initial = self.data.get('name')
        self.fields['surname'].initial = self.data.get('surname')
        self.fields['birth_date_min'].initial = self.data.get('birth_date_min')
        self.fields['birth_date_max'].initial = self.data.get('birth_date_max')
        self.fields['sex'].initial = self.data.get('sex')
        self.fields['city'].initial = self.data.get('city')
        self.fields['address'].initial = self.data.get('address')
        self.fields['telephone'].initial = self.data.get('telephone')
        self.fields['postal_code'].initial = self.data.get('postal_code')

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


class CreateNewVolunteer(forms.ModelForm):

    class Meta:
        model = Volunteer
        exclude = ['id', 'ong']  # ong is added in the view
        widgets = {
            'birth_date': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}, format='%Y-%m-%d'),
            'contract_start_date': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}, format='%Y-%m-%d'),
            'contract_end_date': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}, format='%Y-%m-%d'),
            'dedication_time': forms.NumberInput(attrs={'step': "0.01"}),
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
