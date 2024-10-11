# Bibliotecas utilizadas
import math

# Entrada de dados
a = int(input("Valor de a: "))
b = int(input("Valor de b: "))
c = int(input("Valor de c: "))

# Processamento de dados
delta = b**2 - 4 * a * c
print(f"Valor de delta: {delta:.2f}")

# Condição para caso delta seja maior que 0 e saída de dados
if delta > 0:
    x1 = (-b + math.sqrt(delta)) / (2 * a)  
    print(f'Valor de x1: {x1:.2f}')

    x2 = (-b - math.sqrt(delta)) / (2 * a)
    print(f"Valor de x2: {x2:.2f}")

elif delta == 0:
    x = -b / (2 * a)
    print(f'Valor de x: {x:.2f}')

else:
    print('Não há raízes reais')

# Utilizei a biblioteca math para poder calcular a raiz 