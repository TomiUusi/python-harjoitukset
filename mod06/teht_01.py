'''
Kirjoita ohjelma, joka kysyy käyttäjältä arpakuutioiden lukumäärän. 
Ohjelma heittää kerran kaikkia arpakuutioita ja tulostaa silmälukujen summan. 
Käytä for-toistorakennetta.
'''

import random

arpakuutio_lkm = int(input("Anna arpakuutioiden lukumäärä: "))

summa = 0

for x in range(arpakuutio_lkm):
    silmaluku = random.randint(1, 6)
    summa += silmaluku

print("Silmälukujen summa:", summa)


