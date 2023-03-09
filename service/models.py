from django.db import models

from person import models as person_models
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
        service_type = models.CharField(max_length=50, choices=SERVICES_TYPE,verbose_name="Tipo de servicio")
        user_type = models.CharField(max_length=50, choices=person_models.ASEMUSER_TYPE,verbose_name="Tipo de usuario ASEM")
        amount = models.FloatField(verbose_name="Precio")
        date = models.DateTimeField(default=timezone.now)

        def __str__(self):
            return self.service_type

class Service(models.Model):
    id = models.AutoField(primary_key=True)
    service_type = models.CharField(max_length=50, choices=SERVICES_TYPE,verbose_name="Tipo de servicio")
    date = models.DateTimeField(default=timezone.now)
    attendance = models.BooleanField(verbose_name="Asistencia")
    #TODO: añadir una foreign key con pago cuando pago esté implementado
    #payment = models.ForeignKey(Payment, verbose_name="Pago")
    asem_user = models.ForeignKey(person_models.ASEMUser, verbose_name="Usuario ASEM", on_delete=models.CASCADE)

    @property
    def amount(self):
        try:
            return ServiceAmount.objects.filter(service_type=self.service_type, user_type=self.asem_user.user_type, date__lte=self.date).latest('date').amount
        except ServiceAmount.DoesNotExist:
            return 0

    def __str__(self):
        return self.service_type