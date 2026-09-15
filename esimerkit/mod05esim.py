'''
import random


suorita = True

while suorita:
    print('Tämä printtaantuu vaan kerran.')
    suorita = False

print('Suoritus loppui.')

luku = 1                # alkuarvo / kierrosmuuttuja

while luku <= 5:        # Ehto 
    print(luku)     
    luku += 1           # Muuttujan arvon muuttaminen

print('Jatketaan ohjelmaa.')

# Lasketaan luku 10 alaspäin

luku = int(input('Syötä luku: '))

while luku >= 1:
    print(luku)
    luku -= 1

print('Valmista tuli.')


# Käyttäjä lopettaa toiston

salasana = input('Anna salainen salasana, jotta pääset sisään. (python): ').strip()

while salasana != 'python':
    print('Väärä salasana')
    salasana = input('Yritä uudestaan. (python): ')

print('Tervetuloa!')

# While / else rakenne
# suoritus siirtyy else-haaraan, kun toisto ehto on epätosi
# sitä ei suoritita jos poistutaan break-lauseella
# else rakenne on harvemmin käytetty

komento = input('Anna komento (lopeta, APUA): ').strip().lower()

while komento != 'lopeta':
    if komento == 'apua':
        break
    print(f'annoit komennon: {komento}')
    komento = input('Anna uusi komento: ')
else:
    print('Annoit käskyn lopeta, joten näin tehdään.')

print('Ohjelma jatkuu.')


noppa1 = noppa2 = heitot = 0

while (noppa1 != 6 or noppa2 != 6):
    noppa1 = random.randint(1,6)
    noppa2 = random.randint(1,6)
    heitot = heitot + 1
print(f"Tarvittiin {heitot:d} heittoa.")

# sama nopanheitto uudestaan, nyt sisäkkäisellä toistorakenteella

eka = 1
while eka <= 5:
    toka = 1
    while toka <= 5:
        print(f"{eka} kertaa {toka} on {eka*toka:d}")
        toka = toka + 1
    eka = eka + 1
'''

import random

kierros = 0
heitot = 0


while kierros < 1000:
    noppa1 = noppa2 = 0

    while (noppa1 != 6 or noppa2 != 6):
        noppa1 = random.randint(1,6)
        noppa2 = random.randint(1,6)
        # print(noppa1, noppa2)
        heitot = heitot + 1
    kierros += 1

print(f'pelikertoja oli: {kierros}')
print(f"Tarvittiin {heitot:d} heittoa.")
print(f'Jokaisella kierroksella oli keskimäärin {heitot/kierros} heittoa.')
