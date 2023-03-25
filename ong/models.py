from django.db import models
from django.utils.text import slugify


class Ong(models.Model):
    name = models.CharField(max_length=255, verbose_name="Nombre")
    # FALTA RELACION A PROYECTOS CUANDO SE CREE
    # RELACION A DONACION, SUBVENCION, STOCK, PERSONA HECHAS, SOLO REVISAR
    slug = models.SlugField(max_length=200, unique=True, editable=False)

    def __str__(self):
        return self.name
    
    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super(Ong, self).save(*args, **kwargs)
