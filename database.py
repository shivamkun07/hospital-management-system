import sqlite3

class Database:

    def __init__(self):

        self.conn = sqlite3.connect("hospital.db")
        self.cursor = self.conn.cursor()

        self.create_tables()

    def create_tables(self):

        # Patients table
        self.cursor.execute("""
        CREATE TABLE IF NOT EXISTS patients (
            patient_id TEXT PRIMARY KEY,
            name TEXT,
            age INTEGER,
            gender TEXT,
            phone TEXT,
            blood_group TEXT
        )
        """)

        # Doctors table
        self.cursor.execute("""
        CREATE TABLE IF NOT EXISTS doctors (
            doctor_id TEXT PRIMARY KEY,
            name TEXT,
            specialization TEXT,
            fee REAL
        )
        """)

        # Appointments table
        self.cursor.execute("""
        CREATE TABLE IF NOT EXISTS appointments (
            appointment_id TEXT PRIMARY KEY,
            patient_id TEXT,
            doctor_id TEXT,
            date TEXT,
            slot TEXT,
            status TEXT
        )
        """)

        self.conn.commit()

    def commit(self):
        self.conn.commit()