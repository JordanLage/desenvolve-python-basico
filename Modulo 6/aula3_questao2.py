lista_url = ["www.google.com&quot", "www.gmail.com&quot", "www.github.com&quot", "www.reddit.com&quot", "www.yahoo.com&quot"]

nomes = []

print(lista_url)

for link in lista_url:
    if 'www.' and '.com&quot' in lista_url:
        
        nomes.append(link)

print(nomes)    