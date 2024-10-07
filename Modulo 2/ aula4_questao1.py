# Solicia ao usuário o comprimento, largura e preço do m2 
comprimento = int(input('Digite o comprimento do terreno: '))
largura = int(input('Digite a largura do terreno: '))
preco_m2 = float(input('Digite o preço do metro quadrado : '))

# Calculos da área em metro quadrado e preço total 
area_m2 = comprimento * largura 
preco_total = preco_m2 * area_m2

# Saída dos dados
print(f'O terreno possui {area_m2}m2 e custa R${preco_total:,.3f}')