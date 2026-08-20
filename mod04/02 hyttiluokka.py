#LUX on parvekkeellinen hytti yläkannella.
#A on ikkunallinen hytti autokannen yläpuolella.
#B on ikkunaton hytti autokannen yläpuolella.
#C on ikkunaton hytti autokannen alapuolella.

luokka = input('Anna hyttiluokkasi (A, B, C, LUX): ')

if luokka == 'A':
    print('A on ikkunallinen hytti autokannen yläpuolella.')

elif luokka == 'B':
    print('B on ikkunaton hytti autokannen yläpuolella.')

elif luokka == 'C':
    print('C on ikkunaton hytti autokannen alapuolella.')

elif luokka == 'LUX':
    print('LUX on parvekkeellinen hytti yläkannella.')

else:
    print('Virheellinen hyttiluokka.')