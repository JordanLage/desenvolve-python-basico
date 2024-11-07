import csv

# Dados dos livros
livros = [
    ["O Caçador de Pipas", "Khaled Hosseini", 2003, 368],
    ["Torto Arado", "Itamar Vieira Junior", 2019, 264],
    ["1984", "George Orwell", 1949, 328],
    ["Dom Quixote", "Miguel de Cervantes", 1605, 992],
    ["O Pequeno Príncipe", "Antoine de Saint-Exupéry", 1943, 96],
    ["Orgulho e Preconceito", "Jane Austen", 1813, 279],
    ["O Senhor dos Anéis", "J.R.R. Tolkien", 1954, 1216],
    ["Cem Anos de Solidão", "Gabriel García Márquez", 1967, 417],
    ["A Revolução dos Bichos", "George Orwell", 1945, 112],
    ["Moby Dick", "Herman Melville", 1851, 635]
]

# Cria e abre o arquivo CSV para escrita
with open("meus_livros.csv", "w", newline='', encoding='utf-8') as arquivo_csv:
    escritor_csv = csv.writer(arquivo_csv)

    # Escreve o cabeçalho
    escritor_csv.writerow(["Título", "Autor", "Ano de publicação", "Número de páginas"])

    # Escreve os dados dos livros
    escritor_csv.writerows(livros)

print("Arquivo 'meus_livros.csv' criado com sucesso!")
