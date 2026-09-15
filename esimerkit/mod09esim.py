

k1_rotu = 'Mastiffi'
k1_nimi = 'wuffe'
k1_syntymävuosi = 2022

k2_rotu = 'bokseri'
k2_nimi = 'lissu'
k3_syntymävuosi = 2025

k2_rotu = 'lapinkoira'
k2_nimi = 'Inna'
k3_syntymävuosi = 2020

class Koira:
    pass

# Luokka on kuin suunnitelma. Olio on sen perusteella rakennettu yksilö.

koira = Koira()
koira2 = Koira()

koira.nimi = 'wuffe'
koira.rotu = 'mastiffi'

koira2.nimi = 'Inna'
koira2.rotu = 'Lapinkoira'

print(f'Esnimmäisen koiran nimi: {koira.nimi}')
print(f'Esnimmäisen koiran rotu: {koira.rotu}')

print(f'Toisen koiran nimi: {koira2.nimi}')
print(f'Toisen koiran rotu: {koira2.rotu}')

# Teimme juuri luokan 'Koira' ilman ominaisuuksia 
# Tämän jälkeen määrittelimme ominaisuudet yksi kerrallaan == työlästä!!

# Näin teemme oikeasti: 

# Koira:

# Koiran ominaisuudet:
# - nimi
# - Rotu
# - Syntymävuosi

# Koiran ominaisuudet
# - Hauku
# - Syö
# - Nuku
'''
players = [
    {
        "name": "Player 1",
        "skill_level": 10,
        "inventory": {"map", "knife"}
    },
    {
        "name": "Player 2",
        "skill_level": 20,
        "inventory": {"axe"}
    }
]

for player in players:
    #print(player)
    print(f"Pelaajan {player['name']} taitotaso on {player['skill_level']}, hallussa:")
    for item in player["inventory"]:
        print(f"- {item}")'''

### Miten tämä edellinen voitaisiin kuvata luokkana
### Esim. PELAAJA

print('-------------------------')

info = 'Pelaajan tiedot:'

class Player:
    def __init__(self, name, skill_level, inventory):
        self.name = name
        self.skill_level = skill_level
        self.inventory = inventory

    def show_info(self):
        print(info)
        print(f'Pelaajan nimi: {self.name}')
        print(f'pelaajan taitotaso: {self.skill_level}') 
        print('Reppu:')
        for item in self.inventory:
            print('>', item)
        print('-------------------------')

    def add_item(self, item):
        self.inventory.add(item)
        

player1 = Player('Tomi', 10, {'map', 'knife'})

player2 = Player('Artur', 20, {'axe'})

player1.show_info()
player2.show_info()

player1.add_item('key')

player1.show_info()
player2.show_info()

'''
print(f'palaajan 1 nimi on {player1.name} ja taso on {player1.skill_level}')

print(f'palaajan 1 nimi on {player2.name} ja taso on {player2.skill_level}')'''



