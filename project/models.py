from django.db import models
from django.core.validators import MinValueValidator
from ong.models import Ong
#from django.utils.text import slugify


# Create your models here.


class Project(models.Model):
    title = models.CharField(
        max_length=100, verbose_name="Título del proyecto", blank=False, null=False)
    country = models.CharField(
        max_length=100, blank=True, null=True, verbose_name="País")
    start_date = models.DateField(
        null=True, blank=True, verbose_name="Fecha de inicio del proyecto")
    end_date = models.DateField(
        null=True, blank=True, verbose_name="Fecha de finalización del proyecto")
    number_of_beneficiaries = models.IntegerField(
        null=True, blank=True, verbose_name="Número de beneficiarios", validators=[MinValueValidator(0)])
    amount = models.IntegerField(
        null=True, blank=True, verbose_name="Cantidad solicitada", validators=[MinValueValidator(1)])
    announcement_date = models.DateField(
        null=True, blank=True, verbose_name="Fecha de convocatoria")
    ong = models.ForeignKey(
        Ong, on_delete=models.CASCADE, related_name='project')
    #slug = models.SlugField(max_length=200, unique=True, editable=False)

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
      #  self.slug = slugify(self.title + ' ' + self.country + ' ' + str(self.amount))

        if self.start_date and self.end_date:
            if self.end_date < self.start_date:
                raise Exception(
                    "La fecha de finalización del proyecto no puede ser anterior a la de inicio")
        super(Project, self).save(*args, **kwargs)

    class Meta:
        ordering = ['title']
        verbose_name = 'Proyecto'
        verbose_name_plural = 'Proyectos'
