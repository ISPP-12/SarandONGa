from django.db import models
from django.utils import timezone
from person.models import GodFather


class Payment(models.Model):
    id= models.AutoField(primary_key=True)
    #Fecha y cantidad de la operación
    payday = models.DateTimeField(default=timezone.now)
    amount= models.DecimalField(max_digits=10, decimal_places=2)
    godfather = models.ForeignKey(GodFather, on_delete=models.CASCADE)
    
    #CUANDO SE CREE SERVICIO PONER LA LÍNEA DE ARRIBA PERO A PAGO <3



    def __str__(self):
        return "{}: {}".format(self.payday, self.amount)
