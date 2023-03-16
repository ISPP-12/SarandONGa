from django.db import models
from django.core.validators import MinValueValidator
from django.forms import ValidationError

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
    amount = models.FloatField(validators=[MinValueValidator(0)], verbose_name="Cantidad")

    # Nombre completo (con apellidos) de la persona o entidad que dona
    name = models.CharField(max_length=200, verbose_name="Nombre completo")

    def save(self, force_insert=False, force_update=False, using=None,
          update_fields=None):
        self.clean()
        if self.amount < 0:
            raise ValidationError("El importe no puede ser negativo")
        super().save(force_insert, force_update, using, update_fields)

    def __str__(self):
        return self.name
