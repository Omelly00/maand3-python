def toon_auto(auto):
    print("Merk:", auto["merk"])
    print("Model:", auto["model"])
    print("Bouwjaar:", auto["bouwjaar"])
    print("Kleur:", auto["kleur"])


auto = {
    "merk": "Toyota",
    "model": "Corolla",
    "bouwjaar": 2020,
    "kleur": "zwart"
}

toon_auto(auto)