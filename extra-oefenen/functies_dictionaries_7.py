taken = [
    {"titel": "Python oefenen", "status": "open"},
    {"titel": "GitHub pushen", "status": "afgerond"},
    {"titel": "README schrijven", "status": "open"}
]


def toon_open_taken(taken):
    for taak in taken:
        if taak["status"] == "open":
            print(taak["titel"], "-", taak["status"])


toon_open_taken(taken)