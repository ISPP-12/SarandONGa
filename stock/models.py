from django.db import models
from django.core.validators import MinValueValidator

class Stock(models.Model):   
    id= models.AutoField(primary_key=True)
    name = models.CharField(max_length=200)
    quantity = models.DecimalField(max_digits=10, decimal_places=2,validators=[MinValueValidator(1)])

    def __str__(self):
        return self.name