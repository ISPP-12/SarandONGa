from django.db import models
from ong.models import Ong
from django.core.validators import MinValueValidator
from django.forms import ValidationError
# from django.utils.text import slugify

SUBSIDY_STATUS = (
    ('Por presentar', 'Por presentar'),
    ('Presentada', 'Presentada'),
    ('Justificada', 'Justificada'),
    ('Concedida', 'Concedida'),
    ('Denegada', 'Denegada'),
)


class Subsidy(models.Model):

    id = models.AutoField(primary_key=True)

    # Fecha en la que se presenta la subvención
    presentation_date = models.DateField(
        verbose_name="Fecha de presentación", null=True, blank=True)
    # Fecha de cobro de la subvención
    payment_date = models.DateField(
        verbose_name="Fecha de cobro", null=True, blank=True)
    # Organismo
    organism = models.CharField(max_length=100, verbose_name="Organismo")
    # Fecha de presentación de la justificación
    presentation_justification_date = models.DateField(
        verbose_name="Fecha de presentación de la justificación", null=True, blank=True)
    # Fecha de resolución provisional
    provisional_resolution = models.DateField(
        verbose_name="Resolución provisional", null=True, blank=True)
    # Fecha de resolución definitiva
    final_resolution = models.DateField(
        verbose_name="Resolución definitiva", null=True, blank=True)
    # Importe de la subvención
    amount = models.FloatField(
        validators=[MinValueValidator(0)], verbose_name="Cantidad")

    # Nombre completo (con apellidos) de la persona o entidad que dona
    name = models.CharField(max_length=200, verbose_name="Nombre completo")
    # Estado de la Subvención
    status = models.CharField(
        max_length=50, choices=SUBSIDY_STATUS, verbose_name="Estado")
    #Observaciones
    notes = models.TextField(blank=True, verbose_name='Observaciones')
    #Relacione con la etidad Ong
    ong = models.ForeignKey(Ong, on_delete=models.CASCADE,
                            related_name='subvencion', verbose_name="ONG")
    # slug = models.SlugField(max_length=200, unique=True, editable=False)

    def save(self, force_insert=False, force_update=False, using=None,
             update_fields=None):
        self.clean()
       # self.slug = slugify(self.organism + ' ' + str(self.id)+' '+ self.name)

        if self.amount < 0:
            raise ValidationError("El importe no puede ser negativo")
        
        if self.presentation_date and self.presentation_justification_date:
            if self.presentation_date > self.presentation_justification_date:
                raise ValidationError(
                    "La fecha de presentación de la justificación no puede ser anterior a la de presentación de la subvención")

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
