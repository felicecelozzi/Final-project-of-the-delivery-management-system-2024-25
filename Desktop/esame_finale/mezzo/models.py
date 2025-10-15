from django.db import models

# Create your models here.
class Mezzo(models.Model):
    codice_mezzo = models.CharField(max_length=50)
    targa = models.CharField(max_length=50)
    capacita_massima_peso = models.CharField(max_length=50)
    capacita_massima_volume = models.CharField(max_length=50)

    class Meta:
        verbose_name = "Mezzo"
        verbose_name_plural = "Mezzi"

    def __str__(self):
        return "%s %s"%(self.codice_mezzo)