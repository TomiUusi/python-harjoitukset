# Mod 13 - Tiedostonkäsittelyä
'''
# Datan lukeminen
with open('mod13/intro_teksti.txt', 'r') as intro_file:
    intro = intro_file.read()
    print(intro)


# Datan tallentaminen
with open('mod13/data.txt', 'a') as data_tiedosto:
    data_tiedosto.write('Wassa Wassa\n')

# Datan lukeminen rivi kerrallaan
with open('mod13/data.txt', 'r') as mun_data_tiedosto:
    mun_data = mun_data_tiedosto.readline()
    print('Tiedosto data:', mun_data)
    mun_data = mun_data_tiedosto.readline()
    mun_data = mun_data_tiedosto.readlines()
    print('Tiedosto data:', mun_data)

# Pelaajan tallennus (Suoraan matskusta)
'''
import json

pelaajan_tiedot = {
    "pelaaja": "Matti",
    "taso": 5,
    "varusteet": ["miekka", "kilpi", "haarniska"]
}

with open("mod13/save.json", "w") as tiedosto:
    json.dump(pelaajan_tiedot, tiedosto)

with open("mod13/save.json", "r") as tiedosto:
    data_luettu = json.load(tiedosto)
print(f"Pelaaja: {data_luettu['pelaaja']}, taso: {data_luettu['taso']}, varusteet: {data_luettu['varusteet']}")