# Verificar se um número é impar ou par
n1 = int(input('Digite o número: '))

if n1 % 2 == 0:
    print('É par')
else: 
    print('É impar') 

# Tudo em uma linha 
n1, n2 = int(input('Primeiro número: ')), int(input('Segundo número: '))
print('É par' if (n1 + n2) % 2 == 0 else 'É impar')