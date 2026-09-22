

class Hissi:

    def __init__(self, nimi, alin_kerros, ylin_kerros):
        self.nykyinen_kerros = alin_kerros
        self.alin_kerros = alin_kerros
        self.ylin_kerros = ylin_kerros
        self.nimi = nimi

    def siirry_kerrokseen(self, kohdekerros):
        print(f'Siirrytään kerrokseen {kohdekerros}')
        print("")
        
        while self.nykyinen_kerros < kohdekerros:
            self.kerros_ylös()
        while self.nykyinen_kerros > kohdekerros:
            self.kerros_alas()

    def kerros_ylös(self):
        if self.nykyinen_kerros < self.ylin_kerros:
            self.nykyinen_kerros += 1
            print(f'Hissi {self.nimi} on nyt kerroksessa {self.nykyinen_kerros}')
        

    def kerros_alas(self):
        if self.nykyinen_kerros > self.alin_kerros:
            self.nykyinen_kerros -= 1
            print(f'{self.nimi} Hissi on nyt kerroksessa {self.nykyinen_kerros}')

class Talo:
    def __init__(self, alin_kerros, ylin_kerros, hissien_lkm):
        self.hissit = []
        for i in range(hissien_lkm):
            uusi_hissi = Hissi(f'numero {i+1}', alin_kerros, ylin_kerros)
            self.hissit.append(uusi_hissi)

    def aja_hissiä(self, numero, kohdekerros):
        # hissi nro 1 on listalla indeksissä 0
        print(f'Ajetaan hissiä {numero} kerrokseen {kohdekerros}')
        self.hissit[numero-1].siirry_kerrokseen(kohdekerros)

    def palohälytys(self):
        print('Palohälytys!!')
        # muuttuja h viittaa vuorollaan jokaiseen hissiiolioon listalla
        for h in self.hissit:
            h.siirry_kerrokseen(h.alin_kerros)
        


talo1 = Talo(2, 12, 3)

talo1.aja_hissiä(1, 5)
talo1.aja_hissiä(1, 7)
talo1.aja_hissiä(3, 2)
talo1.aja_hissiä(3, 8)

talo1.palohälytys()





    
# Testejä pellkällä hissi luokalla
'''
hissi1 = Hissi('Pääaula 1', 1, 12)
hissi2 = Hissi('Henkilökunta', 5, 20)

print(hissi1.nykyinen_kerros)
print(hissi2.nykyinen_kerros)

hissi1.siirry_kerrokseen(8)
hissi1.siirry_kerrokseen(5)
hissi2.siirry_kerrokseen(15)
hissi1.siirry_kerrokseen(9)
hissi2.siirry_kerrokseen(5)
hissi1.siirry_kerrokseen(1)
'''
