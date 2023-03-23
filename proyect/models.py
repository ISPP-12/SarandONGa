from django.db import models
from django.utils.text import slugify
from ong.models import Ong

# Create your models here.

class Proyect(models.Model):
    title = models.CharField(max_length=100, verbose_name="Título del proyecto")
    country = models.CharField(max_length=100, blank=True, verbose_name="País")
    start_date = models.DateField(null=True, verbose_name="Fecha de inicio del proyecto")
    end_date = models.DateField(null=True, verbose_name="Fecha de finalización del proyecto")
    number_of_beneficiaries = models.IntegerField(null=True, verbose_name="Número de beneficiarios")
    amount = models.IntegerField(null=True, verbose_name="Cantidad solicitada")
    announcement_date = models.DateField(null=True, verbose_name="Fecha de convocatoria")
    ong = models.ForeignKey(Ong, on_delete=models.CASCADE, related_name='proyect')
    slug = models.SlugField(max_length=200, unique=True, editable=False)


    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title + ' ' + self.country + ' ' + self.amount)
        if self.end_date < self.start_date:
            raise Exception("La fecha de finalización del proyecto no puede ser anterior a la de inicio")
        super(Proyect, self).save(*args, **kwargs)
    
    class Meta:
        verbose_name = 'Proyecto'
        verbose_name_plural = 'Proyectos'