classe = str(input('Digite a sua classe (Guerreiro, Mago ou Arqueiro): '))
forca = int(input('Digite os pontos de força (de 1 a 20): '))
magia = int(input('Digite os pontos de magia (de 1 a 20) '))

guerreiro = forca >= 10 and magia <= 10 
mago = forca <= 10 and magia >= 15 
arqueiro = forca >=5 and magia >= 5


print(f'Pontos de atributo consistentes com a classe escolhida: ')
