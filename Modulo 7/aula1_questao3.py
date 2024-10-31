frase = input('Digite a frase: ')

espaco_em_branco = 0

for i in frase:
    if " " in i:
        espaco_em_branco += 1
        
print(f'Espaço em branco: {espaco_em_branco}')