from xml.dom import ValidationErr
from django.db import models
from django.utils import timezone
from django.core.exceptions import ValidationError
from django.core.validators import MinValueValidator, MaxValueValidator, RegexValidator
# from django.utils.text import slugify
from localflavor.generic.models import IBANField
from localflavor.generic.countries.sepa import IBAN_SEPA_COUNTRIES
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager


from ong.models import Ong

SEX_TYPES = (
    ('F', 'Femenino'),
    ('M', 'Masculino'),
    ('O', 'Otro'),
)

PAYMENT_METHOD = (
    ('T', 'Transferencia'),
    ('TB', 'Tarjeta Bancaria'),
    ('E', 'Efectivo'),
)

STATUS = (
    ('C', 'Casado/a'),
    ('F', 'Fallecido/a'),
    ('V', 'Viudo/a'),
    ('S', 'Soltero/a'),
    ('D', 'Divorciado/a'),
)

FREQUENCY = (
    ('A', 'Anual'),
    ('M', 'Mensual'),
    ('T', 'Trimestral'),
    ('S', 'Semestral'),
)

CONDITION = (
    ('EM', 'Escleorosis múltiple'),
    ('ICTUS', 'Ictus'),
    ('ELA', 'Esclerosis lateral amiotrófica'),
    ('OTROS', 'Otros')
)

MEMBER = (
    ('EM', 'Escleorosis múltiple'),
    ('ICTUS', 'Ictus'),
    ('ELA', 'Esclerosis lateral amiotrófica'),
    ('OTROS', 'Otros'),
    ('UNA', 'Usuario no asociado')
)

ASEMUSER_TYPE = (
    ('SACC', 'Socio ASEM con cuota de socio'),
    ('UCC', 'Usuario con cuota de socio'),
    ('USC', 'Usuario sin cuota de socio')
)

CORRESPONDENCE = (
    ('E', 'Email'),
    ('CC', 'Carta con logo'),
    ('CS', 'Carta sin logo'),
    ('SR', 'Solo revista'),
    ('N', 'Ninguna')
)

HOUSING_TYPE = (
    ('VC', 'Vivienda compartida'),
    ('VP', 'Vivienda propia')
)

VOLUNTEER_TYPE = (
    ('AP', 'Alumno en prácticas'),
    ('O', 'Otro')
)

DNI_REGEX = r'^\d{8}[A-Z]$'

DNI_VALIDATOR = RegexValidator(
    regex=DNI_REGEX,
    message='Introduce un DNI válido (8 números y 1 letra).'
)

TELEPHONE_VALIDATOR = RegexValidator(
    regex=r'^\+?1?\d{9,15}$',
    message="El número de teléfono debe estar en el formato: '+999999999'. Se permiten de 9 a 15 dígitos."
)

POSTAL_CODE_VALIDATOR = RegexValidator(
    regex=r'^\d{5}$',
    message="El código postal debe estar en el formato de cinco dígitos."
)

class Person(models.Model):
    id = models.AutoField(primary_key=True)
    email = models.EmailField(null=True, blank=True, verbose_name="E-Mail")
    name = models.CharField(max_length=50, verbose_name="Nombre")
    surname = models.CharField(
        max_length=50, verbose_name="Apellido")
    birth_date = models.DateField(
        verbose_name="Fecha de nacimiento", null=True, blank=True)
    sex = models.CharField(max_length=50, choices=SEX_TYPES,
                           verbose_name="Género", null=True, blank=True)
    city = models.CharField(
        max_length=200, verbose_name="Ciudad", null=True, blank=True)
    address = models.CharField(
        max_length=200, verbose_name="Dirección", null=True, blank=True)
    telephone = models.CharField(
        validators=[TELEPHONE_VALIDATOR], verbose_name="Teléfono", max_length=17, null=True, blank=True)
    postal_code = models.CharField(validators=[POSTAL_CODE_VALIDATOR], max_length=5, 
        verbose_name="Código postal", null=True, blank=True)
    photo = models.ImageField(
        verbose_name="Foto", upload_to="./static/img/person/", null=True, blank=True)

    def save(self, *args, **kwargs):
       # self.slug = slugify( str(self.id)+' '+self.name + ' ' + self.surname)
        super(Person, self).save(*args, **kwargs)


