# Ler o número de respondentes
N = int(input("Digite a quantidade de respondentes: "))

# Inicializar variáveis
soma_idades = 0
contador = 0

# Usar um loop while para ler as idades
while contador < N:
    idade = int(input(f"Digite a idade do respondente {contador + 1}: "))
    soma_idades += idade  
    contador += 1  

# Calcular a média
media_idades = soma_idades / N

# Imprimir a média
print(f"A média das idades é: {media_idades}")
