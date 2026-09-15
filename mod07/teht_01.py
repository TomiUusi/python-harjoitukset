'''
Kirjoita parametriton funktio, joka palauttaa paluuarvonaan satunnaisen nopan 
silmäluvun väliltä 1..6. Kirjoita pääohjelma, joka heittää noppaa niin kauan 
kunnes tulee kuutonen. Pääohjelma tulostaa kunkin heiton jälkeen saadun silmäluvun.
'''

import random

def heita_noppaa():
    return random.randint(1, 6)

while True:
    silmaluku = heita_noppaa()
    print(silmaluku)

    if silmaluku == 6:
        break