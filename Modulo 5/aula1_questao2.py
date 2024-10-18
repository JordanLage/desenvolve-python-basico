import random
import math

n = int(input('Digite quantos valores aleatórios deseja: '))
soma = 0
for i in range(n):
    soma += random.randint(0, 100)

raiz_quadrada = math.sqrt(soma)
print(f'A raiz quadrada dos números aleatórios é: {raiz_quadrada}')