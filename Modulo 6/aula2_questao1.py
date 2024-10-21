import random

lista = []

for i in range(20):
    numero_aleatorio = random.randint(-100, 100)
    lista.append(numero_aleatorio)

print('Lista ordenada: ', sorted(lista))
print(f'Lista original: {lista}')
print('Índice do valor máximo: ', lista.index(max(lista)))
print('Índice do valor mínimo: ', lista.index(min(lista)))