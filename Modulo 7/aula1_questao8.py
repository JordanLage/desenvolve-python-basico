# Solicita o CPF ao usuário
cpf_input = input("Digite um CPF (formato XXX.XXX.XXX-XX): ")

cpf = cpf_input.replace(".", "").replace("-", "")

if len(cpf) != 11:
    print("Inválido")
else:
    soma1 = 0
    for i in range(9):
        soma1 += int(cpf[i]) * (10 - i)
    primeiro_digito = (soma1 * 10) % 11
    if primeiro_digito == 10:
        primeiro_digito = 0

    soma2 = 0
    for i in range(10):
        soma2 += int(cpf[i]) * (11 - i)
    segundo_digito = (soma2 * 10) % 11
    if segundo_digito == 10:
        segundo_digito = 0

    if primeiro_digito == int(cpf[9]) and segundo_digito == int(cpf[10]):
        print("Válido")
    else:
        print("Inválido")
