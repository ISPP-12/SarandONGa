from xml.dom import ValidationErr
from django.db import models
from django.core.validators import MinValueValidator
from django.core.validators import RegexValidator
#from django.utils.text import slugify
from django.utils import timezone
from xml.dom import ValidationErr

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
                                                                      message='El número de cuenta no es válido.')], null=True, blank=True)
    bank_account_holder = models.CharField(
        max_length=100, verbose_name='Titular de cuenta bancaria', null=True, blank= True)
    bank_account_reference = models.CharField(
        max_length=100, verbose_name='Referencia de cuenta bancaria', validators=[RegexValidator(r'^[0-9]+$')], blank= True, null=True)
    amount = models.DecimalField(max_digits=10, decimal_places=2,
                                 verbose_name='Cantidad', validators=[MinValueValidator(1)])
    frequency = models.CharField(
        max_length=20, choices=FREQUENCY, verbose_name='Frecuencia de pago')
    start_date = models.DateField(
        default=timezone.now, verbose_name="Fecha de alta", null=True, blank=True)
    termination_date = models.DateField(verbose_name="Fecha de baja", null=True, blank=True)
    province = models.CharField(
        default="Sevilla", verbose_name='Provincia', max_length=25)
    notes = models.TextField(blank=True, verbose_name='Observaciones')
    # status = models.CharField(
    #    max_length=20, choices=STATUS, verbose_name='Estado')
    # ¿CUAL ES EL ESTADO DE UNA CASA?¿EN RUINAS, EN OBRAS...?
    #slug = models.SlugField(max_length=200, unique=True, editable=False)

    def __str__(self):
        return "{}, {}".format(self.name, self.province)

    def save(self, *args, **kwargs):
        if self.start_date and self.termination_date:
            if self.termination_date < self.start_date:
                raise ValidationErr(
                    "La fecha de baja debe ser posterior a la fecha de alta.")
            elif self.amount < 1:
                raise ValidationErr(
                    "La cantidad debe ser mayor a 1.")
            else:
               # self.slug = slugify(self.name + ' ' + self.province)
               if self.bank_account_holder == None:
                    self.bank_account_holder = "Pago por efectivo"
                    self.bank_account_reference = "Pago por efectivo"
                    self.bank_account_number = "Pago por efectivo"
                    super(Home, self).save(*args, **kwargs)
        else:
         #   self.slug = slugify(self.name + ' ' + self.province)
            super(Home, self).save(*args, **kwargs)


    class Meta:
        verbose_name = 'Casa'
        verbose_name_plural = 'Casas'

