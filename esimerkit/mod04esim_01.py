import random

# moduulin 4 tuntiesimerkkejä

# boolean

onko_totta = True
if onko_totta:
    print('Onhan se totta!')

## kolikon heitto simulaattori

kolikko = random.randint(0, 1)

# if lauseen ehto muodostuu AINA True tai False arvoksi
if kolikko == 0:
    result = 'kruuna'

if kolikko == 1:
    result = 'Klaava'

print(f'Heitit kolikkoa ja sait {result}n')

## Kolikonheittosimulaattori 2.0
# kolikko pystyyn tod.näk. oikeasti 1/6000
kolikko = random.random() # liukulukuarvo välilstä 0-1
print(kolikko)

# kolikko jää pystyyn tod.näk 1/100
if kolikko < 0.01:
    print('Kolikko jäi pystyyn!')
elif kolikko < 0.505:
    print('Kruuna')
else:
    print('klaava')



