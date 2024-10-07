# 2) Dando continuidade à questão anterior
# um outro bar permite a entrada de grupos onde pelo menos uma pessoa é maior de idade (ficando responsável pelas outras).
# Ajuste sua resposta da questão anterior, ainda solicitando as idades de Juliana e Cris
# mas ajustando a expressão para esse novo cenário, imprimindo True se puderem entrar no bar, e False caso contrário.

# Solicita as idades de Juliana e Cris
idade_juliana = int(input("Digite a idade de Juliana: "))
idade_cris = int(input("Digite a idade de Cris: "))

# Verifica se ambos são maiores de 17 anos
podem_entrar = idade_juliana > 17 or idade_cris > 17

# Imprime o resultado
print("Podem entrar no bar?", podem_entrar)
