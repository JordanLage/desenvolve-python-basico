frase = input('Digite uma frase: ')
palavra_objetivo = input('Digite a palavra objetivo: ')

palavra_objetivo = palavra_objetivo.lower()
anagramas = []

palavra_objetivo_ordenada = sorted(palavra_objetivo)

palavras = frase.split()

for palavra in palavras:
    palavra_normalizada = palavra.lower()
    
    if sorted(palavra_normalizada) == palavra_objetivo_ordenada:
        anagramas.append(palavra_normalizada)

print('Anagramas:', anagramas)
