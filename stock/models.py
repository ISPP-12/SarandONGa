from django.db import models
from ong.models import Ong
from django.core.validators import MinValueValidator


class Stock(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=200, verbose_name="Nombre")
    ong = models.ForeignKey(Ong, on_delete=models.CASCADE,
                            related_name='suministro', verbose_name="ONG")
    quantity = models.DecimalField(max_digits=10, decimal_places=2, validators=[
                                   MinValueValidator(1)], verbose_name="Cantidad")

    def __str__(self):
        return self.name
