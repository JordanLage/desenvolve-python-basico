# Entrada de dados
distancia = float(input('Insira a distância da entrega em km: '))
peso_pacote = float(input('Insira o peso do pacote em kg: '))

# Calcula o preço base do frete de acordo com a distância
if distancia <= 100:
    preco = 1.00 * peso_pacote
elif 101 <= distancia <= 300:
    preco = 1.50 * peso_pacote
else:
    preco = 2.00 * peso_pacote

# Acrescenta taxa adicional para pacotes com peso superior a 10 kg
if peso_pacote > 10:
    preco += 10

# Exibe o valor do frete
print(f'O valor do frete é: R${preco:.2f}')
