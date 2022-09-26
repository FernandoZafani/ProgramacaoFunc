lista_2 = [
    {'nome': 'João', 'idade': 31},
    {'nome': 'Maria', 'idade': 37},
    {'nome': 'José', 'idade': 26}
]

##

so_nomes = map(lambda p: p['nome'], lista_2)
print(list(so_nomes))

#ou

print(list(map(lambda p: p['nome'], lista_2)))

##

list_nomes = []
nome = ''
for i in lista_2:
    nome = i['nome']
    list_nomes.append(nome)

print(list_nomes)