from functools import reduce

pessoas = [
    {'nome': 'Pedro', 'idade' : 11},
    {'nome' : 'Mariana', 'idade' : 18},
    {'nome' : 'Arthur', 'idade' : 26},
    {'nome' : 'Rebeca', 'idade' : 6},
    {'nome' : 'Tiago', 'idade' : 19},
    {'nome' : 'Gabriela', 'idade' : 17}
]

menores=[]

for pessoa in pessoas:
    if pessoa["idade"] < 18:
        menores.append(pessoa)

print(menores)

##

menores_idade = filter(lambda p: p['idade'] <18, pessoas)
print(list(menores_idade))

soma_idades = reduce(lambda idade,pessoa: idade + pessoa['idade'], pessoa, 0)