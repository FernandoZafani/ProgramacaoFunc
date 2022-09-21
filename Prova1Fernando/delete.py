import sqlite3
def delete() :
    conn = sqlite3.connect('prova1.db')
    cursor = conn.cursor()

    done=False

    while done == False :
        escolha=int(input("Deletar:\n[1] Paciente - [2] Vacina - [3] Encerrar função\nOpção: "))
        
        if escolha == 1 :
            patientID = int(input("ID do Paciente: "))
            cursor.execute('DELETE FROM Patient WHERE PatientID= ?', [(patientID)])
            conn.commit()

            choose=int(input("Finalizar função?\n[1]Sim - [2]Não\nOpção: "))
            if choose == 1 :
                done = True
        elif escolha == 2 :
            VaccineID = int(input("ID da Vacina: "))
            cursor.execute('DELETE FROM Vaccine WHERE VaccineID= ?', [(VaccineID)])
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