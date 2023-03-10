from django.utils import timezone
from django.db import models

from person.models import Person

# Create your models here.
class Child(Person):

    # Clave primaria
    id = models.AutoField(primary_key=True)
    sponsorship_date = models.DateTimeField(
        default=timezone.now, verbose_name="Fecha de apadrinamiento")
    terminatio_date = models.DateTimeField(
        default=timezone.now, verbose_name="Fecha de baja")
    study = models.CharField(max_length=200, verbose_name="Estudio")
    expected_mission_time = models.CharField(max_length=200, verbose_name="Tiempo previsto de mision")
    mission_house = models.CharField(max_length=200, verbose_name="Casa de la mision")
    site = models.CharField(max_length=200, verbose_name="Sede")
    subsite = models.CharField(max_length=200, verbose_name="Subsede")
    father_name = models.CharField(max_length=200, verbose_name="Nombre del padre")
    father_profession = models.CharField(max_length=200, verbose_name="Profesion del padre")
    mother_name = models.CharField(max_length=200, verbose_name="Nombre de la madre")
    mother_profession = models.CharField(max_length=200, verbose_name="Profesion de la madre")
    number_brothers_siblings = models.CharField(max_length=200, verbose_name="Número de hermano")
    remarks = models.CharField(max_length=500, verbose_name="Obsevaciones")
    correspondence = models.CharField(max_length=200, verbose_name="Correspondencia")
