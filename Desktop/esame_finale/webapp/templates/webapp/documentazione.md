## ESAME FINALE - 19/06/2025 SVILUPPO SOFTWARE 2024/2025
 
 ## Descrizione del progetto 

Il software è un sistema gestionale per la logistica delle consegne, progettato per monitorare, organizzare e ottimizzare la gestione degli ordini, corrieri, mezzi di trasporto e lo stato delle spedizioni.
L’obiettivo è fornire una piattaforma che consenta la registrazione degli ordini, l’associazione di corrieri e mezzi e il tracciamento dello stato di consegna di ciascun ordine.


## Tecnologie Utilizzate

Linguaggio: Python, Js

Framework: Django (Django ORM per il database)

Database: PostgreSQL

Modello dati: definito tramite django.db.models


## Models
1. Modello: Stato_Ordine
Gestisce lo stato attuale di ciascun ordine tramite una tabella separata.

Campi:

codice_stato: codice identificativo generico (es. "STATO").

stato_attuale: stato dell’ordine, scelto da un set predefinito.

Scelte di stato (StatoOrdineChoices):

Assegnato

Transito

In Consegna

Completato

Utile per tracciare e filtrare gli ordini in base alla fase della consegna.

2. Modello: Ordini
Contiene tutte le informazioni necessarie per registrare un ordine e seguirne la consegna.

Campi:

id_ordine: identificativo univoco dell’ordine.

indirizzo_di_consegna: indirizzo dove recapitare il pacco.

data_e_ora_stimata_di_consegna_richiesta: richiesta temporale della consegna (stringa generica).

priorità: livello di urgenza (Alta, Media, Bassa).

stato_ordine: collegamento (ForeignKey) al modello Stato_Ordine.

Permette la gestione degli ordini con priorità e stato associati.

3. Modello: Corrieri
Rappresenta un'entità corriere (azienda o persona) che effettua le consegne.

Campi:

nome_corriere: nome identificativo (univoco).

indirizzo_corriere: sede del corriere.

capacita_massima: capacità in numero di ordini o peso gestibile.

area_di_copertura_geografica: zona geografica servita.

codice_corriere: codice identificativo interno.

Permette di organizzare e assegnare ordini a corrieri idonei in base alla copertura e capacità.

4. Modello: Mezzo
Definisce i mezzi di trasporto utilizzati dai corrieri per effettuare le consegne.

Campi:

codice_mezzo: codice identificativo del veicolo.

targa: numero di targa del mezzo.

capacita_massima_peso: capacità in kg (facoltativa).

capacita_massima_volume: capacità in litri/m³ (facoltativa).

Utile per associare i mezzi alle capacità logistiche richieste per ogni consegna.

 Funzionalità Implementate

Registrazione Ordini	Salvataggio di nuovi ordini nel sistema con dettagli completi.
Tracciamento Stato Ordini	Lo stato di ogni ordine può essere aggiornato dinamicamente.
Gestione Priorità Ordini	Gli ordini sono classificati per priorità: Alta, Media, Bassa.
Gestione Corrieri	Aggiunta e configurazione dei corrieri con zona e capacità.
Gestione Mezzi di Trasporto	Inserimento mezzi con targa, codice, capacità peso e volume.
Associazione Stato Ordine (ForeignKey)	Ogni ordine è collegato al proprio stato attuale in modo coerente.

## API
L'API è stata implementata con Open Route Service.

## Logica di Assegnazione
Assegnare automaticamente ogni nuovo ordine al corriere (e mezzo) più idoneo in base a:

Prossimità geografica (tra indirizzo di consegna e area di copertura del corriere).

Capacità residua (peso e volume disponibile sul mezzo).

Priorità dell’ordine (Alta, Media, Bassa).