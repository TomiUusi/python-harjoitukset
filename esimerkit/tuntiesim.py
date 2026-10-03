class Koira:
    def __init__(self, nimi, rotu):
        self.nimi = nimi
        self.rotu = rotu

    def hauku(self):
        print(f'[{self.nimi}]: Vuh Vuh!')

class Kissa:
    def __init__(self, nimi, väri):
        self.nimi = nimi
        self.väri = väri

    def miau(self):
        print(f'[{self.nimi}]: Miau!')

class Ihminen:
    def __init__(self, nimi, kotimaa):
        self.nimi = nimi
        self.kotimaa = kotimaa

    def hauku(self):
        print(f'[{self.nimi}]: Oot tyhäm!')


koira1 = Koira('Inna', 'Lapinkoira')
kissa1 = Kissa('Savu', 'Harmaa')
ihminen1 = Ihminen('Tomi', 'Suomalainen')


koira1.hauku()
kissa1.miau()
ihminen1.hauku()
