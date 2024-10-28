frase = input("Digite uma frase: ")

vogais = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']

lista_vogais = []
lista_consoantes = []

for letra in frase:
    if letra in vogais:
        lista_vogais.append(letra)
    else:  
        lista_consoantes.append(letra)

lista_vogais.sort()
print("Vogais:", lista_vogais)
print("Consoantes:", lista_consoantes)
