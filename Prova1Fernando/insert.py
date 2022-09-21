import sqlite3
def insert():
    conn = sqlite3.connect('prova1.db')
    cursor = conn.cursor()

    done=False

    while done == False :
        escolha=int(input("Adicionar:\n[1] Paciente - [2] Vacina - [3] Encerrar função\nOpção: "))
        
        if escolha == 1 :
            patname = input("-- Paciente --\nDigite o nome do paciente: ")
            patlastname = input("Digite o ultimo nome do paciente: ")

            cursor.execute('INSERT INTO Patient (Name, LastName) VALUES (?,?)', (patname,patlastname))
            conn.commit()

            choose=int(input("Adicionar mais?\n[1]Sim - [2]Não\nOpção: "))
            if choose == 2 :
                done = True

        elif escolha == 2 :
            vacpatid = int(input("-- Vacina --\nDigite o ID do Paciente: "))
            vacname = input("Nome da vacina: ")
            vacdosedate = input("Data dose vacina: ")
            vacdosenum = int(input("Número da dose: "))
            vactype = input("Tipo da vacina: ")

            cursor.execute('INSERT INTO Vaccine (PatientID, VaccineName, DoseDate, DoseNumber, VaccineType) VALUES (?,?,?,?,?)', (vacpatid, vacname,vacdosedate,vacdosenum,vactype))
            conn.commit()

            choose=int(input("Adicionar mais?\n[1]Sim - [2]Não\nOpção: "))
            if choose == 2 :
                done = True

        elif escolha == 3:
            print("Voltando para o menu.")
            done = True

        else :
            print("Opção Invalida! :(\n")

    conn.commit()
    conn.close()