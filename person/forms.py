from django import forms
from .models import GodFather, ASEMUser, Worker, Child, SEX_TYPES, CORRESPONDENCE, Volunteer
from localflavor.es.forms import ESIdentityCardNumberField
from localflavor.generic.forms import IBANFormField
from localflavor.generic.countries.sepa import IBAN_SEPA_COUNTRIES
import re

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
    
class FilterGodfatherForm(forms.Form):
    qsearch = forms.CharField(max_length=100, required=False , label="Búsqueda")
    min_birth_date = forms.DateField(required=False, widget=forms.DateInput(attrs={'type': 'date'}), label="Nacido/a después del")
    max_birth_date = forms.DateField(required=False, widget=forms.DateInput(attrs={'type': 'date'}), label="Nacido/a antes del")
    sex = forms.ChoiceField(choices=[('', '--Seleccione--'), ('F', 'Femenino'), ('M', 'Masculino'), ('O', 'Otro')], required=False, label="Género")
    payment_method = forms.ChoiceField(choices=[('', '--Seleccione--'), ('T', 'Transferencia'), ('TB', 'Transferencia Bancaria'), ('E', 'Efectivo')], required=False, label="Método de pago")
    frequency = forms.ChoiceField(choices=[('', '--Seleccione--'), ('A', 'Anual'), ('M', 'Mensual'), ('T', 'Trimestral'), ('S', 'Semestral')], required=False, label="Frecuencia de pago")
    min_amount = forms.DecimalField(decimal_places=2, required=False, label="Cantidad superior a:")
    max_amount = forms.DecimalField(decimal_places=2, required=False, label="Cantidad inferior a:")
    min_start_date = forms.DateField(required=False, widget=forms.DateInput(attrs={'type': 'date'}), label="Alta después del")
    max_start_date = forms.DateField(required=False, widget=forms.DateInput(attrs={'type': 'date'}), label="Alta antes del")
    min_end_date = forms.DateField(required=False, widget=forms.DateInput(attrs={'type': 'date'}), label="Baja después del")
    max_end_date = forms.DateField(required=False, widget=forms.DateInput(attrs={'type': 'date'}), label="Baja antes del")
    status = forms.ChoiceField(choices=[('', '--Seleccione--'), ('C', 'Casado/a'), ('F', 'Fallecido/a'), ('V', 'Viudo/a'), ('S', 'Soltero/a'), ('D', 'Divorciado/a')], required=False, label="Estado civil")

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.method = "get"

class FilterVolunteerForm(forms.Form):
    qsearch = forms.CharField(max_length=100, required=False , label="Búsqueda")
    min_birth_date = forms.DateField(required=False, widget=forms.DateInput(attrs={'type': 'date'}), label="Nacido/a después del")
    max_birth_date = forms.DateField(required=False, widget=forms.DateInput(attrs={'type': 'date'}), label="Nacido/a antes del")
    sex = forms.ChoiceField(choices=[('', '--Seleccione--'), ('F', 'Femenino'), ('M', 'Masculino'), ('O', 'Otro')], required=False, label="Género")
    volunteer_type = forms.ChoiceField(choices=[('', '--Seleccione--'), ('AP', 'Alumno en prácticas'), ('O', 'Otro')], required=False, label="Tipo de voluntario")
    min_dedication_time = forms.DecimalField(decimal_places=2, required=False, label="Tiempo de dedicación mínimo")
    max_dedication_time = forms.DecimalField(decimal_places=2, required=False, label="Tiempo de dedicación máximo")
    min_contract_start = forms.DateField(required=False, widget=forms.DateInput(attrs={'type': 'date'}), label="Inicio de contrato después del")
    max_contract_start = forms.DateField(required=False, widget=forms.DateInput(attrs={'type': 'date'}), label="Inicio de contrato antes del")
    min_contract_end = forms.DateField(required=False, widget=forms.DateInput(attrs={'type': 'date'}), label="Fin de contrato después del")
    max_contract_end = forms.DateField(required=False, widget=forms.DateInput(attrs={'type': 'date'}), label="Fin de contrato antes del")
    raffle = forms.ChoiceField(choices=[('', '--Seleccione--'), (True, 'Sí'), (False, 'No')], required=False,label= "Participa en la rifa")
    lottery = forms.ChoiceField(choices=[('', '--Seleccione--'), (True, 'Sí'), (False, 'No')], required=False,label= "Participa en la lotería")
    is_member = forms.ChoiceField(choices=[('', '--Seleccione--'), (True, 'Sí'), (False, 'No')], required=False,label= "Es miembro")
    pres_table = forms.ChoiceField(choices=[('', '--Seleccione--'), (True, 'Sí'), (False, 'No')], required=False,label= "Preside mesa")
    is_contributor = forms.ChoiceField(choices=[('', '--Seleccione--'), (True, 'Sí'), (False, 'No')], required=False,label= "Es colaborador")

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
    email = forms.CharField(max_length=100, required=False , label="Búsqueda por email")
    name = forms.CharField(max_length=50, required=False , label="Búsqueda por nombre")
    surname = forms.CharField(max_length=50, required=False , label="Búsqueda por apellido")
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

