
import random

numero = str(random.randint(0, 9))
numero6 = str(random.randint(0, 9))
numero7 = str(random.randint(0, 9))

print(f'Kolminumeroinen koodi: {numero + numero6 + numero7}')

numero2 = str(random.randint(1, 6))
numero3 = str(random.randint(1, 6))
numero4 = str(random.randint(1, 6))
numero5 = str(random.randint(1, 6))

print(f'Nelinumeroinen koodi: {numero2 + numero3 + numero4 + numero5}')

# toinen tapa
'''
print(f'Kolminumeroinen koodi: {random.randint(0,9), random.randint(0,9), random.randint(0,9)}')
print(f'Nelinumeroinen koodi: {random.randint(0,6), random.randint(0,6), random.randint(0,6), random.randint(0,6)}')
'''