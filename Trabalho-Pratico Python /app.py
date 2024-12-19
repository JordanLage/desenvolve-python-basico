import csv

# Função para carregar clientes do arquivo CSV
def carregar_clientes():
    clientes = {}
    try:
        with open('clientes.csv', 'r') as file:
            reader = csv.DictReader(file)
            for row in reader:
                clientes[row['cpf']] = row
    except FileNotFoundError:
        pass
    return clientes

# Função para salvar clientes no arquivo CSV
def salvar_clientes(clientes):
    with open('clientes.csv', 'w', newline='') as file:
        fieldnames = ['cpf', 'nome']
        writer = csv.DictWriter(file, fieldnames=fieldnames)
        writer.writeheader()
        for cliente in clientes.values():
            writer.writerow(cliente)

# Função para adicionar um novo cliente
def adicionar_cliente(clientes, cpf, nome):
    if cpf in clientes:
        print("CPF já cadastrado!")
    else:
        clientes[cpf] = {'cpf': cpf, 'nome': nome}
        salvar_clientes(clientes)

# Função para listar todos os clientes
def listar_clientes(clientes):
    for cliente in clientes.values():
        print(cliente)

# Função para carregar produtos do arquivo CSV
def carregar_produtos():
    produtos = []
    try:
        with open('produtos.csv', 'r') as file:
            reader = csv.DictReader(file)
            for row in reader:
                produtos.append(row)
    except FileNotFoundError:
        pass
    return produtos

# Função para salvar produtos no arquivo CSV
def salvar_produtos(produtos):
    with open('produtos.csv', 'w', newline='') as file:
        fieldnames = ['id', 'nome', 'preco', 'quantidade']
        writer = csv.DictWriter(file, fieldnames=fieldnames)
        writer.writeheader()
        for produto in produtos:
            writer.writerow(produto)

# Função para adicionar um novo produto
def adicionar_produto(produtos, id, nome, preco, quantidade):
    for produto in produtos:
        if produto['id'] == id:
            print("ID do produto já existe!")
            return
    produtos.append({'id': id, 'nome': nome, 'preco': preco, 'quantidade': quantidade})
    salvar_produtos(produtos)

# Função para listar todos os produtos
def listar_produtos(produtos):
    for produto in produtos:
        print(produto)

# Função para atualizar um produto existente
def atualizar_produto(produtos, id, nome=None, preco=None, quantidade=None):
    for produto in produtos:
        if produto['id'] == id:
            if nome:
                produto['nome'] = nome
            if preco:
                produto['preco'] = preco
            if quantidade:
                produto['quantidade'] = quantidade
            salvar_produtos(produtos)
            return
    print("Produto não encontrado!")

# Função para remover um produto
def remover_produto(produtos, id):
    for produto in produtos:
        if produto['id'] == id:
            produtos.remove(produto)
            salvar_produtos(produtos)
            return
    print("Produto não encontrado!")

# Função para buscar um produto pelo ID ou nome
def buscar_produto(produtos, chave):
    for produto in produtos:
        if produto['id'] == chave or produto['nome'] == chave:
            print(produto)
            return
    print("Produto não encontrado!")

# Função para ordenar produtos por nome
def ordenar_produtos_por_nome(produtos):
    produtos_ordenados = sorted(produtos, key=lambda x: x['nome'])
    for produto in produtos_ordenados:
        print(produto)

# Função para ordenar produtos por preço
def ordenar_produtos_por_preco(produtos):
    produtos_ordenados = sorted(produtos, key=lambda x: float(x['preco']))
    for produto in produtos_ordenados:
        print(produto)

# Carregar dados 
clientes = carregar_clientes()
produtos = carregar_produtos()

# Loop do menu de opções
while True:
    print("\nMenu de Opções:")
    print("1 - Cadastrar cliente")
    print("2 - Listar clientes")
    print("3 - Adicionar produto")
    print("4 - Listar produtos")
    print("5 - Atualizar produto")
    print("6 - Remover produto")
    print("7 - Buscar produto")
    print("8 - Ordenar produtos por nome")
    print("9 - Ordenar produtos por preço")
    print("0 - Sair")

    acao = input("Escolha uma opção: ")

    if acao == "0":
        break
    elif acao == "1":
        cpf = input("CPF do cliente: ")
        nome = input("Nome do cliente: ")
        adicionar_cliente(clientes, cpf, nome)
    elif acao == "2":
        listar_clientes(clientes)
    elif acao == "3":
        id = input("ID do produto: ")
        nome = input("Nome do produto: ")
        preco = input("Preço do produto: ")
        quantidade = input("Quantidade do produto: ")
        adicionar_produto(produtos, id, nome, preco, quantidade)
    elif acao == "4":
        listar_produtos(produtos)
    elif acao == "5":
        id = input("ID do produto a atualizar: ")
        nome = input("Novo nome (ou enter para manter): ")
        preco = input("Novo preço (ou enter para manter): ")
        quantidade = input("Nova quantidade (ou enter para manter): ")
        atualizar_produto(produtos, id, nome if nome else None, preco if preco else None, quantidade if quantidade else None)
    elif acao == "6":
        id = input("ID do produto a remover: ")
        remover_produto(produtos, id)
    elif acao == "7":
        chave = input("Buscar produto por ID ou nome: ")
        buscar_produto(produtos, chave)
    elif acao == "8":
        ordenar_produtos_por_nome(produtos)
    elif acao == "9":
        ordenar_produtos_por_preco(produtos)
    else:
        print("Opção inválida!")
