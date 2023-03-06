from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils import timezone

SEX_TYPES = (
    ('F','Femenino'),
    ('M', 'Masculino'),
    ('O', 'Otro'),
)

class Person(AbstractUser):

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
        db_table = 'person'

class WorkerProfile(models.Model):
    Person = models.OneToOneField(Person, on_delete=models.CASCADE)
    #ONG = models.OneToOneField(ONG, on_delete=models.CASCADE) #ONG en la que trabaja
    #active = models.BooleanField(default=True) #¿Sigue trabajando en la ONG?

