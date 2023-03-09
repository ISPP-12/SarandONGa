from django.db import models
from django.utils import timezone
from django.core.validators import MinValueValidator, MaxValueValidator
from django.core.validators import RegexValidator
from django.contrib.auth.models import AbstractBaseUser
from django.contrib.auth.models import BaseUserManager

SEX_TYPES = (
    ('F','Femenino'),
    ('M', 'Masculino'),
    ('O', 'Otro'),
)

PAYMENT_METHOD = (
    ('T', 'Transferencia'),
    ('TB','Tarjeta Bancaria'),
    ('E', 'Efectivo'),
)

STATUS = (
    ('C', 'Casado/a'),
    ('F', 'Fallecido/a'),
    ('V', 'Viudo/a'),
    ('S', 'Soltero/a'),
    ('D', 'Divorciado/a') ,
)

FREQUENCY = (
    ('A', 'Anual'),
    ('M', 'Mensual'),
    ('T','Trimestral'),
    ('S','Semestral'),
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

USER_TYPE = (
    ('SCC','Socios ASEM con cuota de socio'),
    ('UCC','Usuarios con cuota de socio'),
    ('UCS','Usuarios sinn cuota de socio')
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

    email = models.EmailField(unique=True,blank=True,verbose_name="E-Mail")
    name = models.CharField(max_length=50, blank=True,verbose_name="Nombre")
    surname = models.CharField(max_length=50, blank=True,verbose_name="Apellido")
    birth_date = models.DateTimeField(default=timezone.now, verbose_name="Fecha de nacimiento",null=True, blank=True)
    sex = models.CharField(max_length=50, choices=SEX_TYPES, verbose_name="Género",null=True, blank=True)
    city = models.CharField(max_length=200, verbose_name="Ciudad",null=True, blank=True)
    address = models.CharField(max_length=200, verbose_name="Dirección",null=True, blank=True)
    telephone = models.IntegerField(verbose_name="Teléfono", null=True, blank=True)
    postal_code = models.IntegerField(verbose_name="Código postal",null=True, blank=True)
    photo = models.ImageField(verbose_name="Foto",null=True,blank=True)

class WorkerManager(BaseUserManager):
    def create_superuser(self, email, password, **extra_fields):
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.is_admin = True
        user.save()
        return user

class Worker(AbstractBaseUser):
        email = models.EmailField(unique=True,verbose_name="E-Mail")
        name = models.CharField(max_length=50, blank=True,verbose_name="Nombre")
        surname = models.CharField(max_length=50, blank=True,verbose_name="Apellido")
        birth_date = models.DateTimeField(default=timezone.now, verbose_name="Fecha de nacimiento",null=True, blank=True)
        sex = models.CharField(max_length=50, choices=SEX_TYPES, verbose_name="Género",null=True, blank=True)
        city = models.CharField(max_length=200, verbose_name="Ciudad",null=True, blank=True)
        address = models.CharField(max_length=200, verbose_name="Dirección",null=True, blank=True)
        telephone = models.IntegerField(verbose_name="Teléfono", null=True, blank=True)
        postal_code = models.IntegerField(verbose_name="Código postal",null=True, blank=True)
        photo = models.ImageField(verbose_name="Foto",null=True,blank=True)
        is_active = models.BooleanField(default=True, verbose_name="¿Activo?")
        is_admin = models.BooleanField(default=True, verbose_name="¿Es admin?")

        USERNAME_FIELD = 'email'

        objects = WorkerManager()

        def __str__(self):
            return self.email

        def has_perm(self, perm, obj=None):
            return self.has_perm

        def has_module_perms(self, app_label):
            return self.has_module_perms

        @property
        def is_staff(self):
            return self.is_admin

class GodFather(Person):
    dni = models.CharField(max_length=9, unique=True,verbose_name='DNI')
    payment_method = models.CharField(max_length=50, choices=PAYMENT_METHOD,verbose_name='Método de pago',)
    bank_account_number = models.CharField(max_length=24,verbose_name='Número de cuenta bancaria', validators=[RegexValidator(r'^[0-9]+$')])
    bank_account_holder = models.CharField(max_length=100,verbose_name='Titular de cuenta bancaria')
    bank_account_reference = models.CharField(max_length=100,verbose_name='Referencia de cuenta bancaria', validators=[RegexValidator(r'^[0-9]+$')])
    amount = models.DecimalField(max_digits=10, decimal_places=2,verbose_name='Cantidad',validators=[MinValueValidator(1)])
    frequency = models.CharField(max_length=20, choices=FREQUENCY,verbose_name='Frecuencia de pago')
    seniority = models.DateField(verbose_name='Antigüedad')
    notes = models.TextField(blank=True,verbose_name='Observaciones')
    status = models.CharField(max_length=20, choices=STATUS,verbose_name='Estado')
    #T0D0
    #Añadir relacion uno a muchos con entidad pago

class ASEMUser(Person):
    condition = models.CharField(max_length=20, choices=CONDITION,verbose_name='Condición médica')
    member = models.CharField(max_length=20, choices=MEMBER,verbose_name='Socio')
    user_type = models.CharField(max_length=20, choices=USER_TYPE,verbose_name='Tipo de usuario')
    correspondence = models.CharField(max_length=20, choices=CORRESPONDENCE,verbose_name='Tipo de correspondencia')
    status = models.CharField(max_length=20, choices=STATUS,verbose_name='Estado')
    family_unit_size = models.IntegerField(verbose_name='Tamaño de la unidad familiar', validators=[MaxValueValidator(30)])
    own_home = models.CharField(max_length=20, choices=HOUSING_TYPE,verbose_name='Tipo de vivienda')
    own_vehicle = models.BooleanField(default=False, verbose_name='¿Tiene vehículo propio?')
    bank_account_number = models.CharField(max_length=24,verbose_name='Número de cuenta bancaria', validators=[RegexValidator(r'^[A-Z]{2}\d{22}$')])

