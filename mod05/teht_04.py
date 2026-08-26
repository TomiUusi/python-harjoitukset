'''
Kirjoita peli, jossa tietokone arpoo kokonaisluvun väliltä 1..10. 
Kone arvuuttelee lukua pelaajalta siihen asti, kunnes tämä arvaa oikein. 
Kunkin arvauksen jälkeen ohjelma tulostaa tekstin Liian suuri arvaus, 
Liian pieni arvaus tai Oikein. Huomaa, että tietokone ei saa vaihtaa lukuaan 
arvauskertojen välissä.
'''

import random

luku = random.randint (1, 10)
luku2 = int(input('Arvaa lukua 1-10 väliltä: '))

while luku != luku2:
    if luku2 < luku:
        print('Liian pieni arvaus.')
    elif luku2 > luku:
        print('Liian suuri arvaus')
    luku2 = int(input('Arvaa Uudestaan: '))

print('Aivan oikein!')
   