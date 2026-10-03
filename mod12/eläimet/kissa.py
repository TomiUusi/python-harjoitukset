class Kissa:
    def __init__(self, nimi, väri):
        self.nimi = nimi
        self.väri = väri

    def miau(self):
        print(f'[{self.nimi}]: Miau!')