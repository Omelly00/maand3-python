cursussen = [
    {
        "naam": "Python basis",
        "prijs": 49,
        "niveau": "beginner"
    },
    {
        "naam": "Linux fundamentals",
        "prijs": 39,
        "niveau": "beginner"
    },
    {
        "naam": "Cloud basics",
        "prijs": 59,
        "niveau": "intermediate"
    }
]


def toon_cursussen(cursussen):
    for cursus in cursussen:
        print(cursus["naam"], "-", cursus["prijs"], "euro")


toon_cursussen(cursussen)