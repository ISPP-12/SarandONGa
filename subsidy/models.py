from django.db import models

# Create your models here.


class Subsidy(models.Model):

    id = models.AutoField(primary_key=True)
    # Fecha en la que se realiza la subvención
    date = models.DateField(verbose_name="Fecha")

    # Importe de la subvención
    amount = models.FloatField(verbose_name="Cantidad")

    # Nombre de la persona o entidad que dona
    name = models.CharField(max_length=100, verbose_name="Nombre")

    def __str__(self):
        return self.name
