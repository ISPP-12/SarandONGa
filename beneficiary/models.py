from django.db import models

from django.db import models
from django.utils import timezone


SEX_TYPES = (
    ('F','Femenino'),
    ('M', 'Masculino'),
    ('O', 'Otro'),
)

class Beneficiary(models.Model):   
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




    def __str__(self):
        return '{} {}, {}'.format(self.name, self.surname, self.email)