'''
Muokkaa edellistä funktiota siten, että funktio saa parametrinaan nopan tahkojen 
yhteismäärän. Muokatun funktion avulla voit heitellä esimerkiksi 21-tahkoista roolipelinoppaa. 
Edellisestä tehtävästä poiketen nopan heittelyä jatketaan pääohjelmassa 
kunnes saadaan nopan maksimisilmäluku, joka kysytään käyttäjältä ohjelman suorituksen alussa.
'''

import random

def heita_noppaa(tahkot):
    return random.randint(1, tahkot)

tahkot_lk = int(input('Syötä tahkojen lukumäärä: '))

while True:
    silmaluku = heita_noppaa(tahkot_lk)
    print(silmaluku)

    if silmaluku == tahkot_lk:
        break