def processar(titulo,lista, funcao):
    print(f'Processando:{titulo}')
    for i in lista:
        print(i, '=>', funcao(i))

if __name__ == '__main__' :
   p = processar
   print('print maroto para testar')
   p('Dobros de 1 a 10', range(1,11),lambda x: x*2)

