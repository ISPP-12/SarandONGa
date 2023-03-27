from django.db import models
#from django.utils.text import slugify
from person import models as person_models
from payment import models as payment_models
from django.utils import timezone
# Create your models here.

SERVICES_TYPE = (
    ('Fisioterapia','Fisioterapia'),
    ('Logopedia', 'Logopedia'),
    ('Transporte Adaptado', 'Transporte Adaptado'),
    ('Neuropsicología', 'Neuropsicología'),
    ('Atención Social', 'Atención Social'),
    ('Atención Jurídica', 'Atención Jurídica'),
    ('Atención Psicológica', 'Atención Psicológica'),
    ('Trabajo Social', 'Trabajo Social'),
    ('Ocio y Tiempo Libre', 'Ocio y Tiempo Libre'),
)

class ServiceAmount(models.Model):
    id = models.AutoField(primary_key=True)
    service_type = models.CharField(max_length=50, choices=SERVICES_TYPE,verbose_name="Tipo de servicio" )
    user_type = models.CharField(max_length=50, choices=person_models.ASEMUSER_TYPE,verbose_name="Tipo de usuario ASEM")
    amount = models.FloatField(verbose_name="Precio")
    date = models.DateTimeField(default=timezone.now, verbose_name="Fecha")
    def __str__(self):
        return self.service_type + str(self.date)

    class Meta:
        verbose_name = 'Cantidad de servicio'
        verbose_name_plural = 'Cantidades de servicios'

class Service(models.Model):
    id = models.AutoField(primary_key=True)
    service_type = models.CharField(max_length=50, choices=SERVICES_TYPE,verbose_name="Tipo de servicio")
    date = models.DateTimeField(default=timezone.now, verbose_name="Fecha")
    attendance = models.BooleanField(verbose_name="Asistencia")
    payment = models.ForeignKey(payment_models.Payment, verbose_name="Pago", on_delete=models.SET_NULL, null=True)
    asem_user = models.ForeignKey(person_models.ASEMUser, verbose_name="Usuario ASEM", on_delete=models.CASCADE)
   # slug = models.SlugField(max_length=200, unique=True, editable=False)

    @property
    def amount(self):
        try:
            return ServiceAmount.objects.filter(service_type=self.service_type, user_type=self.asem_user.user_type, date__lte=self.date).latest('date').amount
        except ServiceAmount.DoesNotExist:
            return 0
    def __str__(self):
        return self.service_type + ' - ' + str(self.date) + ' - ' + self.asem_user.surname + ', ' + self.asem_user.name
    
    def save(self, *args, **kwargs):
       ## self.slug = slugify(self.service_type + ' ' + str(self.id))
        super(Service, self).save(*args, **kwargs)
    class Meta:
        verbose_name = 'Sevicio'
        verbose_name_plural = 'Servicios'

