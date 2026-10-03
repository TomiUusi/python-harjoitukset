

class Julkaisu:
    def __init__(self, nimi):
        self.nimi = nimi

    def tulosta_tiedot(self):
            print(f'\nJulkaisun nimi: {self.nimi}')


class Kirja(Julkaisu):
    def __init__(self, nimi, kirjoittaja, sivumäärä):
        self.kirjoittaja = kirjoittaja
        self.sivumäärä = sivumäärä
        super().__init__(nimi)

    def tulosta_tiedot(self):
        super().tulosta_tiedot()
        print(f'Kirjoittaja: {self.kirjoittaja}')
        print(f'Sivumäärä: {self.sivumäärä} sivua')
        
    


class Lehti(Julkaisu):
    def __init__(self, nimi, päätoimittaja):
        self.päätoimittaja = päätoimittaja
        super().__init__(nimi)

    def tulosta_tiedot(self):
            super().tulosta_tiedot()
            print(f'Päätoimittaja: {self.päätoimittaja}')


kirja1 = Kirja('Hytti n:o 6', 'Rosa Liksom', 200)
lehti1 = Lehti('Aku Ankka', 'Aki Hyyppä')

kirja1.tulosta_tiedot()
lehti1.tulosta_tiedot()

