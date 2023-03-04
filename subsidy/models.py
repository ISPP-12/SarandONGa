from django.db import models

# Create your models here.


class Subsidy(models.Model):

    id = models.AutoField(primary_key=True)
    # Fecha en la que se realiza la subvención
    date = models.DateField()

    # Importe de la subvención
    amount = models.FloatField()

    # Nombre de la persona o entidad que dona
    name = models.CharField(max_length=100)
    
    def __str__(self):
        return self.nombre