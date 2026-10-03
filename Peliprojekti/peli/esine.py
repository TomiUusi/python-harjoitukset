class Esine:
    def __init__(self, nimi, hinta, ympäristö_pisteet):
        self.nimi = nimi
        self.hinta = hinta
        self.ympäristö_pisteet = ympäristö_pisteet

    def __str__(self):
        return f'{self.nimi} {self.hinta}'