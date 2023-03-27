from django.db import models
from person import models as person_models
from home import models as home_models
from xml.dom import ValidationErr
# from django.utils.text import slugify


class Sponsorship(models.Model):
    id = models.AutoField(primary_key=True)
    sponsorship_date = models.DateField(verbose_name='Fecha de apadrinamiento')
    termination_date = models.DateField(verbose_name='Fecha de baja')
    godfather = models.ManyToManyField(
        person_models.GodFather, verbose_name="Padrinos", blank=True)
    child = models.ForeignKey(
        person_models.Child, verbose_name="Niños", on_delete=models.CASCADE)
    home = models.ForeignKey(
        home_models.Home, verbose_name="Casa", on_delete=models.SET_NULL, null=True, blank=True)

    slug = models.SlugField(max_length=200, unique=True, editable=False)

    def __str__(self):
        # if (self.home):
        return "Apadrinamiento para {}".format(self.child.name)

    def save(self, *args, **kwargs):
       # self.slug = slugify(self.home.name + ' ' + self.godfather.name + ' ' + self.child.name)
        if self.sponsorship_date is not None:
            if self.termination_date is not None:
                if self.sponsorship_date > self.termination_date:
                    raise ValidationErr(
                        "La fecha de empadronamiento no puede ser posterior a la fecha de baja")

            if self.sponsorship_date < self.child.birth_date:
                raise ValidationErr(
                    "La fecha de empadronamiento no puede ser anterior a la fecha de nacimiento del niño")

        super(Sponsorship, self).save(*args, **kwargs)

    class Meta:
        verbose_name = 'Apadrinamiento'
        verbose_name_plural = 'Apadrinamientos'
