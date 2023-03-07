from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils import timezone
from django.core.validators import MinValueValidator
from django.core.validators import RegexValidator

SEX_TYPES = (
    ('F','Femenino'),
    ('M', 'Masculino'),
    ('O', 'Otro'),
)

PAYMENT_METHOD = (
    ('T', 'Transferencia'),
    ('TB','Tarjeta Bancaria')
)

STATUS = (
    ('C', 'Casado/a'),
    ('F', 'Fallecido/a'),
    ('V', 'Viudo/a'),
    ('S', 'Soltero/a')  
)

FREQUENCY = (
    ('A', 'Anual'),
    ('M', 'Mensual')
)

class Person(models.Model):

    id= models.AutoField(primary_key=True)
    name = models.CharField(max_length=200, verbose_name="Nombre")
    surnames = models.CharField(max_length=200, verbose_name="Apellidos")
    email = models.CharField(max_length=200, verbose_name="Correo electrónico")
    birth_date = models.DateTimeField(default=timezone.now, verbose_name="Fecha de nacimiento")
    sex = models.CharField(max_length=50, choices=SEX_TYPES, verbose_name="Género")
    city = models.CharField(max_length=200, verbose_name="Ciudad")
    address = models.CharField(max_length=200, verbose_name="Dirección")
    telephone = models.IntegerField(verbose_name="Teléfono")
    postal_code = models.IntegerField(verbose_name="Código postal")

    is_worker = models.BooleanField(default=False, verbose_name="¿Es trabajador?") #Extiende a clase WorkerProfile si es un trabajador

    class Meta:
        abstract = True

class GodFather(Person):
    dni = models.CharField(max_length=9, unique=True,verbose_name='DNI')
    payment_method = models.CharField(max_length=50, choices=PAYMENT_METHOD,verbose_name='Método de pago',)
    bank_account_number = models.CharField(max_length=20,verbose_name='Número de cuenta bancaria', validators=[RegexValidator(r'^[0-9]+$')])
    bank_account_holder = models.CharField(max_length=100,verbose_name='Titular de cuenta bancaria')
    bank_account_reference = models.CharField(max_length=100,verbose_name='Referencia de cuenta bancaria', validators=[RegexValidator(r'^[0-9]+$')])
    amount = models.DecimalField(max_digits=10, decimal_places=2,verbose_name='Cantidad',validators=[MinValueValidator(1)])
    frequency = models.CharField(max_length=20, choices=FREQUENCY,verbose_name='Frecuencia de pago')
    seniority = models.CharField(max_length=50,verbose_name='Antiguedad')
    notes = models.TextField(blank=True,verbose_name='Observaciones')
    status = models.CharField(max_length=20, choices=STATUS,verbose_name='Estado')
    #T0D0
    #Añadir relacion uno a muchos con entidad pago

#class WorkerProfile(models.Model):
    #Person = models.OneToOneField(Person, on_delete=models.CASCADE)
    #ONG = models.OneToOneField(ONG, on_delete=models.CASCADE) #ONG en la que trabaja
    #active = models.BooleanField(default=True) #¿Sigue trabajando en la ONG?