# Entrada de dados
n = int(input('Insira o valor de n: '))

maior = 0 # Inicializa o maior com o menor valor possível

while n > 0:
    x = int(input())
    if x > maior:
        maior = x
    else:
        n = n - 1 

print(maior)