taken = [
    {"titel": "Python functies oefenen", "status": "open"},
    {"titel": "Dictionaries begrijpen", "status": "open"},
    {"titel": "Code pushen naar GitHub", "status": "afgerond"}
]


def toon_alle_taken(taken):
    print("\nAlle taken:")
    for taak in taken:
        print("-", taak["titel"], "| status:", taak["status"])


def toon_open_taken(taken):
    print("\nOpen taken:")
    for taak in taken:
        if taak["status"] == "open":
            print("-", taak["titel"])


def markeer_als_afgerond(taken, titel):
    for taak in taken:
        if taak["titel"] == titel:
            taak["status"] = "afgerond"
            return taak

    return None


toon_alle_taken(taken)
toon_open_taken(taken)

aangepaste_taak = markeer_als_afgerond(taken, "Python functies oefenen")

if aangepaste_taak:
    print("\nTaak aangepast:", aangepaste_taak["titel"])
else:
    print("\nTaak niet gevonden.")

toon_alle_taken(taken)