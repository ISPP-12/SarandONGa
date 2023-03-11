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
    study = models.CharField(max_length=200, verbose_name="Estudio", default='Apadrinamiento en curso')
    expected_mission_time = models.CharField(max_length=200, verbose_name="Tiempo previsto de mision", default='1 mes')
    mission_house = models.CharField(max_length=200, verbose_name="Casa de la mision", default='Casa')
    site = models.CharField(max_length=200, verbose_name="Sede", default='Sevilla, España')
    subsite = models.CharField(max_length=200, verbose_name="Subsede", default='Sevilla, España')
    father_name = models.CharField(max_length=200, verbose_name="Nombre del padre", default='Padre')
    father_profession = models.CharField(max_length=200, verbose_name="Profesion del padre", default='Trabajo')
    mother_name = models.CharField(max_length=200, verbose_name="Nombre de la madre", default='Madre')
    mother_profession = models.CharField(max_length=200, verbose_name="Profesion de la madre", default='Trabajo')
    number_brothers_siblings = models.IntegerField(verbose_name="Número de hermano", default=0)
    correspondence = models.CharField(max_length=200, verbose_name="Correspondencia", default='Sevilla, España')
