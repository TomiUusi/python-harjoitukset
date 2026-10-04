import json
import os

TALLENNUSKANSIO = os.path.dirname(os.path.abspath(__file__))

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

    def _tallennuspolku(self):
        return TALLENNUSKANSIO / f'tallennus_{self.nimi.lower()}.json'

    def _tallennuspolku(self):
        return os.path.join(TALLENNUSKANSIO, f'tallennus_{self.nimi.lower()}.json')

    def tallenna_peli(self):
        data = {
            'nimi': self.nimi,
            'sijainti': self.sijainti.nimi,
            'raha': self.raha,
            'ympäristö_pisteet': self.ympäristö_pisteet,
            'esineet': [esine.nimi for esine in self.esineet],
        }
        try:
            polku = self._tallennuspolku()
            os.makedirs(os.path.dirname(polku), exist_ok=True)
            with open(polku, 'w', encoding='utf-8') as file:
                json.dump(data, file, ensure_ascii=False, indent=2)
            print(f'Peli tallennettu: {polku}')
        except OSError as e:
            print(f'Tallennus epäonnistui: {e}')

    def lataa_peli(self, huoneet, kaikki_esineet):
        """huoneet ja kaikki_esineet ovat sanakirjoja: nimi -> olio."""
        try:
            with open(self._tallennuspolku(), 'r', encoding='utf-8') as file:
                data = json.load(file)
        except FileNotFoundError:
            print('Tallennusta ei löydy.')
            return
        except (OSError, json.JSONDecodeError) as e:
            print(f'Tiedoston käsittelyssä tapahtui virhe: {e}')
            return

        try:
            self.sijainti = huoneet[data['sijainti']]
            self.raha = data['raha']
            self.ympäristö_pisteet = data['ympäristö_pisteet']
            self.esineet = [kaikki_esineet[nimi] for nimi in data['esineet']]
        except KeyError as e:
            print(f'Tallennus on vioittunut, puuttuu: {e}')
            return

        print('Peli ladattu.')





