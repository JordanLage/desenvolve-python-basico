# 5) Solicite de um usuário seu gênero ("M" ou "F"), sua idade e seu tempo de serviço (em anos)
# E escreva uma expressão que imprima True se a pessoa já pode se aposentar, ou False caso contrário, de acordo com as seguintes regras:
# A: Para mulheres, ter mais de 60 anos. Para homens, 65.
# B: Ou ter trabalhado pelo menos 30 anos
# C: Ou ter 60 anos  e trabalhado pelo menos 25.

# Entrada de dados
genero = str(input('Digite seu genero (M ou F): '))
idade = int(input('Digite a sua idade: '))
tempo_servico = int(input('Digite o tempo de serviço: '))

# Processamento
cond_a = (genero == "m" and idade >= 65) or (genero == "f" and idade >= 60)
cond_b = tempo_servico > 30
cond_c = idade >= 60 and tempo_servico >= 30 

pode_aposentar = cond_a or cond_b or cond_c

# Saída
print(pode_aposentar)