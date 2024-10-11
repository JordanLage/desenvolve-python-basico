# Entrada de dados
x = int(input('Insira um número: '))

# Processamento com condicional 
while x > 5:
    print('Maior que 5')

    x = int(input('Insira um número: '))
print('Fim')


# Tambem funciona com Condicionais 

# Entrada de dados
x = int(input('Insira um número: '))

# Processamento com condicional 
while True:
    if x > 5:
        print('Maior que 5')
    else:
        print('Fim')
    break # Break para parar o loop