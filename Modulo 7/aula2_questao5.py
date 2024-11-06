def embaralhar_palavras(frase):
    palavras = frase.split(' ') 
    palavras_embaralhadas = []  

    for palavra in palavras:
        palavra_embaralhada = palavra[::-1] 
        palavras_embaralhadas.append(palavra_embaralhada)  

    frase_embaralhada = ' '.join(palavras_embaralhadas)  
    print(frase_embaralhada)  

frase = "Python é uma linguagem de programação"
embaralhar_palavras(frase)
