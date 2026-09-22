

name = input('Kerro nimesi: ')
ikä = int(input('kerro ikäsi: '))

if ikä < 0:
    print('Et ole edes vielä syntynyt!')
    exit()
elif ikä < 12:
    print('Olet liian nuori pelaamaan peliä.')
    exit()
else:
    print(f'tervetuloa pelaamaan peliä {name}, ikäsi on {ikä}.')

 
inventaario = []
hp = 100
energia = 100
kylläisyys = 100

def etsi_esine():
    esine = input('Minkä esineen löysit: ')
    inventaario.append(esine)
    print(f'löysit esineen {esine}.')

def näytä_inventaario():
    print('----INVENTAARIO----')
    for esine in inventaario:
        print(f'> {esine}')

def näytä_tilastot():
    print('----PELAAJAN TILASTOT----')
    print(f'HP: {hp}')
    print(f'Energia: {energia}')
    print(f'Kylläisyys: {kylläisyys}')




# Usein while rakennetta käytetään ja varsinkin teidän projekteissa!!
# ns. pääsilmukka ELI main loop

Peli_käynissä = True
# main loop
print('Tervetuloa peliini!!')

while Peli_käynissä:
    print('=======PÄÄVALIKKO=======')
    print('1. Etsi esine')
    print('2. Näytä inventaario')
    print('3. Näytä tilastot')
    print('4. lopeta peli')

    valinta = input('anna komento: ')

    if valinta == '1':
        etsi_esine()

    elif valinta == '2':
        näytä_inventaario()

    elif valinta == '3':
        näytä_tilastot()
        
    elif valinta == '4':
        print('lopetetaan peli')
        Peli_käynissä = False

    else:
        print('Virheellinen komento')
