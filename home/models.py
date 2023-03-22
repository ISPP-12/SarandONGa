from xml.dom import ValidationErr
from django.db import models
from django.core.validators import MinValueValidator
from django.core.validators import RegexValidator
from django.utils.text import slugify

PAYMENT_METHOD = (
    ('T', 'Transferencia'),
    ('TB', 'Tarjeta Bancaria'),
    ('E', 'Efectivo'),
)

FREQUENCY = (
    ('A', 'Anual'),
    ('M', 'Mensual'),
    ('T', 'Trimestral'),
    ('S', 'Semestral'),
)


class Home(models.Model):
    id = models.AutoField(primary_key=True)

    name = models.CharField(default="", max_length=25, verbose_name="Nombre")
    payment_method = models.CharField(
        max_length=50, choices=PAYMENT_METHOD, verbose_name='Método de pago',)
    bank_account_number = models.CharField(max_length=24, verbose_name='Número de cuenta bancaria',
                                           validators=[RegexValidator(regex=r'^ES\d{2}\s?\d{4}\s?\d{4}\s?\d{1}\d{1}\d{10}$',
                                                                      message='El número de cuenta no es válido.')])
    bank_account_holder = models.CharField(
        max_length=100, verbose_name='Titular de cuenta bancaria')
    bank_account_reference = models.CharField(
        max_length=100, verbose_name='Referencia de cuenta bancaria', validators=[RegexValidator(r'^[0-9]+$')])
    amount = models.DecimalField(max_digits=10, decimal_places=2,
                                 verbose_name='Cantidad', validators=[MinValueValidator(1)])
    frequency = models.CharField(
        max_length=20, choices=FREQUENCY, verbose_name='Frecuencia de pago')
    seniority = models.DateField(verbose_name='Antigüedad de la casa')
    province = models.CharField(
        default="Sevilla", verbose_name='Provincia', max_length=25)
    notes = models.TextField(blank=True, verbose_name='Observaciones')
    # status = models.CharField(
    #    max_length=20, choices=STATUS, verbose_name='Estado')
    # ¿CUAL ES EL ESTADO DE UNA CASA?¿EN RUINAS, EN OBRAS...?
    slug = models.SlugField(max_length=200, unique=True, editable=False)

    def __str__(self):
        return "{}, {}".format(self.name, self.province)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name + ' ' + self.province)
        if self.amount < 1:
            raise ValidationErr(
                'La cantidad debe ser mayor que 1')
        super(Home, self).save(*args, **kwargs)
