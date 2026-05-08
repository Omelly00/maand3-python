orders = [
    {
        "ordernummer": "PO1001",
        "bedrag": 250,
        "status": "goedgekeurd",
        "categorie": "ICT"
    },
    {
        "ordernummer": "PO1002",
        "bedrag": 1200,
        "status": "open",
        "categorie": "Facilitair"
    },
    {
        "ordernummer": "PO1003",
        "bedrag": 75,
        "status": "afgerond",
        "categorie": "Training"
    }
]


def toon_orders(orders):
    print("\nAlle orders:")
    for order in orders:
        print(order["ordernummer"], "-", order["categorie"], "-", order["bedrag"], "euro")


def toon_open_orders(orders):
    print("\nOpen orders:")
    for order in orders:
        if order["status"] == "open":
            print(order["ordernummer"], "-", order["categorie"])


def bereken_totaalbedrag(orders):
    totaal = 0

    for order in orders:
        totaal = totaal + order["bedrag"]

    return totaal


def check_hoge_bedragen(orders):
    print("\nOrders boven 1000 euro:")
    for order in orders:
        if order["bedrag"] > 1000:
            print(order["ordernummer"], "-", order["bedrag"], "euro")


toon_orders(orders)
toon_open_orders(orders)

totaal = bereken_totaalbedrag(orders)
print("\nTotaalbedrag:", totaal, "euro")

check_hoge_bedragen(orders)