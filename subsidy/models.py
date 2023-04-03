from django.db import models
from ong.models import Ong
from django.core.validators import MinValueValidator
from django.forms import ValidationError
# from django.utils.text import slugify

SUBSIDY_STATUS = (
    ('Por presentar', 'Por presentar'),
    ('Presentada', 'Presentada'),
    ('Concedida', 'Concedida'),
    ('Denegada', 'Denegada'),
)


class Subsidy(models.Model):

    id = models.AutoField(primary_key=True)

    # Fecha en la que se presenta la subvención
    presentation_date = models.DateField(
        verbose_name="Fecha de presentación", null=True, blank=True)
    payment_date = models.DateField(
        verbose_name="Fecha de cobro", null=True, blank=True)
    # Organismo
    organism = models.CharField(max_length=100, verbose_name="Organismo")

    provisional_resolution = models.DateField(
        verbose_name="Resolución provisional", null=True, blank=True)
    final_resolution = models.DateField(
        verbose_name="Resolución definitiva", null=True, blank=True)
    # Importe de la subvención
    amount = models.FloatField(
        validators=[MinValueValidator(0)], verbose_name="Cantidad")

    # Nombre completo (con apellidos) de la persona o entidad que dona
    name = models.CharField(max_length=200, verbose_name="Nombre completo")
    status = models.CharField(
        max_length=50, choices=SUBSIDY_STATUS, verbose_name="Estado")
    ong = models.ForeignKey(Ong, on_delete=models.CASCADE,
                            related_name='subvencion', verbose_name="ONG")
    # slug = models.SlugField(max_length=200, unique=True, editable=False)

    def save(self, force_insert=False, force_update=False, using=None,
             update_fields=None):
        self.clean()
       # self.slug = slugify(self.organism + ' ' + str(self.id)+' '+ self.name)

        if self.amount < 0:
            raise ValidationError("El importe no puede ser negativo")
        if self.final_resolution and self.provisional_resolution:
            if self.final_resolution < self.provisional_resolution:
                raise ValidationError(
                    "La resolución definitiva no puede ser anterior a la provisional")
        super().save(force_insert, force_update, using, update_fields)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Subvenciones'
        verbose_name_plural = 'Subvenciones'
