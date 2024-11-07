import random

def imprime_enforcado(erros, estagios_enforcado):
    print(estagios_enforcado[erros])

# Lê o arquivo de gabarito de palavras
with open('gabarito_forca.txt', 'r', encoding='utf-8') as f:
    palavras = f.read().splitlines()

with open('gabarito_enforcado.txt', 'r', encoding='utf-8') as f:
    estagios_enforcado = f.read().split("\n\n")  

palavra_secreta = random.choice(palavras).upper()
tentativas = 6 
acertos = ['_' for _ in palavra_secreta]
letras_erradas = []
erros = 0

print("Bem-vindo ao jogo da forca!")
print("A palavra secreta tem", len(palavra_secreta), "letras:", " ".join(acertos))

while erros < tentativas and "_" in acertos:
    letra = input("\nDigite uma letra: ").upper()

    if letra in palavra_secreta:
        for i, l in enumerate(palavra_secreta):
            if l == letra:
                acertos[i] = letra
    else:
        if letra not in letras_erradas:
            letras_erradas.append(letra)
            erros += 1
            imprime_enforcado(erros, estagios_enforcado)

    print("Palavra:", " ".join(acertos))
    print("Letras erradas:", ", ".join(letras_erradas))

if "_" not in acertos:
    print("\nParabéns! Você adivinhou a palavra:", palavra_secreta)
else:
    print("\nVocê perdeu! A palavra era:", palavra_secreta)
    imprime_enforcado(erros, estagios_enforcado)
