nome = str(input('Insira um nome: '))
print(nome)

for letra in range(1, len(nome) + 1):
    print(nome[:letra])