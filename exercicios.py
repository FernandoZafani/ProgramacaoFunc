# exercicio 1



from pickle import FALSE, TRUE
from random import randint


print('ex 1')

a = "abcde"
print(a [::-1])

# exercicio 2
print('ex 2')

texto = 'Python é uma linguagem excelente'
print('py' in texto)
print('ing' in texto)
print('zzz' in texto)

#exercicio 3
print('ex 3')



#exercicio 4
print('ex 4')

x = int(input("x= "))
y = int(input("y= "))

print(f'{x}+{y}={x+y}')

#exercicio 5
print('ex 5')

idade = int(input('idade= '))
if idade<18:
    print("menor de idade")
elif 18<idade<65 :
    print("Adulto")
elif 66<idade<100 :
    print("Melhor Idade")
else :
    print("Centenário")

#exercicio 6
print('ex 6')

pipedo = "paralelepípedo"
print("paralelepípedo")
n=0

while n<14:
    print(f'{pipedo[n]},',end="")
    n += 1
print()

#exercicio 7
print('ex 7')

lista_nomes = ['Danieli','André','Marcelo','Ana Paula']
for nome in lista_nomes:
    print(nome)

#exercicio 8
print('ex 8')

aleatorio = randint(0,9)
acertou= FALSE
tentativa = -1
while acertou == FALSE :
    tentativa =int(input("insira um numero de 0 a 9: "))
    if tentativa==aleatorio:
        acertou=TRUE
        print(f"Numero Secreto {aleatorio} foi encontrado!")

#exercicio 9
print('ex 9')

n = int(input())
ultimo = n
penultimo = n
k = 0
fibo = [n, n]

count = 0
while count < (10-2):
    k = ultimo + penultimo
    penultimo = ultimo
    ultimo = k
    fibo.append(k)
    count += 1
print(fibo)