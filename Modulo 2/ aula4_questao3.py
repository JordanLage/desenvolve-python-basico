# Variáveis 
produto1 = str(input('Digite o nome do produto 1: '))
preco_produto1 = float(input('Digite o preço unitário do produto 1: '))
qtd_produto1 = int(input('Digite a quantidade do produto 1: '))

produto2 = str(input('Digite o nome do produto 2: '))
preco_produto2 = float(input('Digite o preço unitário do produto 2: '))
qtd_produto2 = int(input('Digite a quantidade do produto 2: '))

produto3 = str(input('Digite o nome do produto 3: '))
preco_produto3 = float(input('Digite o preço unitário do produto 2: '))
qtd_produto3 = int(input('Digite a quantidade do produto 3: '))

# Calculo do valor total  
valor_total = (preco_produto1 * qtd_produto1) + (preco_produto2 * qtd_produto2) + (preco_produto3 * qtd_produto3)

# Saída do valor
print(f'Total: R${valor_total:3,.2f}')