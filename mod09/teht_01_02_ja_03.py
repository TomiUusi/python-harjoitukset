class Auto:

    def __init__(self, rekisteritunnus, huippunopeus):
        self.rekisteritunnus = rekisteritunnus
        self.huippunopeus = huippunopeus
        self.nopeus = 0
        self.matka = 0

    def kiihdytä(self, muutos):
        self.nopeus += muutos
        # Auton nopeus ei saa kasvaa huippunopeutta suuremmaksi
        # Eikä alentua nollaa pienemmäksi
        if self.nopeus > self.huippunopeus:
            self.nepeus = self.huippunopeus
        elif self.nopeus < 0:
            self.nopeus = 0

    def kulje(self, aika):
        self.matka += aika * self.nopeus

auto = Auto('ABC-123', 142)

print(f'Auton rekisteritunnus: {auto.rekisteritunnus}')
print(f'Huippunopeu: {auto.huippunopeus}')
print(f'Nopeus: {auto.nopeus}')
print(f'Kuljettu matka: {auto.matka}')

auto.kiihdytä(30)
auto.kiihdytä(70)
auto.kiihdytä(50)
print(f'Auton nopeus kiihdytyksen jälkeen: {auto.nopeus}')
auto.kulje(1.5)
print(f'Kuljettu matka 1,5h jälkeen: {auto.matka}km')
auto.kiihdytä(-200)
print(f'Auton nopeus jarrutuksen jälkeen: {auto.nopeus}')
