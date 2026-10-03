
nimi = input('Syötä nimi tai lopeta antamalla tyhjä merkkijono: ')
nimet = set()

while nimi != '':
    if nimi in nimet:
        print('Aiemmin syötetty nimi.')
    
    else:
        print('Uusi nimi')
        nimet.add(nimi)
    nimi = input('Syötä nimi tai lopeta antamalla tyhjä merkkijono: ')

for nimi in nimet:
    print(nimi)