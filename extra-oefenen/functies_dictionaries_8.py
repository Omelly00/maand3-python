trainingen = [
    {"naam": "Python", "prijs": 49, "maanden": 3},
    {"naam": "Linux", "prijs": 39, "maanden": 2},
    {"naam": "Cloud", "prijs": 59, "maanden": 4}
]


def bereken_totale_kosten(trainingen):
    totaal = 0

    for item in trainingen:
        subtotaal = item["prijs"] * item["maanden"]
        totaal = totaal + subtotaal

    return totaal


totaalkosten = bereken_totale_kosten(trainingen)

print("Totaal trainingen:", totaalkosten)