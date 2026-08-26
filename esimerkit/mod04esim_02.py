'''
Kirjoita ohjelma, joka kysyy käyttäjältä sähkönkulutusta kilowattitunteina (kWh). 
Ohjelman tulee laskea sähkölasku kolmen eri porrastetun hinnan mukaan ja tulostaa loppusumma.

Ensimmäiset 50 kWh maksavat 10 senttiä/kWh.
Seuraavat 150 kWh maksavat 8 senttiä/kWh.
Yli 200 kWh menevä kulutus maksaa 6 senttiä/kWh.
'''

kulutus = float(input('\nSyötä sähkönkulutus (kWh): '))

hinta = 0

if kulutus <= 50:
    hinta = kulutus * 10
    hinta = hinta / 100
elif kulutus <= 200:
    hinta = 50 * 10
    hinta += (kulutus - 50) * 8
else:
    hinta = 50 * 10
    hinta += 150 * 8
    hinta += (kulutus -200) * 6

sentit = int(hinta % 100)
hinta = hinta / 100

print(f'Sähkön hinta: {hinta:.0f} euroa ja {sentit} senttiä.')




