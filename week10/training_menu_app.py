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


def toon_menu():
    print("")
    print("=== Training Planner ===")
    print("1. Toon alle trainingen")
    print("2. Toon totale kosten")
    print("3. Stoppen")


def toon_alle_trainingen(trainingen):
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

while True:
    toon_menu()

    keuze = input("Maak een keuze: ")

    if keuze == "1":
        toon_alle_trainingen(trainingen)

    elif keuze == "2":
        totale_kosten = bereken_totale_kosten(trainingen)
        print(f"Totale kosten: €{totale_kosten}")

    elif keuze == "3":
        print("Programma gestopt.")
        break

    else:
        print("Ongeldige keuze. Probeer opnieuw.")