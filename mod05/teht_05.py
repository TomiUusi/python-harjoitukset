'''
Kirjoita ohjelma, joka kysyy käyttäjältä käyttäjätunnuksen ja salasanan. 
Jos jompikumpi tai molemmat ovat väärin, tunnus ja salasana kysytään uudelleen. 
Tätä jatketaan kunnes kirjautumistiedot ovat oikein tai väärät tiedot on syötetty 
viisi kertaa. Edellisessä tapauksessa tulostetaan Tervetuloa ja jälkimmäisessä Pääsy 
evätty. (Oikea käyttäjätunnus on python ja salasana rules).
'''

käyttäjä = 'python'
salasana = 'rules'

kerrat = 0

while kerrat < 3:

    käyttäjä2 = input('Syötä käyttäjätunnus: ')
    salasana2 = input('Syötä salasana: ')

    if käyttäjä == käyttäjä2 and salasana == salasana2:
        print('Tervetuloa!')
        break

    kerrat += 1

else:
    print('Pääsy evätty.')





    

        





    


