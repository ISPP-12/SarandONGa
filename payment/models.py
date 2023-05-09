from django.db import models
from django.utils import timezone
from django.core.validators import MinValueValidator
from ong.models import Ong
from person.models import GodFather
from project.models import Project
from home.models import Home


class Payment(models.Model):
    id = models.AutoField(primary_key=True)
    # Fecha y cantidad de la operación
    payday = models.DateField(default=timezone.now, verbose_name="Día de cobro")
    amount = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        validators=[MinValueValidator(0)],
        verbose_name="Importe",
    )
    concept = models.CharField(
        max_length=150, verbose_name="Concepto", blank=False, null=False
    )

    ong = models.ForeignKey(
        Ong, on_delete=models.CASCADE, related_name="payment", verbose_name="ONG"
    )

    paid = models.BooleanField(default=True, verbose_name="Pagado")

    godfather = models.ForeignKey(
        GodFather,
        null=True,
        blank=True,
        on_delete=models.CASCADE,
        verbose_name="Padrino",
    )

    home = models.ForeignKey(
        Home, null=True, blank=True, on_delete=models.CASCADE, verbose_name="Casa"
    )

    project = models.OneToOneField(
        Project,
        null=True,
        blank=True,
        on_delete=models.CASCADE,
        verbose_name="Proyecto",
    )

    def __str__(self):
        return "{} - {}".format(self.concept, str(self.payday))

    def save(self, *args, **kwargs):
        if self.amount < 0:
            raise Exception("La cantidad del pago no puede ser negativa")
        if self.amount > 9999999999:
            raise Exception("La cantidad del pago no puede ser superior a 10 dígitos")
        if self.godfather and self.home:
            raise Exception("No puedes elegir a la vez un padrino y una casa")
        # check that self.amount is decimal:
        if not isinstance(self.paid, bool):
            raise Exception("El pago debe ser un booleano")
        super(Payment, self).save(*args, **kwargs)

    class Meta:
        verbose_name = "Pago"
        verbose_name_plural = "Pagos"
