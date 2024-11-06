while True:
    frase_original = input('Digite uma frase (digite (fim) para encerrar): ')
   
    if frase_original == 'fim':
        break

    frase = frase_original.replace(' ', '').replace('!', '').replace('.', '').replace('?', '').lower()

    if frase[::-1] == frase:
        print(f'"{frase_original}" É palindromo')
    else:
        print(f'"{frase_original}" Não é palindromo')
    
