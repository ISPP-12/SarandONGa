from django.db import models
from django.core.validators import MinValueValidator
from django.forms import ValidationError

class Subsidy(models.Model):

    id = models.AutoField(primary_key=True)
    # Fecha en la que se realiza la subvención
    date = models.DateField(verbose_name="Fecha")

    # Importe de la subvención
    amount = models.FloatField(validators=[MinValueValidator(0)], verbose_name="Cantidad")

    # Nombre de la persona o entidad que dona
    name = models.CharField(max_length=100, verbose_name="Nombre")

    def save(self, *args, **kwargs):
        self.clean()
        if self.amount < 0:
            raise ValidationError("El importe no puede ser negativo")
        super().save(*args, **kwargs)
        
    def __str__(self):
        return self.name
