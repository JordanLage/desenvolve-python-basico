lista1 = []
lista2 = []

qtd_item1 = int(input('Digite a quantidade de elementos da lista 1: '))

for i in range(qtd_item1):
    item = int(input(f'Digite os {qtd_item1} elementos da lista 1:'))
    lista1.append(item)

qtd_item2 = int(input('Digite a quantidade de elementos da lista 2: '))

for i in range(qtd_item2):
    item = int(input(f'Digite os {qtd_item2} elementos da lista 1:'))
    lista2.append(item)


lista_intercalada = []
min_len = min(qtd_item1, qtd_item2)

for i in range(min_len):
    lista_intercalada.append(lista1[i])
    lista_intercalada.append(lista2[i])

if qtd_item1 > qtd_item2:
    lista_intercalada.extend(lista1[min_len:])
else:
    lista_intercalada.extend(lista2[min_len:])

print(f'Lista intercalada: {lista_intercalada}')