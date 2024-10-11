# Entrada de dados
n = int(input('Insira o valor de n: '))

maior = 0 # Inicializa o maior com o menor valor possível

while n > 0:  # Continua enquanto n for maior que 0
    x = int(input())
    if x > maior:
        maior = x
    n -= 1  # Decrementa n independentemente do valor de x

print(maior)