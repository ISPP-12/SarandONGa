from django.db import models
from django.utils import timezone
from django.core.validators import MinValueValidator
from project.models import Project
from django.utils.text import slugify



class Payment(models.Model):
    id = models.AutoField(primary_key=True)
    # Fecha y cantidad de la operación
    payday = models.DateTimeField(
        default=timezone.now, verbose_name="Día de cobro")
    amount = models.DecimalField(max_digits=10, decimal_places=2, validators=[
                                 MinValueValidator(0)], verbose_name="Importe")
    project = models.ForeignKey(
        Project, null=True, blank=True, on_delete=models.CASCADE, verbose_name="Proyecto")

    # ACTUALMENTE ESTO FALLA PORQUE SERVICIO Y PADRINO NO EXISTEN
    # godfather = models.ForeignKey(Godfather, on_delete=models.CASCADE)
    # CUANDO SE CREE SERVICIO PONER LA LÍNEA DE ARRIBA PERO A PAGO <3

    slug = models.SlugField(max_length=200, unique=True, editable=False)

    def __str__(self):
        return "{}: {}".format(self.payday, self.amount)


    def save(self, *args, **kwargs):
        self.slug = slugify(self.project.title + ' ' + str(self.amount))
        super(Payment, self).save(*args, **kwargs)

    class Meta:
        verbose_name = 'Pago'
        verbose_name_plural = 'Pagos'