numero = input('Digite o número: ')

if len(numero) == 8:
    numero = '9' + numero
if len(numero) == 9:
    numero_formatado = numero[0:5] + '-' + numero[5:]

print(f'Número completo: {numero_formatado}')