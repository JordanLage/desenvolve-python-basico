data = input('Digite a data de nascimento(dd/mm/aaaa): ') 
meses = ['janeiro', 'fevereiro', 'março', 'abril', 'maio', 'junho', 'julho', 'agosto', 'setembro', 'outubro', 'novembro', 'dezembro']

data.split('/') # ['25', '04', '2005']

mes = int(data[3:5])
mes = meses[mes -1].capitalize()
ano = data[6:]

resultado = print(f'Você nasceu em {data[0:2]} de {mes} de {ano}')