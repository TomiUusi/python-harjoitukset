

name = input('Kerro nimesi: ')
ikä = int(input('kerro ikäsi: '))

if ikä < 0:
    print('Et ole edes vielä syntynyt!')
elif ikä < 12:
    print('Olet liian nuori pelaamaan peliä.')
else:
    print(f'tervetuloa pelaamaan peliä {name}, ikäsi on {ikä}.')

    input('Paina enter jatkaaksesi...')
    menu = input('Päävalikko: (pelaa/lopeta): ').lower()

    if menu == 'pelaa':
        print('peli alkaa')

    else:
        print('lopetit pelin')

# Usein while rakennetta käytetään ja varsinkin teidän projekteissa!!
# ns. pääsilmukka ELI main loop

Peli_käynissä = True
# main loop
print('Tervetuloa peliini!!')

while Peli_käynissä:
    print('Valitse minne mennään. (j tai l)')
    # j jatkaa peliä ja l lopettaa
    valinta = input('anna komento: ')
    if valinta == 'j':
        print('Jatketaan peliä')
    if valinta == 'l':
        print('lopetetaan peli')
        Peli_käynissä = False
