# Entrada de dados
n1, n2, n3 = int(input()), int(input()), int(input())

# Media dos 3 números
m = (n1 + n2 + n3) / 3

# Processamentos dos dados
while True:
    if m >= 60:
        print("Aprovado!")
    elif m >= 40:
        print('Recuperação')
    else:
        print('Reprovado')
    break
print('Fim')  