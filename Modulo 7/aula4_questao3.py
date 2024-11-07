import re

with open('estomago.txt', 'r', encoding='utf-8') as arquivo:
    linhas = arquivo.readlines()

print("Texto das primeiras 25 linhas:")
for linha in linhas[:25]:
    print(linha.strip())

num_linhas = len(linhas)
print(f"\nNúmero de linhas do arquivo: {num_linhas}")

linha_mais_longa = max(linhas, key=len)
print(f"\nLinha com maior número de caracteres:\n{linha_mais_longa.strip()}")

nonato_count = sum(1 for linha in linhas if re.search(r'\bNonato\b', linha, re.IGNORECASE))
iria_count = sum(1 for linha in linhas if re.search(r'\bÍria\b', linha, re.IGNORECASE))
print(f"\nNúmero de menções aos personagens 'Nonato': {nonato_count}, 'Íria': {iria_count}")
