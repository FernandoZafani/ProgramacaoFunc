def fatorial_imp(n):
    resultado = 1
    for i in range(1,n+1):
        resultado = resultado * i
    return resultado

def fatorial(n):
    return n * (fatorial(n-1) if(n-1) > 1 else 1)

if __name__ == '__main__':
    print(fatorial_imp(5))
    print(fatorial(5))