from django.db import models

# Create your models here.
class Corrieri(models.Model):
    nome_corriere = models.CharField(max_length=50)
    capacita_massima = (peso e volume) = models.CharField(max_length=50)
    area_di_copertura_geografica = models.CharField(max_length=50)
    codice_corriere = models.CharField(max_length=50)

    class Meta:
        verbose_name = "Corriere"
        verbose_name_plural = "Corrieri"

    def __str__(self):
        return "%s %s"%(self.nome_corriere)