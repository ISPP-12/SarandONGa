from django.db import models
from django.utils import timezone
from django.core.validators import MinValueValidator, RegexValidator
from ong.models import Ong
# from django.utils.text import slugify

DNI_REGEX = r'^\d{8}[A-Z]$'

DNI_VALIDATOR = RegexValidator(
    regex=DNI_REGEX,
    message='Introduce un DNI válido (8 números y 1 letra).'
)
class Donation(models.Model):
    id = models.AutoField(primary_key=True)
    # Titulo y descripción de la donación
    title = models.CharField(max_length=200, verbose_name="Título")
    description = models.TextField(verbose_name="Descripción", null=True, blank=True)
    # Fecha de creación de la donación (automática)
    created_date = models.DateField(
        default=timezone.now, verbose_name="Fecha creación")
    # Importe de la donación
    amount = models.DecimalField(max_digits=10, decimal_places=2, validators=[
                                 MinValueValidator(0.1)], verbose_name="Importe")
    # Información del donante
    donor_name = models.CharField(max_length=100, verbose_name="Nombre")
    donor_surname = models.CharField(max_length=250, verbose_name="Apellidos")
    donor_dni = models.CharField(
        max_length=9,
        validators=[DNI_VALIDATOR],
        verbose_name='DNI'
    )
    donor_address = models.CharField(max_length=200, verbose_name="Dirección", null=True, blank=True)
    donor_email = models.EmailField(verbose_name="Correo Electrónico")
    ong = models.ForeignKey(
        Ong, on_delete=models.CASCADE, related_name='donacion', verbose_name="ONG")
    # slug = models.SlugField(max_length=200, unique=True, editable=False)
    document = models.FileField(
        verbose_name="Documento", upload_to="./media/docs/donation/", null=True, blank=True)
    # documents = models.JSONField(
    #     verbose_name="Documentos", null=True, blank=True)

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
       # self.slug = slugify(self.title + ' ' + self.description)
        super(Donation, self).save(*args, **kwargs)

    class Meta:
        verbose_name = 'Donación'
        verbose_name_plural = 'Donaciones'
