nums = [3, 41, 12, 9, 74, 3, 15]

print(len(nums)) # len para ver o tamanho da lista

print(max(nums)) # max para ver o maior valor da lista

print(min(nums)) # min para ver o menor valor da lista

print(sum(nums)) # sum para somar os valores da lista

print(sum(nums) / len(nums)) # sum para somar, len para pegar o tamanho
                             # e podemos fazer operações com esses valores

print(nums.index(74)) # index para ver a posição do valor na lista 

print(nums.count(3)) # count para contar quantas vezes o valor aparece na lista 

nums.sort() # sort serve para ordenar os valores do menor pro maior na lista 

nums.remove(3) # remove apenas para remover a primeira aparição do elemento na lista
nums.pop(3) # remove pelo indice 