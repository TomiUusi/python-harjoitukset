import math

kokonaisluku = 10
kokonaisluku_pitkä = 12_123_234_939
liukuluku = 4.123
kompleksiluku = -4 + 2j
totuusarvo = True

print(kompleksiluku)
print(kompleksiluku.real)
print(kompleksiluku.imag)


# printataan muuttujan tyyppi

print(f'muuttujan tyyppi voidaan tutkia {type(kompleksiluku)}')

print(f'{'vakio':6s}|{'arvo':>5s}')
print('-----------------')
print(f"{'Pii':6s}:{math.pi:10.7f}")

tuloste = '''
yhteenlasku (+), vähennyslasku (-), 
kertolasku (*) ja jakolasku (/). 
jakojäännösoperaatio (%), pelkän kokonaisosan palauttava jakolasku (//) 
potenssiinkorotus (**).
'''
print(tuloste)

# laskukone

luku = float(input('anna ensimmäinen luku: '))
luku2 = float(input('anna toinen luku: '))

yhteenasku = luku + luku2
vähennyslasku = luku - luku2
kertolasku = luku * luku2
potenssi = luku ** luku2
jakolasku = luku / luku2
kokonaisosa = luku // luku2
jakojäännös = luku % luku2

print(f'yhteenlaskun tulos on {yhteenasku}')
print(f'vähennyslasku on {vähennyslasku}')
print(f'kertolasku on {kertolasku}')
print(f'potenssiinkorotus on {potenssi}')
print(f'jakolasku on {jakolasku}')
print(f'kokonaisosa on {kokonaisosa}')
print(f'jakojäännös on {jakojäännös}')