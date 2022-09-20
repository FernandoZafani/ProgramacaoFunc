import sqlite3

conn = sqlite3.connect('prova1.db')
cursor = conn.cursor()

escolha=int(input("Deletar:\n[1] Paciente - [2] Vacina\nOpção: "))
##delete
if escolha ==1 :
    PatientID = int(input("ID do Paciente: "))
    cursor.execute('DELETE FROM Patient WHERE PatientID= ?'(PatientID))
else :
    VaccineID = int(input("ID da Vacina: "))
    cursor.execute('DELETE FROM Vaccine WHERE VaccineID= ?'(VaccineID))

print("Deletado das tabelas! :)")

conn.commit()
conn.close()