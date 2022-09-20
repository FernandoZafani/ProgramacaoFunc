from re import T
import sqlite3

conn = sqlite3.connect('prova1.db')
cursor = conn.cursor()

done=False

while done == False :
    escolha=int(input("Atualizar dados de:\n[1] Paciente - [2] Vacina - [3] Encerrar Programa\nOpção: "))
    if escolha == 1 :
        #update paciente
        patientID = int(input("-- Paciente --\nDigite o ID do paciente que sera atualizado: "))
        patname = input("Digite o nome do paciente: ")
        patlastname = input("Digite o ultimo nome do paciente: ")

        cursor.execute('UPDATE Patient SET Name = ?, LastName = ? WHERE PatientID = ?', (patname,patlastname,patientID))
        print("Paciente atualizado! :)\n")

        choose=int(input("Finalizar programa?\n[1]Sim - [2]Não\nOpção: "))
        if choose == 1 :
            done = T

    elif escolha == 2 :
        #update vacina
        vaccineid = int(input("-- Vacina --\nDigite o ID da vacina que será atualizado: "))
        vacpatid = int(input("Digite o ID do Paciente: "))
        vacname = input("Nome da vacina: ")
        vacdosedate = input("Data dose vacina: ")
        vacdosenum = int(input("Número da dose: "))
        vactype = input("Tipo da vacina: ")

        cursor.execute('UPDATE Vaccine SET PatientID = ?, VaccineName = ?, DoseDate = ?, DoseNumber = ?, VaccineType = ? WHERE VaccineID = ?',(vacpatid,vacname,vacdosedate,vacdosedate,vacdosenum,vactype,vaccineid))
        conn.commit()
        
        print("Vacina atualizada! :)\n")

        choose=int(input("Finalizar programa?\n[1]Sim - [2]Não\nOpção: "))
        if choose == 1 :
            done = T
    elif escolha == 3 :
        done = T
    else :
        print("Opção Invalida! :(\n")

conn.commit()
conn.close()