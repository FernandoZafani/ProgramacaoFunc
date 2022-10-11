from funcoes import soma_nat,quadrados,quadrados_inv,indices_pares
from functools import reduce

if __name__ == '__main__':
    print(soma_nat(10))
    quadrados(5)
    quadrados_inv(5)
    indices_pares([4,3,7,1,2,9])

# Exercicio 6
    pessoas = [
        {'nome': 'Pedro', 'idade': 11},
        {'nome': 'Mariana', 'idade': 18},
        {'nome': 'Arthur', 'idade': 26},
        {'nome': 'Rebeca', 'idade': 6},
        {'nome': 'Raquel', 'idade': 34},
        {'nome': 'André', 'idade':22},
        {'nome': 'Tiago', 'idade': 19},
        {'nome': 'Gabriela', 'idade': 127}
    ]

    idadesfiltradas = filter(lambda p: p['idade']<30 and p['idade']> 18, pessoas)
    print(reduce(lambda i,p: i + p['idade'], idadesfiltradas, 0))
