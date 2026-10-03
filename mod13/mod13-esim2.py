# Virheiden käsittely
import json

class Player:
    def __init__(self, age):
        self.age = age
        self.points = 0

    def go_forward(self):
        print('Pelaaja etenee ja saa yhden pisteen.')
        self.points += 1
        print(f'Pisteitä kasassa: {self.points}')



    
    ## Peli tilanteen lataus ja tallennus

    def save_game(self):
        try:
            with open("mod13/save.txt", "w") as file:
                data = {"age": player.age, "points": player.points}
                json.dump(data, file)
        except FileNotFoundError:
            print("Tiedostoa ei löydy.")
        except IOError:
            print("Tiedoston käsittelyssä tapahtui virhe.")
    def load_game(self):
        try:
            with open("mod13/save.txt", "r") as file:
                data = json.load(file)
                print('Ladattu data:', data)
                self.points = data['age']
                self.age = data['age']

        except FileNotFoundError:
            print("Tiedostoa ei löydy.")
        except IOError:
            print("Tiedoston käsittelyssä tapahtui virhe.")

## Main loop

def start_game():
    game_running = True
    while game_running:
        command = input('Anna komento: ')
        if command == 'tallenna':
            player.save_game()
        elif command == 'Lataa':
            player.load_game()
        elif command == 'etene':
            player.go_forward()
        elif command == 'lopeta':
            game_running = False
        else:
            print('Virheellinen komento.')


print('Peli alkaa')
age = None
while age == None:
    try:
        age = int(input('Anna pelaajan ikä: '))
    except ValueError:
        print('Virhe: Syötetty arvo ei ole kokonaisluku.')

print(f'Pelaajan ikä on: {age}')

if age > 11:
    player = Player(age)
    start_game()
else:
    print('Pelaaja on liian nuori.')
    exit()



print('Suljetaan ohjelma.')


