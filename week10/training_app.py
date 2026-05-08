class Training:
    def __init__(self, naam, prijs, maanden):
        self.naam = naam
        self.prijs = prijs
        self.maanden = maanden

    def bereken_totaalprijs(self):
        return self.prijs * self.maanden

    def toon_info(self):
        print("----------------------")
        print(f"Training: {self.naam}")
        print(f"Prijs per maand: €{self.prijs}")
        print(f"Duur: {self.maanden} maanden")
        print(f"Totaalprijs: €{self.bereken_totaalprijs()}")


def toon_alle_trainingen(trainingen):
    print("Overzicht trainingen")

    for training in trainingen:
        training.toon_info()


def bereken_totale_kosten(trainingen):
    totaal = 0

    for training in trainingen:
        totaal = totaal + training.bereken_totaalprijs()

    return totaal


trainingen = [
    Training("Python", 49, 3),
    Training("Linux", 39, 2),
    Training("Cloud", 59, 4)
]

toon_alle_trainingen(trainingen)

totale_kosten = bereken_totale_kosten(trainingen)

print("----------------------")
print(f"Totale kosten alle trainingen: €{totale_kosten}")