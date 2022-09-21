import sqlite3
def select():

    conn = sqlite3.connect('prova1.db')
    cursor = conn.cursor()

    done=False

    while done == False :
        escolha=int(input("Mostrar:\n[1] Paciente - [2] Vacina - [3] Encerrar função\nOpção: "))
        
        if escolha == 1 :
            cursor.execute('SELECT * FROM Patient')
            linhas = cursor.fetchall()
            for linha in linhas:
                print(linha)
            conn.commit()

            choose=int(input("Finalizar função?\n[1]Sim - [2]Não\nOpção: "))
            if choose == 1 :
                done = True
        elif escolha == 2 :
            cursor.execute('SELECT * FROM Vaccine')
            linhas = cursor.fetchall()
            for linha in linhas:
                print(linha)
            conn.commit()

            choose=int(input("Finalizar função?\n[1]Sim - [2]Não\nOpção: "))
            if choose == 1 :
                done = True
        elif escolha == 3:
            print("Voltando para o menu.")
            done = True
        else :
            print("Opção Invalida! :(\n")


    conn.commit()
    conn.close()