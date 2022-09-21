import sqlite3
def banco():
    conn = sqlite3.connect('prova1.db')
    cursor = conn.cursor()

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS Patient(
        PatientID INTEGER NOT NULL NULL PRIMARY KEY AUTOINCREMENT,
        Name TEXT NOT NULL,
        LastName TEXT NOT NULL
    )
    """)

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS Vaccine(
        VaccineID INTEGER NOT NULL NULL PRIMARY KEY AUTOINCREMENT,
        PatientID INTEGER NOT NULL,
        VaccineName TEXT NOT NULL,
        DoseDate DATETIME NOT NULL,
        DoseNumber INTEGER NOT NULL,
        VaccineType TEXT NOT NULL,
        FOREIGN KEY (PatientID) references Patient
    )
    """)

    conn.commit()
    conn.close()