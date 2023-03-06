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
    name = models.CharField(max_length=200)
    surname = models.CharField(max_length=200)
    email = models.CharField(max_length=200)
    birth_date = models.DateTimeField(default=timezone.now)
    sex = models.CharField(max_length=50, choices=SEX_TYPES)
    resident_place = models.CharField(max_length=200)
    address = models.CharField(max_length=200)
    telephone = models.IntegerField
    postal_code = models.IntegerField

    is_worker = models.BooleanField(default=False) #Extiende a clase WorkerProfile si es un trabajador

    class Meta:
        db_table = 'person'

class WorkerProfile(models.Model):
    Person = models.OneToOneField(Person, on_delete=models.CASCADE)
    #ONG = models.OneToOneField(ONG, on_delete=models.CASCADE) #ONG en la que trabaja
    active = models.BooleanField(default=True) #¿Sigue trabajando en la ONG?

