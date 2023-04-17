from django.db import models
# from django.utils.text import slugify

PLAN_TYPES = (
    ('B', 'Básico'),
    ('P', 'Premium'),
)


class Ong(models.Model):
    name = models.CharField(max_length=255, verbose_name="Nombre")
    plan = models.CharField(max_length=50, choices=PLAN_TYPES,
                            verbose_name="Plan de pago", default='B', null=True, blank=True)
    premium_payment_date = models.DateField(
        verbose_name="Fecha de pago del plan Premium", null=True, blank=True)

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        # self.slug = slugify(self.name)
        super(Ong, self).save(*args, **kwargs)

    class Meta:
        verbose_name = 'ONG'
        verbose_name_plural = 'ONG'
