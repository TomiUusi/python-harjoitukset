class Pelaaja:

    def __init__(self, nimi, sijainti):
        self.nimi = nimi
        self.sijainti = sijainti
        self.esineet = []
        self.raha = 2000
        self.ympäristö_pisteet = 0

    def liiku(self, kohde):
        self.sijainti = kohde
        print(f'\nsiirryit kauppaan: {kohde.nimi}')

    def osta_tuote(self):
        if len(self.sijainti.esineet) == 0:
            print('Täällä ei ole puhelimia.')
            return

        print('\nKaupan puhelimet:')
        print('')
        for i, esine in enumerate(self.sijainti.esineet):
            print(f'{i+1}. {esine}€')
        print('')

        try:
            valinta = int(input('Minkä puhelimen haluat ostaa?: '))
        except ValueError:
            print('Virheellinen valinta.')
            return

        if 1 <= valinta <= len(self.sijainti.esineet):
            esine = self.sijainti.esineet[valinta - 1]

            if esine in self.esineet:
                print('Sinulla on jo tämä puhelin.')
            elif esine.hinta > self.raha:
                print('Sinulla ei ole tarpeeksi rahaa.')
            else:
                self.raha -= esine.hinta
                self.ympäristö_pisteet += esine.ympäristö_pisteet
                self.esineet.append(esine)
                print(f'Ostit puhelimen: {esine.nimi}')
        else:
            print('Virheellinen valinta.')

    def näytä_inventaario(self):
        print('----INVENTAARIO----')
        print('')
        if len(self.esineet) == 0:
            print('Inventaariosi on tyhjä.')
        else:
            for esine in self.esineet:
                print(f'> {esine.nimi}')
            print('')

    def loppu(self):
        
        print('\n=========== LOPPU ===========')

        if len(self.esineet) == 0:
            print('MINIMALISTI')
            print('Lähdit Luurikatu 22:sta tyhjin käsin.')
            print('Vanha luuri toimii vielä ihan hyvin, ja pankkitili kiittää.')

        elif len(self.esineet) >= 3:
            print('SALAINEN REITTI: KERÄILIJÄ')
            print('Kävelet ulos kaupasta taskut pullottaen puhelimia.')
            print('Yksi taittuu, toinen kestää ydinsodan ja kolmannella voit pelata matopeliä.')
            print(f'Puhelimia: {len(self.esineet)}kpl')
            print('Kokoelmasi on legendaarinen.')

        elif self.ympäristö_pisteet >= 25:
            print('YMPÄRISTÖSANKARI')
            print('Annoit vanhalle puhelimelle uuden elämän.')
            print(f'Ympäristöpisteesi: {self.ympäristö_pisteet}')
            print('Maapallo kiittää!')

        else:
            print('TEKNOLOGIAHIFISTELIJÄ')
            print('Kävelet ulos kaupasta kiiltävä uutuus kädessäsi.')
            print(f'Ympäristöpisteesi: {self.ympäristö_pisteet}')
            print('Kannattaa tutustua kestävän kehityksen tavoitteisiin.')

        print(f'\nLopullinen rahatilanne: {self.raha}€')
        print(f'Kiitos pelaamisesta {self.nimi}!')