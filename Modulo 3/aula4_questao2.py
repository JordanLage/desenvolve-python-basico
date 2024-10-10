# Entrada de dados
filme = str(input('Digite o nome do filme: '))
print(f"Filme: {filme}")
avaliacao = int(input('Digite e nota que quer dar para o filme: '))

if avaliacao == 5:
    print('Nota: Excelente!')
elif avaliacao == 4:
    print('Nota: Muito Bom!')
elif avaliacao == 3:
    print('Nota: Bom!')
elif avaliacao == 2:
    print('Nota: Relugar')
elif avaliacao == 1:
    print('Nota: Ruim')
else: 
    print('Insira uma nota de 1 a 5')