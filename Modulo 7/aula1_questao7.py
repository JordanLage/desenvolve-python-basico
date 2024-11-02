import random

def encrypt(nomes):
    chave = random.randint(1, 10)
    nomes_criptografados = []

    for nome in nomes:
        nome_criptografado = ""
        for c in nome:
            novo_caractere = chr(((ord(c) - 33 + chave) % (126 - 33 + 1)) + 33)
            nome_criptografado += novo_caractere
        nomes_criptografados.append(nome_criptografado)

    return nomes_criptografados, chave

nomes = ["Luana", "Ju", "Davi", "Vivi", "Pri", "Luiz"]
nomes_cript, chave_aleatoria = encrypt(nomes)

print(f'Chave Aleatória: {chave_aleatoria}')
print(f'Nomes Criptografados: {nomes_cript}')
