import string

# Tipo
a = 2
print(type(a))
a = 2.0
print(type(a))
a = False
print(type(a))
a = "Cria"
print(type(a))
print("--")

# Operações

print(2+3)
print(4-7)
print(2*5.3)
print(9.4/3)
print(10%3)
print(2**8)
print(10//3)
print(81**(1/2))

# String

dir(str)

print("--")
nome = "Zafs Cria"
print(nome[0]) #Letra "z"
print(nome[3]) #Letra "s"
print(nome[-3]) #Letra "r"

print("--")
print("zafs" == 'zafs') # indiferença entre ' e "
print("--")

texto = 'Texto entre apostrófos pode ter "aspas"'

doc = """texto com multiplas
linhas..."""
print(doc)
print("--")
nome = "um nome qualquer"
print(nome[4:])
print(nome[-5:])
print(nome[:4]) #o ultimo elemento nunca esta contido!(o primeiro sempre esta contido)
print(nome[1:5]) #o ultimo elemento nunca esta contido!(o primeiro sempre esta contido)
print("--")

numeros = "1234567890"

print(numeros[::])
print(numeros[::2])
print(numeros[::3])
print(numeros[::-2])
print(numeros[3::2])
