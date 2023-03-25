from django.db import models
from ong.models import Ong
from django.core.validators import MinValueValidator
from django.utils.text import slugify


class Stock(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=200, verbose_name="Nombre")
    ong = models.ForeignKey(Ong, on_delete=models.CASCADE,
                            related_name='suministro', verbose_name="ONG")
    quantity = models.DecimalField(max_digits=10, decimal_places=2, validators=[
                                   MinValueValidator(1)], verbose_name="Cantidad")
    #slug = models.SlugField(max_length=200, unique=True, editable=False)
    photo = models.ImageField(verbose_name="Foto", upload_to="./static/img/stock/", null=True, blank=True)

    def save(self, *args, **kwargs):
       # self.slug = slugify(self.name + ' ' + str(self.id))
        super(Stock, self).save(*args, **kwargs)
    def __str__(self):
        return self.name


    class Meta:
        verbose_name = 'Inventario'
        verbose_name_plural = 'Inventario'
