idade = int(input('Digite sua idade: '))
partidas_jogadas = int(input('Quantos jogos de tabuleiro você já jogou? '))
vitorias = int(input('Quantos jogos já venceu? '))

# Verificando se a idade está entre 16 e 18
pode_entrar_idade = 16 <= idade <= 18
# Verificando se já jogou pelo menos 3 jogos
pode_entrar_jogos = partidas_jogadas >= 3
# Verificando se venceu mais de 1 jogo
pode_entrar_vitorias = vitorias > 1

# Verifica se todas as condições são verdadeiras
pode_entrar = pode_entrar_idade and pode_entrar_jogos and pode_entrar_vitorias

print(pode_entrar)
