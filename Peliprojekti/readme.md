# Puhelin mäsänä

**Tomi Uusitalo**

## Pelin idea

Tekstipohjainen Python peli, jossa pelaajan puhelin on mennyt rikki. Pelaajalla on 2000€ rahaa. Pelaajan tulee valita kahdesta eri kaupasta. Toinen on uunituoreita huippu puhelimia myyvä kauppa, ja toinen taas käytettyjä puhelimia myyvä kauppa. Pelaajan valinnoilla on merkitystä ympäristönpisteisiin. Pelissä on neljä erilaista loppua omista valinnoista riippuen.

## Toiminallisuudet

- Nimen ja iän kysyminen sekä ikätarkistus (k-12)
- alkuteksti tiedostona `intro.txt`
- Päävalikko, joka näyttää pelaajan sijainnin, rahat ja ympäristö pisteet
- Puhelimien katsominen hintoineen ja ympäristö pisteineen
- liikkuminen kauppojen välillä
- Neljä erilaista loppua

## Kestävän kehityksen teema

Pelissä otettu huomiion kestävän kehityksen tavoite 12. "Vastuullista kuluttamista". Pelissä käy ilmi, että ostamalla uusia puhelimia ympäristö pisteet laskevat ja ostamalla käytettyjä puhelimia pisteet nousevat.

## 


## pelinrakenne

```
├── Peliprojekti
│   ├── intro.txt
│   ├── main.py
│   ├── peli
│   │   ├── __init__.py
│   │   ├── __pycache__
│   │   │   ├── __init__
│   │   │   ├── esine
│   │   │   ├── huone
│   │   │   └── pelaaja
│   │   ├── esine.py
│   │   ├── huone.py
│   │   └── pelaaja.py
│   └── readme.md
```

