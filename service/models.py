from django.db import models


# Create your models here.

SERVICES_TYPES = (
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

class Service(models.Model):

    id = models.AutoField(primary_key=True)

    service_type = models.CharField(max_length=50, choices=SERVICES_TYPES,verbose_name="Tipo de servicio")

    date = models.DateField(verbose_name="Fecha")

    attendance = models.BooleanField(verbose_name="Asistencia")

    amount = models.FloatField(verbose_name="Importe")

    #TODO: añadir una foreign key con pago cuando pago esté implementado
    #payment = models.ForeignKey(Payment, verbose_name="Pago")

    #TODO: añadir una foreign key con SclerosisUser cuando este último esté implementado
    #sclerosis_user = models.ForeignKey(SclerosisUser, verbose_name="Usuario Esclerosis", on_delete=models.CASCADE)

    def __str__(self):
        return self.service_type