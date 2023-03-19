from django.db import models


class Ong(models.Model):
    name = models.CharField(max_length=255, verbose_name="Nombre")
    # FALTA RELACION A PROYECTOS CUANDO SE CREE
    # RELACION A DONACION, SUBVENCION, STOCK, PERSONA HECHAS, SOLO REVISAR
