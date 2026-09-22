
def parilliset_luvut(kokonaisluku_lista):
    karsittu = []
    for i in kokonaisluku_lista:
        if i % 2 == 0:
            karsittu.append(i)

    return karsittu

lista = [1, 4, 6, 7, 12, 11]

parilliset_lista = parilliset_luvut(lista)

print(f'Alkuperäinen lista: {lista}')

print(f'Karsittu lista: {parilliset_lista}')