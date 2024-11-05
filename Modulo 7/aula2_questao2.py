frase = input('Digite a frase: ')
vogais = 'aeiouAEIOU'

frase_modificada = frase
for letra in vogais:
    frase_modificada = frase_modificada.replace(letra, '*')

print(f'Frase modificada: {frase_modificada}')
