import random

# Gerando a lista aleatória
lista = [random.randint(-10, 10) for _ in range(20)]
print("Original:", lista)

# Encontrando o intervalo com a maior quantidade de números negativos
max_negativos = 0
inicio_intervalo = 0
fim_intervalo = 0

for i in range(len(lista)):
    for j in range(i, len(lista)):
        sub_lista = lista[i:j+1]
        cont_negativos = sum(1 for x in sub_lista if x < 0)
        
        if cont_negativos > max_negativos:
            max_negativos = cont_negativos
            inicio_intervalo = i
            fim_intervalo = j

# Deletando o intervalo encontrado
del lista[inicio_intervalo:fim_intervalo + 1]
print("Editada:", lista)
