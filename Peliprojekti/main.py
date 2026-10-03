from peli import Esine, Huone, Pelaaja
import json

Kännykatu = Huone('Kännykatu 22')
kauppa1 = Huone('Uunituore Luuri (Kauppa)')
kauppa2 = Huone('Toisen käden Luuri (Kauppa)')


Uusi_puhelin1 = Esine('MePhone 23 Ultra Pro Max Plus', 1999, -20)
Uusi_puhelin2 = Esine('Mansung Super Fold 67', 1599, -20)
käytetty_puhelin1 = Esine('Mogia 3310', 199, 25)
käytetty_puhelin2 = Esine('Rotomola 2', 99, 25)


kauppa1.lisää_esine(Uusi_puhelin1)
kauppa1.lisää_esine(Uusi_puhelin2)
kauppa2.lisää_esine(käytetty_puhelin1)
kauppa2.lisää_esine(käytetty_puhelin2)


with open('peliprojekti/ohjeet.txt','r') as tiedosto:
    data = tiedosto.read()
    print(data)
    print('')

name = input('Kerro nimesi: ')
ikä = int(input('kerro ikäsi: '))

with open('peliprojekti/intro.txt','r') as tiedosto:
    data = tiedosto.read()
    print(data)
    print('')

if ikä < 0:
    print('Et ole edes vielä syntynyt!')
    exit()
elif ikä < 12:
    print('Olet liian nuori pelaamaan peliä.')
    exit()
else:
    print(f'tervetuloa pelaamaan peliä {name}, ikäsi on {ikä}.')


pelaaja = Pelaaja(name, Kännykatu)


# Pääsilmukka
peli_käynissä = True


while peli_käynissä:
    print('\n=======PÄÄVALIKKO=======')
    print(f'\nSijainti: {pelaaja.sijainti.nimi}')
    print(f'Rahaa: {pelaaja.raha}€')
    print(f'Ympäristöpisteet: {pelaaja.ympäristö_pisteet}')
    print('')
    print('1. Näytä kaupan tuotteet')
    print('2. Osta Tuote')
    print('3. Näytä inventaario')
    print('4. Liiku')
    print('5. Lähde kotiin (päätä peli)')
    print('6. Lopeta peli')
    print('------------------------')

    valinta = input('Anna komento: ')

    if valinta == '1':
        pelaaja.sijainti.näytä_kaupan_tuotteet()

    elif valinta == '2':
        pelaaja.osta_tuote()

    elif valinta == '3':
        pelaaja.näytä_inventaario()

    elif valinta == '4':
        print(f'\nMissä kaupassa tahdot asioida?')
        print('\n1. Uunituore Luuri (Kauppa)')
        print('2. Toisen Käden Luuri (Kauppa)')
        print('')

        kohde = input('Valitse huone: ')

        if kohde == '1':
            pelaaja.liiku(kauppa1)

        elif kohde == '2':
            pelaaja.liiku(kauppa2)

        else:
            print('Virheellinen valinta.')

    elif valinta == '5':
        pelaaja.loppu()
        peli_käynissä = False

    elif valinta == '6':
        print('Lopetetaan peli.')
        peli_käynissä = False

    else:
        print('Virheellinen valinta.')
