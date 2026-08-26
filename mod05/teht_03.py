'''
Kirjoita ohjelma, joka kysyy käyttäjältä lukuja siihen saakka, kunnes tämä 
syöttää tyhjän merkkijonon lopetusmerkiksi. Lopuksi ohjelma tulostaa 
saaduista luvuista pienimmän ja suurimman.
'''
lista = []
luku = input('Anna luku: ')

while True:
    luku = input('Anna luku: ')
    

    if luku == '':
        break
    lista.append(int(luku))

pienin = min(lista)
suurin = max(lista)

print(f'Pienin numero oli {pienin} ja suurin numero oli {suurin}.')
