from django.db import models


class Ong(models.Model):
    name = models.CharField(max_length=255)
    #FALTA RELACION A PROYECTOS CUANDO SE CREE
    #RELACION A DONACION, SUBVENCION, STOCK, PERSONA HECHAS, SOLO REVISAR
    def __str__(self):
        return self.name
