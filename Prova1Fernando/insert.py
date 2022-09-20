import sqlite3

conn = sqlite3.connect('prova1.db')
cursor = conn.cursor()

#input paciente
patname = input("-- Paciente --\n Digite o nome do paciente: ")
patlastname = input("Digite o ultimo nome do paciente: ")

#input vacina
vacpatid = int(input("-- Vacina --\n Digite o ID do Paciente: "))
vacname = input("Nome da vacina: ")
vacdosedate = input("Data dose vacina: ")
vacdosenum = int(input("Número da dose: "))
vactype = input("Tipo da vacina: ")

##insert

#insert paciente
cursor.execute('INSERT INTO Patient (Name, LastName) VALUES (?,?)', (patname,patlastname))
#insert vacina
cursor.execute('INSERT INTO Vaccine (PatientID, VaccineName, DoseDate, DoseNumber, VaccineType) VALUES (?,?,?,?,?)', (vacpatid, vacname,vacdosedate,vacdosenum,vactype))

print('Acrescentadas nas tabelas! :)')

conn.commit()
conn.close()