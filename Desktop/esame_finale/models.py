from django.db import models

# classi
class prodotto:
    def stampa(self):
        print(prodotto)

class corriere:
    def stampa(self):
        print(corriere)

class ordine:
    def stampa(self):
        print(ordine)

class consegne:
    def stampa(self):
        print(consegne)

# Oggetti
Pr=prodotto()
Cor=corriere()
Or=ordine()
Con=consegne()
Pr.stampa()
Cor.stampa()
Or.stampa()
Con.stampa()