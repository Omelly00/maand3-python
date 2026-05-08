def bereken_kosten(training):
    totaal = training["prijs"] * training["maanden"]
    return totaal


training = {
    "naam": "Python cursus",
    "prijs": 49,
    "maanden": 6
}

totaalbedrag = bereken_kosten(training)

print("Training:", training["naam"])
print("Totaal:", totaalbedrag)