from django.db import models
from django.utils import timezone


class Donation(models.Model):
    id= models.AutoField(primary_key=True)
    #Titulo y descripción de la donación
    title = models.CharField(max_length=200)
    description = models.TextField()
    #Fecha de creación de la donación (automática)
    created_date = models.DateTimeField(default=timezone.now)
    #Importe de la donación
    amount= models.DecimalField(max_digits=10, decimal_places=2)
    #Información del donante
    donor_name= models.CharField(max_length=100)
    donor_surname=models.CharField(max_length=250)
    donor_email= models.EmailField()

    #Dejo esto comentado pero es para almacenar un documento correspondiente a la donación, si fuese necesario
    #document= models.FileField(blank=True, null=True)


    def __str__(self):
        return self.title
