'''
Kirjoita funktio, joka saa parametrinaan bensiinin määrän Yhdysvaltain nestegallonoina 
ja palauttaa paluuarvonaan vastaavan litramäärän. Kirjoita pääohjelma, 
joka kysyy gallonamäärän käyttäjältä ja muuntaa sen litroiksi. Muunnos on tehtävä 
aliohjelmaa hyödyntäen. Muuntamista jatketaan siihen saakka, kunnes käyttäjä syöttää 
negatiivisen gallonamäärän.
Yksi gallona on 3,785 litraa.
'''

def muunnos(galloonat):
    return galloonat * 3.785

while True:
    galloonat = float(input('Syötä Bensiinin määrä nestegalloonina: '))

    if galloonat < 0:
        break

    litrat = muunnos(galloonat)
    print(f'{litrat:.2f} litraa')
