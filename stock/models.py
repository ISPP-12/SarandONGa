from django.db import models

class Stock(models.Model):   
    id= models.AutoField(primary_key=True)
    name = models.CharField(max_length=200)
    quantity = models.DecimalField(max_digits=10, decimal_places=2)
    
    def __str__(self):
        return self.name