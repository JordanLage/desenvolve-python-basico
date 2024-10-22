import random

elementos = []

num_elementos = random.randint(5,20)

for i in range(num_elementos):
    num_aleatorios = random.randint(1,10)
    elementos.append(num_aleatorios)

soma = sum(elementos)

print(f'Lista de elementos: {elementos}')
print(f'Soma dos valores da lista: {soma}')
print(f'Média dos valores da lista: {sum(elementos) / len(elementos):.2f}')