#todos os pares de 20 a 50
lista = [i for i in range(20,52,2)]
print(lista)


# Todos os quadrados da lista
lista = [1,2,3,4,5,6,7,8,9]
quadrado = [n**2 for n in lista]
print(quadrado)

# Numeros divisíveis por 7
lista = [n for n in range(1,100) if n % 7 ==0]
print(lista)

# Par ou impar
lista = ['par' if i % 2 == 0 else 'impar' for i in range(0,30,3)]
print(lista)