from django.db import models
from person import models as person_models
from home import models as home_models
from xml.dom import ValidationErr
from django.utils.text import slugify


class Sponsorship(models.Model):
    id= models.AutoField(primary_key=True)
    sponsorship_date = models.DateField(verbose_name='Fecha de apadrinamiento')
    termination_date = models.DateField(verbose_name='Fecha de baja')
    godfather = models.ForeignKey(person_models.GodFather, verbose_name="Padrinos", on_delete=models.SET_NULL, null=True)
    child = models.ForeignKey(person_models.Child, verbose_name="Niños", on_delete=models.CASCADE)
    home = models.ForeignKey(home_models.Home, verbose_name="Casa", on_delete=models.SET_NULL, null=True)

    slug = models.SlugField(max_length=200, unique=True, editable=False)

    def __str__(self):
        return "{}, {}, {}".format(self.home.name, self.godfather.name, self.child.name)
    
    def save(self, *args, **kwargs):
        self.slug = slugify(self.home.name + ' ' + self.godfather.name + ' ' + self.child.name)
        if self.godfather.ong != self.child.ong :
            raise ValidationErr(
                "The child and godfather cannot belong to diferent ONG")
        super(Sponsorship, self).save(*args, **kwargs)

    
    class Meta:
        verbose_name = 'Apadrinamiento'
        verbose_name_plural = 'Apadrinamientos'