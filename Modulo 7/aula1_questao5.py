frase = input('Digite uma frase: ')
qtd_vogais = 0
alfabeto = 'aeiouAEIOU'
indices = []
indice = 0 

for letra in frase:
    if letra in alfabeto:
        qtd_vogais += 1
        indices.append(indice) 
    indice += 1 

print(f'{qtd_vogais} Vogais')
print(indices)
