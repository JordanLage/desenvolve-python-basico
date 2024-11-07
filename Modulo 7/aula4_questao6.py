import csv

# Abre o arquivo para leitura
with open('spotify-2023.csv', 'r', encoding='latin-1') as arquivo_csv:
    leitor_csv = csv.reader(arquivo_csv)
    
    cabecalho = next(leitor_csv)
    
    musicas_mais_tocadas = {}

    for linha in leitor_csv:
        try:
            nome_musica = linha[0].strip()
            nome_artistas = linha[1].strip()
            quantidade_artistas = int(linha[2].strip())
            ano_lancamento = int(linha[3].strip())
            reproducoes = int(linha[8].strip())
            
            if quantidade_artistas > 1 or '"' in nome_musica or '"' in nome_artistas:
                continue
            
            if 2012 <= ano_lancamento <= 2022:
                if (ano_lancamento not in musicas_mais_tocadas) or (reproducoes > musicas_mais_tocadas[ano_lancamento][3]):
                    musicas_mais_tocadas[ano_lancamento] = [nome_musica, nome_artistas, ano_lancamento, reproducoes]

        except (ValueError, IndexError):
            continue

lista_musicas = [musicas_mais_tocadas[ano] for ano in sorted(musicas_mais_tocadas)]

# Imprime a lista final
print(lista_musicas)
