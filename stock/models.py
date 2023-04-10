from django.db import models
from ong.models import Ong
from django.core.validators import MinValueValidator
from django.forms import ValidationError
#from django.utils.text import slugify


class Stock(models.Model):

    id = models.AutoField(primary_key=True)
    #Nombre del suministro
    name = models.CharField(max_length=200, verbose_name="Nombre")

     #Modelo del suministro
    model = models.CharField(max_length=200, verbose_name="Modelo",null=True, blank=True)

    #Relación con la ONG
    ong = models.ForeignKey(Ong, on_delete=models.CASCADE,
                            related_name='suministro', verbose_name="ONG")
    #Cantidad de suministros
    quantity = models.IntegerField(validators=[
                                   MinValueValidator(1)], verbose_name="Cantidad")
    
    #Precio del suministro
    amount = models.DecimalField(max_digits=10, decimal_places=2, validators=[
                                 MinValueValidator(0)], verbose_name="Precio",null=True, blank=True)

    #Foto del suministro
    photo = models.ImageField(verbose_name="Foto", upload_to="./static/img/stock/", null=True, blank=True)

    #Observaciones del suministro
    notes = models.TextField(blank=True, verbose_name='Observaciones')

    #slug = models.SlugField(max_length=200, unique=True, editable=False)

    def save(self, *args, **kwargs):
       # self.slug = slugify(self.name + ' ' + str(self.id))
        if self.amount:
            if self.amount < 0:
                raise ValidationError("El importe no puede ser negativo")
        
        if self.quantity < 1:
            raise ValidationError("La cantidad no puede ser menor que 1")
        super(Stock, self).save(*args, **kwargs)
    def __str__(self):
        return self.name


    class Meta:
        verbose_name = 'Inventario'
        verbose_name_plural = 'Inventario'
