from sqlite3 import Cursor
import pyodbc
import sqlite3

server='dlapoio.database.windows.net'
database='masterUber'
username='andre'
password='ShC12%Uz'
driver='SQL Server'

cnxn= pyodbc.connect('DRIVER='+driver+';SERVER='+server+';PORT=1443;DATABASE='+database+';UID='+username+';PWD='+password)

cursor = cnxn.cursor()

cursor.execute('SELECT * FROM tb_pessoas')

for linha in cursor.fetchall():
    print(linha)

conn = sqlite3.connect('espm4s.db')
cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS tb_pessoas(
    id INTEGER NOT NULL NULL PRIMARY KEY AUTOINCREMENT,
    nome TEXT NOT NULL,
    idade INT NOT NULL
)
""")

nome = input("Digite o nome: ")
idade = int(input("Digite a idade: "))

cursor.execute('INSERT INTO tb_pessoas (nome, idade) VALUES (?,?)', (nome,idade))

cursor.execute('UPDATE tb_pessoas SET nome = ? WHERE id=?', ('Fernando Zafani',1))

cursor.execute('DELETE FROM tb_pessoas WHERE id= 1')

print('update ok')

conn.commit()
conn.close()