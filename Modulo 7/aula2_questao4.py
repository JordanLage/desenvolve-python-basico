senha = input('Digite a senha: ')

def validador_senha(senha):
    if len(senha) < 8:
        return False

    tem_maiuscula = False
    tem_minuscula = False
    tem_numero = False
    tem_especial = False

    caracteres_especiais = "!@#$%^&*()-_=+[]{};:'\",.<>?/|\\`~"

    for char in senha:
        if char.isupper():
            tem_maiuscula = True
        elif char.islower():
            tem_minuscula = True
        elif char.isdigit():
            tem_numero = True
        elif char in caracteres_especiais:
            tem_especial = True

    return tem_maiuscula and tem_minuscula and tem_numero and tem_especial

print(validador_senha(senha))
