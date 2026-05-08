class Training:
    def __init__(self, naam, prijs, maanden):
        self.naam = naam
        self.prijs = prijs
        self.maanden = maanden


python_training = Training("Python", 49, 3)
linux_training = Training("Linux", 39, 2)
cloud_training = Training("Cloud", 59, 4)

print(python_training.naam)
print(linux_training.naam)
print(cloud_training.naam)