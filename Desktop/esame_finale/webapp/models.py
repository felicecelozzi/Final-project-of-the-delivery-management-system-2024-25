from django.db import models

class StatoOrdineChoices(models.TextChoices):
    ASSEGNATO = 'Assegnato', 'Assegnato'
    TRANSITO = 'Transito', 'Transito'
    IN_CONSEGNA = 'In Consegna', 'In Consegna'
    COMPLETATO = 'Completato', 'Completato'

class Stato_Ordine(models.Model):
    codice_stato = models.CharField(max_length=10, default='STATO')
    stato_attuale = models.CharField(
        max_length=20,
        choices=StatoOrdineChoices.choices,
        default=StatoOrdineChoices.ASSEGNATO
    )

    def __str__(self):
        return f"{self.codice_stato} - {self.stato_attuale}"

class Ordini(models.Model):
    PRIORITA = [
        ('Alta', 'Priorità Alta'), 
        ('Media', 'Priorità Media'),
        ('Bassa', 'Priorità Bassa')
    ]
    id_ordine = models.CharField(max_length=50, unique=True)
    indirizzo_di_consegna = models.CharField(max_length=50)
    data_e_ora_stimata_di_consegna_richiesta = models.CharField(max_length=50)
    priorità = models.CharField(max_length=10, choices=PRIORITA)
    stato_ordine = models.ForeignKey(Stato_Ordine, null=True, on_delete=models.SET_NULL)

    class Meta:
        verbose_name = "Ordine"
        verbose_name_plural = "Ordini"

    def __str__(self):
        return f"{self.id_ordine}"


class Corrieri(models.Model):
    nome_corriere = models.CharField(max_length=50, unique=True)
    indirizzo_corriere = models.CharField(max_length=255, default='Via Tirino')
    capacita_massima = models.IntegerField(default=0)
    area_di_copertura_geografica = models.CharField(max_length=50)
    codice_corriere = models.CharField(max_length=50)

    class Meta:
        verbose_name = "Corriere"
        verbose_name_plural = "Corrieri"

    def __str__(self):
        return f"{self.nome_corriere}"


class Mezzo(models.Model):
    codice_mezzo = models.CharField(max_length=50, unique=True)
    targa = models.CharField(max_length=50)
    capacita_massima_peso = models.IntegerField(null=True)
    capacita_massima_volume = models.IntegerField(null=True)

    class Meta:
        verbose_name = "Mezzo"
        verbose_name_plural = "Mezzi"

    def __str__(self):
        return f"{self.codice_mezzo} - Targa: {self.targa}"

class ConfigurazioneAPI(models.Model):
    nome = models.CharField(max_length=50, unique=True)
    api_key = models.CharField(max_length=255)

    def __str__(self):
        return self.nome