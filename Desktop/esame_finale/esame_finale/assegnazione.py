def assegna_ordine(ordine, corrieri):
    candidati = []
    for corriere in corrieri:
        for mezzo in corriere.mezzi:
            if not copre_area(corriere.area, ordine.indirizzo):
                continue
            distanza = calcola_distanza(mezzo.posizione, ordine.indirizzo)
            if mezzo.capacita_peso >= ordine.peso and mezzo.capacita_volume >= ordine.volume:
                candidati.append((corriere, mezzo, distanza))

    if not candidati:
        raise Exception("Nessun corriere disponibile per questo ordine.")

    candidati.sort(key=lambda x: (
        priorita_valore(ordine.priorita),
        x[2]  # distanza
    ))

    corriere_scelto, mezzo_scelto, _ = candidati[0]

    ordine.corriere = corriere_scelto
    ordine.mezzo = mezzo_scelto
    ordine.stato = "Assegnato"
    ordine.codice_assegnazione = genera_codice()

    mezzo_scelto.capacita_peso -= ordine.peso
    mezzo_scelto.capacita_volume -= ordine.volume

    return ordine