class WorkerManager(BaseUserManager):
    def create_superuser(self, email, password, **extra_fields):
        ongs = Ong.objects.all()

        # Agregar opción para crear una nueva ong
        options = [f"{i}. {ong.name}" for i, ong in enumerate(ongs, start=1)]
        options.append(f"{len(ongs) + 1}. Crear nueva ONG")

        print("Seleccione una ong (ingrese el número correspondiente):")
        for option in options:
            print(option)

        while True:
            try:
                choice = int(input("> "))
                if choice == len(ongs) + 1:
                    # Si elige la opción de crear una nueva ong, pedir el nombre
                    ong_name = input("Nombre de la nueva ong: ")
                    if Ong.objects.filter(name=ong_name).exists():
                        print("Ya existe una ong con ese nombre. Intente de nuevo.")
                    else:
                        ong = Ong.objects.create(name=ong_name)
                        break
                else:
                    # Si elige una ong existente, usarla
                    ong = ongs[choice - 1]
                    break
            except (ValueError, IndexError):
                print("Opción inválida. Intente de nuevo.")

        user = self.model(email=email, ong_id=ong.id, **extra_fields)
        user.set_password(password)
        user.is_admin = True
        user.save()

        return user


class Worker(AbstractBaseUser):
    email = models.EmailField(unique=True, verbose_name="E-Mail")
    name = models.CharField(max_length=50, blank=True, verbose_name="Nombre")
    surname = models.CharField(
        max_length=50, blank=True, verbose_name="Apellido")
    birth_date = models.DateTimeField(
        verbose_name="Fecha de nacimiento", null=True, blank=True)
    sex = models.CharField(max_length=50, choices=SEX_TYPES,
                           verbose_name="Género", null=True, blank=True)
    city = models.CharField(
        max_length=200, verbose_name="Ciudad", null=True, blank=True)
    address = models.CharField(
        max_length=200, verbose_name="Dirección", null=True, blank=True)
    telephone = models.CharField(
        validators=[TELEPHONE_VALIDATOR], verbose_name="Teléfono", max_length=17, null=True, blank=True)
    postal_code = models.CharField(validators=[POSTAL_CODE_VALIDATOR], max_length=5, 
        verbose_name="Código postal", null=True, blank=True)
    photo = models.ImageField(
        verbose_name="Foto", upload_to="./static/img/worker/", null=True, blank=True)
    is_active = models.BooleanField(default=True, verbose_name="¿Activo?")
    is_admin = models.BooleanField(default=True, verbose_name="¿Es admin?")
    ong = models.ForeignKey(Ong, on_delete=models.CASCADE,
                            related_name='trabajador', verbose_name="ONG", null=True, blank=True)

    USERNAME_FIELD = 'email'

    objects = WorkerManager()

    class Meta:
        ordering = ['surname', 'name']
        verbose_name = 'Trabajador'
        verbose_name_plural = 'Trabajadores'

    def __str__(self):
        return self.surname + ', ' + self.name

    @classmethod
    def has_perm(self, perm, obj=None):
        return True

    @classmethod
    def has_module_perms(self, app_label):
        return True

    @property
    def is_staff(self):
        return self.is_admin


