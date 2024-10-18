import random

numero_aleatorio = random.randint(1, 10)

while numero != numero_aleatorio:
        numero = int(input('Adivinhe o número: '))
        
        if numero < numero_aleatorio:
            print('Muito baixo')
        elif numero > numero_aleatorio:
            print('Muito alto')

print('Você acertou!!!')