# Exercicio 2
def soma_nat(n):
    return n + (soma_nat(n-1) if(n-1) > 1 else 1)

# Exercicio 3
def quadrados(valor):
   lista = []
   for i in range(1,valor):
        lista.append(i**2)
   print(lista)

# Exercicio 4   
def quadrados_inv(valor):
    lista = []
    for i in range(1,valor):
        lista.append(i**2)
    print(lista[::-1])

# Exercicio 5
def indices_pares(lista):
    print(lista[::2])

