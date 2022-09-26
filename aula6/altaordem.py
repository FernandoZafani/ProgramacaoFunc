#se fosse de uma pasta seria "from (nome pasta).primeiraclasse import dobro, quadrado"
from primeiraclasse import dobro, quadrado

def processar(titulo,lista, funcao):
    print(f'Processando:{titulo}')
    for i in lista:
        print(i, '=>', funcao(i))

if __name__ == '__main__' :
   p = processar
   p('Dobros de 1 a 10', range(1,11),dobro)
   p('Quadrados de 1 a 10', range(1,11),quadrado)