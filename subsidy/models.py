from django.db import models

from ong.models import Ong

# Create your models here.


class Subsidy(models.Model):

    id = models.AutoField(primary_key=True)

    # Fecha en la que se presenta la subvención
    presentation_date = models.DateField(verbose_name="Fecha",null=True, blank=True)
    payment_date = models.DateField(verbose_name="Fecha de cobro",null=True, blank=True)
    #Organismo
    organism = models.CharField(max_length=100, verbose_name="Organismo")

    provisional_resolution = models.BooleanField(verbose_name="Resolución provisional", default=False)
    final_resolution = models.BooleanField(verbose_name="Resolución definitiva", null=True)
    # Importe de la subvención
    amount = models.FloatField(verbose_name="Cantidad")

    # Nombre completo (con apellidos) de la persona o entidad que dona
    name = models.CharField(max_length=200, verbose_name="Nombre completo")
    ong = models.ForeignKey(Ong, on_delete=models.CASCADE, related_name='subvencion')
    
    def __str__(self):
        return self.name