class FilterChildForm(forms.Form):
    email = forms.CharField(max_length=100, required=False , label="Búsqueda por email")
    name = forms.CharField(max_length=50, required=False , label="Búsqueda por nombre")
    surname = forms.CharField(max_length=50, required=False , label="Búsqueda por apellido")
    birth_date_min = forms.DateField(required=False, widget=forms.DateInput(attrs={'type': 'date'}), label="Nacido/a después del")
    birth_date_max = forms.DateField(required=False, widget=forms.DateInput(attrs={'type': 'date'}), label="Nacido/a antes del")
    sex = forms.ChoiceField(choices=[('', '--Seleccione--'), ('F', 'Femenino'), ('M', 'Masculino'), ('O', 'Otro')], required=False, label="Género")
    city = forms.CharField(max_length=100, required=False, label="Búsqueda por ciudad")
    address = forms.CharField(max_length=100, required=False, label="Búsqueda por dirección")
    telephone = forms.CharField(max_length=15, required=False, label="Búsqueda por teléfono")
    postal_code = forms.CharField(max_length=5, required=False, label="Búsqueda por código postal")
    start_date_min = forms.DateField(required=False, widget=forms.DateInput(attrs={'type': 'date'}), label="Dado/a de alta después del")
    start_date_max = forms.DateField(required=False, widget=forms.DateInput(attrs={'type': 'date'}), label="Dado/a de alta antes del")
    termination_date_min = forms.DateField(required=False, widget=forms.DateInput(attrs={'type': 'date'}), label="Dado/a de baja después de")
    termination_date_max = forms.DateField(required=False, widget=forms.DateInput(attrs={'type': 'date'}), label="Dado/a de baja antes de")
    expected_mission_time = forms.CharField(max_length=100, required=False, label="Búsqueda por tiempo de misión esperado")
    mission_house = forms.CharField(max_length=100, required=False, label="Búsqueda por casa de misión")
    site = forms.CharField(max_length=100, required=False, label="Búsqueda por sede")
    subsite = forms.CharField(max_length=100, required=False, label="Búsqueda por subsede")
    father_name = forms.CharField(max_length=100, required=False, label="Búsqueda por nombre del padre")
    father_profession = forms.CharField(max_length=100, required=False, label="Búsqueda por profesión del padre")
    mother_name = forms.CharField(max_length=100, required=False, label="Búsqueda por nombre de la madre")
    mother_profession = forms.CharField(max_length=100, required=False, label="Búsqueda por profesión de la madre")
    number_brothers_siblings = forms.IntegerField(required=False, label="Búsqueda por número de hermanos", widget=forms.NumberInput(attrs={'min': 0}))
    correspondence = forms.ChoiceField(choices=[('', '--Seleccione--'), ('E', 'Email'), ('CC', 'Carta con logo'), ('CS', 'Carta sin logo'), ('SR', 'Solo revista'), ('N', 'Ninguna')], required=False, label="Correspondencia")
    is_older = forms.ChoiceField(choices=[('', '--Seleccione--'), ('S', 'Sí'), ('N', 'No')], required=False, label="¿Es mayor de edad?")

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.method = 'GET'

        # Assigning Filter Values ​​as Initial Values

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
        self.fields['start_date_min'].initial = self.data.get('start_date_min')
        self.fields['start_date_max'].initial = self.data.get('start_date_max')
        self.fields['termination_date_min'].initial = self.data.get('termination_date_min')
        self.fields['termination_date_max'].initial = self.data.get('termination_date_max')
        self.fields['expected_mission_time'].initial = self.data.get('expected_mission_time')
        self.fields['mission_house'].initial = self.data.get('mission_house')
        self.fields['site'].initial = self.data.get('site')
        self.fields['subsite'].initial = self.data.get('subsite')
        self.fields['father_name'].initial = self.data.get('father_name')
        self.fields['father_profession'].initial = self.data.get('father_profession')
        self.fields['mother_name'].initial = self.data.get('mother_name')
        self.fields['mother_profession'].initial = self.data.get('mother_profession')
        self.fields['number_brothers_siblings'].initial = self.data.get('number_brothers_siblings')
        self.fields['correspondence'].initial = self.data.get('correspondence')
        self.fields['is_older'].initial = self.data.get('is_older')

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
