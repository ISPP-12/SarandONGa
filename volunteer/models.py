from django.db import models
from person.models import Person

# Create your models here.

class Volunteer(Person):

    # Clave primaria
    id = models.AutoField(primary_key=True)

    # Trabajo que realiza el voluntario
    job = models.CharField(max_length=50, verbose_name="Trabajo")

    # Tiempo de dedicación en horas
    dedication_time = models.FloatField(verbose_name="Tiempo de dedicación")

    # Fecha de inicio del contrato
    contract_date = models.DateField(verbose_name="Fecha de inicio del contrato")