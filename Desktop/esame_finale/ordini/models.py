from django.db import models

# Create your models here.
class Ordini(models.Model):
    id_ordine = models.CharField(max_length=50)
    indirizzo_di_consegna = models.CharField(max_length=50)
    data_e_ora_stimata_di_consegna_richiesta = models.CharField(max_length=50)
    priorità = (alta, media, bassa) = models.CharField(max_length=50)

    class Meta:
        verbose_name = "Ordine"
        verbose_name_plural = "Ordini"

    def __str__(self):
        return "%s %s"%(self.id_ordine)