lista_url = ["www.google.com&quot", "www.gmail.com&quot", "www.github.com&quot", "www.reddit.com&quot", "www.yahoo.com&quot"]

dominios = []

print(lista_url)

for link in lista_url:
    nome = link[4:-9]
    dominios.append(nome)

print(dominios)    