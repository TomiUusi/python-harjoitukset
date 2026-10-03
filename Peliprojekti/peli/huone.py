class Huone:
    def __init__(self, nimi):
        self.nimi = nimi
        self.esineet = []

    def lisää_esine(self, esine):
        self.esineet.append(esine)

    def näytä_kaupan_tuotteet(self):
        print('Huoneessa olevat esineet:')
        print()
        for esine in self.esineet:
            print(f'> {esine.nimi} {esine.hinta}€')
            print(f'Ympäristö pisteet: {esine.ympäristö_pisteet}')        