class GodFather(Person):
    dni = models.CharField(
        max_length=9,
        unique=True,
        validators=[DNI_VALIDATOR],
        verbose_name='DNI'
    )
    payment_method = models.CharField(
        max_length=50, choices=PAYMENT_METHOD, verbose_name='Método de pago',)
    bank_account_number = IBANField(
        include_countries=IBAN_SEPA_COUNTRIES, verbose_name='Número de cuenta bancaria')
    bank_account_holder = models.CharField(
        max_length=100, verbose_name='Titular de cuenta bancaria')
    bank_account_reference = models.CharField(
        max_length=100, verbose_name='Referencia de cuenta bancaria', validators=[RegexValidator(r'^[0-9]+$')])  # for example, 1234567890
    amount = models.DecimalField(max_digits=10, decimal_places=2,
                                 verbose_name='Cantidad', validators=[MinValueValidator(1)])
    frequency = models.CharField(
        max_length=20, choices=FREQUENCY, verbose_name='Frecuencia de pago')
    start_date = models.DateField(
        default=timezone.now, verbose_name="Fecha de alta", null=True, blank=True)
    termination_date = models.DateField(
        verbose_name="Fecha de baja", null=True, blank=True)
    notes = models.TextField(blank=True, verbose_name='Observaciones')
    status = models.CharField(
        max_length=20, choices=STATUS, verbose_name='Estado')
   # slug = models.SlugField(max_length=200, unique=True, editable=False)
    ong = models.ForeignKey(Ong, on_delete=models.CASCADE,
                            related_name='padrino', verbose_name="ONG")

    def __str__(self):
        return self.name + ' ' + self.surname + ' (' + self.dni + ')'

    def save(self, *args, **kwargs):
       # self.slug = slugify(str(self.postal_code) + ' '+self.name + ' ' + self.surname)
        if self.termination_date and self.birth_date:
            if self.termination_date < self.birth_date:
                raise ValidationErr(
                    "la fecha de terminación no puede ser menor que la fecha de nacimiento")
        super(GodFather, self).save(*args, **kwargs)

    def __str__(self):
        return self.surname + ', ' + self.name

    class Meta:
        ordering = ['name']
        verbose_name = 'Padrino'
        verbose_name_plural = 'Padrinos'


class ASEMUser(Person):

    condition = models.CharField(
        max_length=20, choices=CONDITION, verbose_name='Condición médica')
    member = models.CharField(
        max_length=20, choices=MEMBER, verbose_name='Socio')
    user_type = models.CharField(
        max_length=20, choices=ASEMUSER_TYPE, verbose_name='Tipo de usuario ASEM')
    correspondence = models.CharField(
        max_length=20, choices=CORRESPONDENCE, verbose_name='Tipo de correspondencia')
    status = models.CharField(
        max_length=20, choices=STATUS, verbose_name='Estado civil')
    family_unit_size = models.IntegerField(
        verbose_name='Tamaño de la unidad familiar', validators=[MinValueValidator(0), MaxValueValidator(30)])
    own_home = models.CharField(
        max_length=20, choices=HOUSING_TYPE, verbose_name='Tipo de vivienda')
    own_vehicle = models.BooleanField(
        default=False, verbose_name='¿Tiene vehículo propio?')
    bank_account_number = models.CharField(max_length=24, verbose_name='Número de cuenta bancaria',
                                           validators=[RegexValidator(regex=r'^ES\d{2}\s?\d{4}\s?\d{4}\s?\d{1}\d{1}\d{10}$',
                                                                      message='El número de cuenta no es válido.')])
    ong = models.ForeignKey(Ong, on_delete=models.CASCADE,
                            related_name='asemuser', verbose_name="ONG")

    class Meta:
        ordering = ['surname', 'name']
        verbose_name = 'Usuario de ASEM'
        verbose_name_plural = 'Usuarios de ASEM'

    def __str__(self):
        return self.surname + ', ' + self.name


