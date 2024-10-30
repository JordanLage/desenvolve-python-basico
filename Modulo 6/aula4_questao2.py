frase = input("Digite uma frase: ")

vogais = sorted([letra for letra in frase if letra in 'aeiouAEIOU'])

consoantes = [letra for letra in frase if letra.isalpha() and letra.lower() not in 'aeiou']

# Exibir resultados
print("Vogais:", vogais)
print("Consoantes:", consoantes)
