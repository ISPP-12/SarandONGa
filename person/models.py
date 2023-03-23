from xml.dom import ValidationErr
from django.db import models
from django.utils import timezone

from django.core.validators import MinValueValidator, MaxValueValidator
from django.core.validators import RegexValidator
from django.utils.text import slugify
from django.contrib.auth.models import AbstractBaseUser
from django.contrib.auth.models import BaseUserManager

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


class Person(models.Model):

    email = models.EmailField(unique=True, blank=True, verbose_name="E-Mail")
    name = models.CharField(max_length=50, blank=True, verbose_name="Nombre")
    surname = models.CharField(
        max_length=50, blank=True, verbose_name="Apellido")
    birth_date = models.DateTimeField(
        default=timezone.now, verbose_name="Fecha de nacimiento", null=True, blank=True)
    sex = models.CharField(max_length=50, choices=SEX_TYPES,
                           verbose_name="Género", null=True, blank=True)
    city = models.CharField(
        max_length=200, verbose_name="Ciudad", null=True, blank=True)
    address = models.CharField(
        max_length=200, verbose_name="Dirección", null=True, blank=True)
    telephone = models.IntegerField(
        verbose_name="Teléfono", null=True, blank=True)
    postal_code = models.IntegerField(
        verbose_name="Código postal", null=True, blank=True)
    photo = models.ImageField(verbose_name="Foto", upload_to="person/", null=True, blank=True)


class WorkerManager(BaseUserManager):
    def create_superuser(self, email, password, **extra_fields):
        user = self.model(email=email, **extra_fields)
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
        default=timezone.now, verbose_name="Fecha de nacimiento", null=True, blank=True)
    sex = models.CharField(max_length=50, choices=SEX_TYPES,
                           verbose_name="Género", null=True, blank=True)
    city = models.CharField(
        max_length=200, verbose_name="Ciudad", null=True, blank=True)
    address = models.CharField(
        max_length=200, verbose_name="Dirección", null=True, blank=True)
    telephone = models.IntegerField(
        verbose_name="Teléfono", null=True, blank=True)
    postal_code = models.IntegerField(
        verbose_name="Código postal", null=True, blank=True)
    photo = models.ImageField(verbose_name="Foto", upload_to="./static/img/worker/", null=True, blank=True)
    is_active = models.BooleanField(default=True, verbose_name="¿Activo?")
    is_admin = models.BooleanField(default=True, verbose_name="¿Es admin?")

    USERNAME_FIELD = 'email'

    objects = WorkerManager()

    def __str__(self):
        return self.email

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
    dni = models.CharField(max_length=9, unique=True, verbose_name='DNI')
    payment_method = models.CharField(
        max_length=50, choices=PAYMENT_METHOD, verbose_name='Método de pago',)
    bank_account_number = models.CharField(max_length=24, verbose_name='Número de cuenta bancaria',
                                           validators=[RegexValidator(regex=r'^ES\d{2}\s?\d{4}\s?\d{4}\s?\d{1}\d{1}\d{10}$',
                                                                      message='El número de cuenta no es válido.')])
    bank_account_holder = models.CharField(
        max_length=100, verbose_name='Titular de cuenta bancaria')
    bank_account_reference = models.CharField(
        max_length=100, verbose_name='Referencia de cuenta bancaria', validators=[RegexValidator(r'^[0-9]+$')])
    amount = models.DecimalField(max_digits=10, decimal_places=2,
                                 verbose_name='Cantidad', validators=[MinValueValidator(1)])
    frequency = models.CharField(
        max_length=20, choices=FREQUENCY, verbose_name='Frecuencia de pago')
    seniority = models.DateField(verbose_name='Antigüedad')
    notes = models.TextField(blank=True, verbose_name='Observaciones')
    status = models.CharField(
        max_length=20, choices=STATUS, verbose_name='Estado')
    slug = models.SlugField(max_length=200, unique=True, editable=False)
    

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name + ' ' + self.surname)
        super(GodFather, self).save(*args, **kwargs)

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
        max_length=20, choices=STATUS, verbose_name='Estado')
    family_unit_size = models.IntegerField(
        verbose_name='Tamaño de la unidad familiar', validators=[MinValueValidator(0), MaxValueValidator(30)])
    own_home = models.CharField(
        max_length=20, choices=HOUSING_TYPE, verbose_name='Tipo de vivienda')
    own_vehicle = models.BooleanField(
        default=False, verbose_name='¿Tiene vehículo propio?')
    bank_account_number = models.CharField(max_length=24, verbose_name='Número de cuenta bancaria',
                                           validators=[RegexValidator(regex=r'^ES\d{2}\s?\d{4}\s?\d{4}\s?\d{1}\d{1}\d{10}$',
                                                                      message='El número de cuenta no es válido.')])

    class Meta:
        ordering = ['surname','name']
        verbose_name = 'Usuario de ASEM'
        verbose_name_plural = 'Usuarios de ASEM'

    def __str__(self):
        return self.surname + ', ' + self.name

class Volunteer(Person):

    # Trabajo que realiza el voluntario
    job = models.CharField(max_length=50, verbose_name="Trabajo")

    # Tiempo de dedicación en horas
    dedication_time = models.FloatField(verbose_name="Tiempo de dedicación")

    # Fecha de inicio del contrato
    contract_date = models.DateField(
        verbose_name="Fecha de inicio del contrato")


class Child(Person):
    sponsorship_date = models.DateTimeField(
        default=timezone.now, verbose_name="Fecha de apadrinamiento")
    terminatio_date = models.DateTimeField(
        default=timezone.now, verbose_name="Fecha de baja")
    study = models.CharField(
        max_length=200, verbose_name="Estudio", default='Apadrinamiento en curso')
    expected_mission_time = models.CharField(
        max_length=200, verbose_name="Tiempo previsto de mision", default='1 mes')
    mission_house = models.CharField(
        max_length=200, verbose_name="Casa de la mision", default='Casa')
    site = models.CharField(
        max_length=200, verbose_name="Sede", default='Sevilla, España')
    subsite = models.CharField(
        max_length=200, verbose_name="Subsede", default='Sevilla, España')
    father_name = models.CharField(
        max_length=200, verbose_name="Nombre del padre", default='Padre')
    father_profession = models.CharField(
        max_length=200, verbose_name="Profesion del padre", default='Trabajo')
    mother_name = models.CharField(
        max_length=200, verbose_name="Nombre de la madre", default='Madre')
    mother_profession = models.CharField(
        max_length=200, verbose_name="Profesion de la madre", default='Trabajo')
    number_brothers_siblings = models.IntegerField(
        verbose_name="Número de hermanos", default=0)
    correspondence = models.CharField(
        max_length=200, verbose_name="Correspondencia", default='Sevilla, España')
        

    def __str__(self):
        return self.name + ' ' + self.surname
    
    def save(self, *args, **kwargs):
        if self.terminatio_date < self.sponsorship_date:
            raise ValidationErr("The termination date must be after the sponsorship date")
        if self.number_brothers_siblings < 0:
            raise ValidationErr("A child cannot have a negative number of siblings")
        super(Child, self).save(*args, **kwargs)

    class Meta:
        ordering = ['name']
        verbose_name = 'Niño'
        verbose_name_plural = 'Niños'
