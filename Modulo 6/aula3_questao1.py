list()
lista = []
for i in range(5):
    valor = int(input('Digite 5 valores: '))
    lista.append(valor)

print(f'Lista original: {lista}')
print(f'3 primeiros elementos: {lista[:-1]}') # início indefinido até o penultimo
print(f'2 últimos elementos:{lista[-2:]}') # início no antepenultimo até indefinido/fim
print(f'Lista invertida: {lista[::-1]}') # Início e fim indefinido com pulo de -1 
print(f'Elementos de índice par: {lista[0::2]}') # começa no 0 sem fim definido e vai pulando 2 
print(f'Elementos de índice ímpar{lista[1::2]}') # começa no segundo número e vai pulando 2 