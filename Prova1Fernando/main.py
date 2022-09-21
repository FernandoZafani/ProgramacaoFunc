from insert import insert
from delete import delete
from update import update
from banco import banco
from select import select

def main():
    banco()
    stop = False
    while stop == False :
        resultado = int(input("Escolha uma função:\n[1] Inserir dado\n[2] Deletar dado\n[3] Atualizar dado\n[4] Mostrar tabela\n[5]Encerrar programa\nOpção: "))
        if resultado == 1 :
            insert()
        elif resultado == 2 :
            delete()
        elif resultado == 3:
            update()
        elif resultado == 4:
            select()
        elif resultado == 5:
            stop = True

if __name__ == "__main__" :
    main()