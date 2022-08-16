import string

acertou = False
while(acertou == False):
    print("Quem é o maior gado da sala?")

    resp=input()
    if resp == 'Fefo' or resp == 'fefo':
        print('Correto')
        acertou = True
    else:
        print('Incorreto')