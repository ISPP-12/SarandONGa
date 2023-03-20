from django.db import models
from django.utils import timezone
from django.core.validators import MinValueValidator


class Payment(models.Model):
    id = models.AutoField(primary_key=True)
    # Fecha y cantidad de la operación
    payday = models.DateTimeField(
        default=timezone.now, verbose_name="Día de cobro")
    amount = models.DecimalField(max_digits=10, decimal_places=2, validators=[
                                 MinValueValidator(0)], verbose_name="Importe")

    # ACTUALMENTE ESTO FALLA PORQUE SERVICIO Y PADRINO NO EXISTEN
    # godfather = models.ForeignKey(Godfather, on_delete=models.CASCADE)
    # CUANDO SE CREE SERVICIO PONER LA LÍNEA DE ARRIBA PERO A PAGO <3

    def __str__(self):
        return "{}: {}".format(self.payday, self.amount)