class Volunteer(Person):

    dni = models.CharField(
        max_length=9,
        unique=True,
        validators=[DNI_VALIDATOR],
        verbose_name='DNI'
    )
    # Trabajo que realiza el voluntario
    job = models.CharField(max_length=50, verbose_name="Trabajo")
    # Tiempo de dedicación en horas
    dedication_time = models.FloatField(verbose_name="Tiempo de dedicación")
    contract_start_date = models.DateField(
        verbose_name="Fecha de inicio del contrato")
    contract_end_date = models.DateField(
        verbose_name="Fecha de finalización del contrato")
    raffle = models.BooleanField(
        default=False, verbose_name="¿Participa en la rifa?")
    lottery = models.BooleanField(
        default=False, verbose_name="¿Participa en la lotería?")
    is_member = models.BooleanField(default=False, verbose_name="¿Es socio?")
    pres_table = models.BooleanField(
        default=False, verbose_name="¿Preside la mesa?")
    is_contributor = models.BooleanField(
        default=False, verbose_name="¿Es colaborador?")
    notes = models.TextField(blank=True, verbose_name='Observaciones')
    entity = models.CharField(
        max_length=50, blank=True, verbose_name="Entidad")
    table = models.CharField(max_length=50, blank=True, verbose_name="Mesa")
    volunteer_type = models.CharField(
        max_length=20, choices=VOLUNTEER_TYPE, verbose_name="Tipo de voluntario")
    ong = models.ForeignKey(Ong, on_delete=models.CASCADE,
                            related_name='voluntario', verbose_name="ONG")

    class Meta:
        ordering = ['surname', 'name']
        verbose_name = 'Voluntario'
        verbose_name_plural = 'Voluntarios'

    def __str__(self):
        return self.surname + ', ' + self.name

    def clean(self):
        if self.contract_start_date >= self.contract_end_date:
            raise ValidationError(
                'La fecha de inicio del contrato debe ser anterior a la fecha de finalización del contrato')


class Child(Person):
    start_date = models.DateField(
        default=timezone.now, verbose_name="Fecha de alta", null=True, blank=True)
    termination_date = models.DateField(
        verbose_name="Fecha de baja", null=True, blank=True)
    educational_level = models.CharField(
        max_length=200, verbose_name="Nivel de estudios")
    expected_mission_time = models.CharField(
        max_length=200, verbose_name="Tiempo previsto de mision")
    mission_house = models.CharField(
        max_length=200, verbose_name="Casa de la mision")
    site = models.CharField(
        max_length=200, verbose_name="Sede")
    subsite = models.CharField(
        max_length=200, verbose_name="Subsede")
    father_name = models.CharField(
        max_length=200, verbose_name="Nombre del padre")
    father_profession = models.CharField(
        max_length=200, verbose_name="Profesion del padre")
    mother_name = models.CharField(
        max_length=200, verbose_name="Nombre de la madre")
    mother_profession = models.CharField(
        max_length=200, verbose_name="Profesion de la madre")
    number_brothers_siblings = models.IntegerField(
        verbose_name="Número de hermanos", default=0, validators=[MinValueValidator(0)])
    correspondence = models.CharField(
        max_length=20, verbose_name="Tipo de correspondencia", choices=CORRESPONDENCE)
    # slug = models.SlugField(max_length=200, unique=True, editable=False)

    ong = models.ForeignKey(Ong, on_delete=models.CASCADE,
                            related_name='niño', verbose_name="ONG")

    def __str__(self):
        return self.surname + ', ' + self.name

    def save(self, *args, **kwargs):
        if self.termination_date and self.start_date:
            if self.termination_date < self.start_date:
                raise ValidationErr(
                    "The termination date must be after the start date")

        if self.number_brothers_siblings < 0:
            raise ValidationErr(
                "Un niño no puede tener menos de 0 hermanos")
        # self.slug = slugify(str(self.postal_code) + ' '+self.name + ' ' + self.surname)
        super(Child, self).save(*args, **kwargs)

    class Meta:
        ordering = ['name']
        verbose_name = 'Niño'
        verbose_name_plural = 'Niños'
