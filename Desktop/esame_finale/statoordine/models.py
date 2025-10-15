from django.db import models

# Create your models here.
class StatoOrdine(models.TextChoices):
    ASSEGNATO = 'Assegnato', 'Assegnato'
    TRANSITO = 'Transito', 'Transito'
    IN_CONSEGNA = 'In Consegna', 'In Consegna'
    COMPLETATO = 'Completato', 'Completato'