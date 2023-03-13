from django.db import models
from django.utils import timezone
from django.core.validators import MinValueValidator


class Donation(models.Model):
    id= models.AutoField(primary_key=True)
    #Titulo y descripción de la donación
    title = models.CharField(max_length=200, verbose_name="Título")
    description = models.TextField(verbose_name="Descripción")
    #Fecha de creación de la donación (automática)
    created_date = models.DateTimeField(default=timezone.now,verbose_name="Fecha Creación")
    #Importe de la donación
    amount= models.DecimalField(max_digits=10, decimal_places=2, validators=[MinValueValidator(0.1)], verbose_name="Importe")
    #Información del donante
    donor_name= models.CharField(max_length=100,verbose_name="Nombre")
    donor_surname=models.CharField(max_length=250, verbose_name="Apellidos")
    donor_dni= models.CharField(max_length=9, unique=True, verbose_name="DNI/CIF")
    donor_address=models.CharField(max_length=200, verbose_name="Dirección")
    donor_email= models.EmailField(verbose_name="Correo Electrónico")

    #Dejo esto comentado pero es para almacenar un documento correspondiente a la donación, si fuese necesario
    #document= models.FileField(blank=True, null=True)


    def __str__(self):
        return self.title
