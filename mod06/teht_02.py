'''
Kirjoita ohjelma, joka kysyy käyttäjältä lukuja siihen saakka, kunnes tämä syöttää 
tyhjän merkkijonon lopetusmerkiksi. Lopuksi ohjelma tulostaa saaduista luvuista 
viisi suurinta suuruusjärjestyksessä suurimmasta alkaen. Vihje: listan alkioiden 
lajittelujärjestyksen voi kääntää antamalla sort-metodille argumentiksi reverse=True.
'''

lista = []
luku = None

luku = input('Anna luku: ')

while True:
    luku = input('Anna luku: ')

    if luku == '':
        break

    lista.append(int(luku))

lista.sort(reverse=True)

print('Viisi suurinta lukua:')

for luku in lista[:5]:
    print(luku)
