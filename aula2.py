from difflib import restore


lista= []

len(lista)

lista.append(1)
lista.append(5)
print(lista)
print(len(lista))
print(lista[0])
print("--")

##

nova_lista = [1, 5, 'Ana', 'Bia', ['C#','Python','Node'], 3.14]
print(nova_lista)
print(nova_lista[3])
print(nova_lista[4])
print(nova_lista[4][1])
print(nova_lista[4][1][3])
print("--")

nova_lista.remove(5)
print(nova_lista)
del nova_lista[2]
print(nova_lista)
nova_lista.reverse()
print(nova_lista)
print("--")

lista = [1,5,"Raquel","Guilherme", 3.1415,"Guilherme"]

print(lista.index(5))
print(lista.index('Raquel'))
print(lista.index('Guilherme'))

print('Andre' in lista)
print('Raquel' in lista)

lista.append('Andre')
print(lista)
lista.insert(2, 'Ana')
print(lista)
lista.insert(2,['Metalica','Led','Ozy'])
print(lista)
print("--")

lista = ['Ana','Aline','Guilherme','Andre','Dani']
print(lista[1:3])
print(lista[1:-1])
print(lista[1:])

print("--")

tupla = ()
cores = ('verde','amarelo','azul','branco')
print(cores[0])
print(cores[-1])
print(cores[1:])

cores_list = list(cores)
print(cores)
print(cores_list)
print("--")

## Dicionario

pessoa = {}

pessoa = {'nome' : 'Andre', 'idade' : '35','altura' : 1.83, 'cursos': ['C#','Node','React','Python']}
print(pessoa)
print(pessoa['altura'])
print(pessoa['cursos'][2])
print(pessoa.keys())
print(pessoa.values())
print(pessoa.items())
items = list(pessoa.items())
print(items)
print(type(items))
print(items[3])
print(type(items[3]))
print(type(items[3][0]))
print(items[3][1])
print(items[3][1][3][:-1])
print(type(items[3][1][2][4]))


print("--")

##

lista_pessoas = [{'nome' : 'Andre', 'idade' : '35','altura' : 1.83},
                {'nome' : 'Ana', 'idade' : '22','altura' : 1.57},
                {'nome' : 'João', 'idade' : '39','altura' : 1.78},
                {'nome' : 'Bia', 'idade' : '27','altura' : 1.63}]

print(lista_pessoas[2]['idade'])

pessoa1 = {'nome' : 'Andre', 'idade' : '35','altura' : 1.83}
print(pessoa1)
pessoa1.update({'idade' : '34', 'genero' : "M"})
print(pessoa1)
print('--')

## if <3

a = int(input(' Digite o valor: '))
b = int(input(' Digite o valor: '))
c = int(input(' Digite o valor: '))
resultado=0
if a > b and a > c :
    resultado=a
elif b > c and b > a:
    resultado= b
else :
    resultado=c

print(resultado)
