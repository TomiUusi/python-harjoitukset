# Yksi leiviskä on 20 naulaa
# yksi naula on 32 luotia
# Yksi luoti on 13,3g

luoti = 0.0133
naula = 32*luoti
leiviskä = 20*naula

leiviskä2 = float(input('anna leviskät: '))
naula2 = float(input('anna naulat: '))
luoti2 = float(input('anna luodit: '))

leiviskä3 = leiviskä*leiviskä2
naula3 = naula*naula2
luoti3 = luoti*luoti2

tarkka = leiviskä3 + naula3 + luoti3
tulos = int(leiviskä3 + naula3 + luoti3)
grammat = tarkka - tulos

print('Massa nykymittojen mukaan: ')
print(f'{tulos} kilogrammaa {round(grammat * 1000, 2)} grammaa.')

