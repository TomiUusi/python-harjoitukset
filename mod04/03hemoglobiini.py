#Naisen normaali hemoglobiiniarvo on välillä 117-175 g/l.
#Miehen normaali hemoglobiiniarvo on välillä 134-195 g/l.

suku = input('Oletko nainen (n) vai mies (m): ')

if suku == 'n':

    arvo = float(input('Mikä on hemoglobiiniarvosi: '))

    if 117 <= arvo <= 175:
        print('Hemoglobiiniarvosi on normaali')

    elif arvo < 117:
        print('Hemoglobiiniarvosi on liian matala. Naisen normaali hemoglobiiniarvo on välillä 117-175 g/l.')

    elif arvo > 175:
        print('Hemoglobiiniarvosi on liian korkea. Naisen normaali hemoglobiiniarvo on välillä 117-175 g/l.')


elif suku == 'm':

    arvo = float(input('Mikä on hemoglobiiniarvosi: '))

    if 134 <= arvo <= 195:
        print('Hemoglobiiniarvosi on normaali')

    elif arvo < 134:
        print('Hemoglobiiniarvosi on liian matala. Miehen normaali hemoglobiiniarvo on välillä 134-195 g/l.')
    elif arvo > 195:
        print('Hemoglobiiniarvosi on liian korkea. Miehen normaali hemoglobiiniarvo on välillä 134-195 g/l.')

else:

    print('Syötä joko "n" tai "m"')
