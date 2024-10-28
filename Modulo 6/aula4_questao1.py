#todos os pares de 20 a 50
lista = []

for i in range(20, 52, 2):
    lista.append(i)
print(lista)

# Todos os quadrados da lista
lista = [1,2,3,4,5,6,7,8,9]

for num in lista:
    num_ao_quad = num ** 2
    print(num_ao_quad)

# Numeros divisíveis por 7
lista = []

for numero in range(1,100):
    if numero % 7 == 0:
        lista.append(numero)
print(lista)

# Par ou impar
lista = []

for i in range(0,30,3):
    if i % 2 == 0:
        lista.append(f'{i} par')
    else:
        lista.append(f'{i} impar')
print(lista)