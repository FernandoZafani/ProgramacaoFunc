from faulthandler import cancel_dump_traceback_later
from sys import dont_write_bytecode


def multiplicar(x):
    def calcular(y):
        return y * x
    return calcular

if __name__ == "__main__" :
    dobro = multiplicar(2)
    triplo = multiplicar(3)
    print(dobro)
    print(triplo)
    print(f'O dobro de 3 é {dobro(3)}')
    print(f'O triplo de 7 é {triplo(7)}')