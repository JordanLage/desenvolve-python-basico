import random

lista1 = []
lista2 = []

for i in range(20):
    rand_int1 = random.randint(0, 50)
    rand_int2 = random.randint(0, 50)

    lista1.append(rand_int1)
    lista2.append(rand_int2)

interseccao = sorted(set(lista1) & set(lista2))

print(f'Primeira lista: {lista1}')
print(f'Segunda lista: {lista2}')
print(f'Interseção ordenada: {interseccao}')

elementos_interseccao = []
contagem_lista1 = []
contagem_lista2 = []

for elemento in interseccao:
    elementos_interseccao.append(elemento)
    contagem_lista1.append(lista1.count(elemento))
    contagem_lista2.append(lista2.count(elemento))

print('Contagem:')
for i in range(len(elementos_interseccao)):
    print(f'{elementos_interseccao[i]}: (lista1={contagem_lista1[i]}, lista2={contagem_lista2[i]})')
