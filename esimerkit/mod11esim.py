# mod 11 - perintä esimerkkejä 

class Eläin:

    eläinten_lkm = 0

    def __init__(self, nimi, paino, synt_aika):
        self.nimi = nimi
        self.paino = paino
        self.synt_aika = synt_aika
        Eläin.eläinten_lkm += 1


    def liiku(self):
        print(f'{self.nimi} liikkuu jotenkin johonkin...')

    def tulosta_tiedot(self):
        print(f'Nimi: {self.nimi}')
        print(f'Paino: {self.paino}')
        print(f'Syntymä aika: {self.synt_aika}')


uusi_eläin = Eläin('joku elukka', 1500, 20250922)
uusi_eläin.liiku()

class Peto:
    def __init__(self, on_metsästäjä):
        self.on_metsästäjä = on_metsästäjä


class Ilves(Eläin):

    def kilju(self):
        print(f'{self.nimi} kiljuu...')

    def tulosta_tiedot(self):
        print('\n--------Ilves--------')
        super().tulosta_tiedot()


# Karhu perii kaksi luokkaa
class Karhu(Eläin, Peto):
    def __init__(self, nimi, paino, synt_aika, on_horroksessa, on_metsästäjä):
        self.on_horroksessa = on_horroksessa
        self.on_metsästäjä = on_metsästäjä
        super().__init__(nimi, paino, synt_aika,)
        

    def karju(self):
        print(f'{self.nimi} karjuu!!')

    def liiku(self):
        print(f'Karhu {self.nimi} tallustelee eteenpäin')


    def tulosta_tiedot(self):
            print('\n--------Karhu--------')
            super().tulosta_tiedot()


# Eläintarha eläimiä varten (assosiaatio esimerkki)
class Eläintarha:
    def __init__(self, nimi):
        self.eläimet = []
        self.nimi = nimi

    def lisää_eläin(self, eläin):
        self.eläimet.append(eläin)

    def listaa_kaikki(self):
        print(f'\nEläintarhan {self.nimi} kaikki eläimet ({len(self.eläimet)} kpl)')
        for eläin in self.eläimet:
            eläin.tulosta_tiedot()

ilves1 = Ilves('Ilkka Ilves', 6500, 20210622)
ilves1.liiku()
ilves1.kilju()

karhu1 = Karhu('Otso Karhu', 155000, 20190315, False, True)
karhu1.karju()
karhu1.liiku()

tarha = Eläintarha('Korkeasaari')
tarha.lisää_eläin(ilves1)
tarha.lisää_eläin(karhu1)

tarha.listaa_kaikki()

print(f'\nEläimiä luotu yhteensä: {Eläin.eläinten_lkm}')



