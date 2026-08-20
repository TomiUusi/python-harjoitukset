

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
