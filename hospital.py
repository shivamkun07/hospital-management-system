import sqlite3
from appointment import Appointment
from medicine import Medicine
from medical_record import MedicalRecord
from lab_report import LabReport
from bill import Bill


# =========================
# DATABASE LAYER
# =========================

class Database:

    def __init__(self):
        self.conn = sqlite3.connect("hospital.db")
        self.cursor = self.conn.cursor()
        self.create_tables()

    def create_tables(self):

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

        self.cursor.execute("""
        CREATE TABLE IF NOT EXISTS doctors (
            doctor_id TEXT PRIMARY KEY,
            name TEXT,
            specialization TEXT,
            fee REAL
        )
        """)

        self.cursor.execute("""
        CREATE TABLE IF NOT EXISTS nurses (
            nurse_id TEXT PRIMARY KEY,
            name TEXT,
            department TEXT,
            shift TEXT
        )
        """)

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

        self.cursor.execute("""
        CREATE TABLE IF NOT EXISTS medicines (
            medicine_id TEXT PRIMARY KEY,
            name TEXT,
            stock INTEGER,
            price REAL,
            expiry TEXT
        )
        """)

        self.cursor.execute("""
        CREATE TABLE IF NOT EXISTS medical_records (
            record_id TEXT PRIMARY KEY,
            patient_id TEXT,
            diagnosis TEXT,
            prescription TEXT,
            notes TEXT
        )
        """)

        self.cursor.execute("""
        CREATE TABLE IF NOT EXISTS lab_reports (
            report_id TEXT PRIMARY KEY,
            patient_id TEXT,
            test_name TEXT,
            result TEXT,
            date TEXT
        )
        """)

        self.cursor.execute("""
        CREATE TABLE IF NOT EXISTS bills (
            bill_id TEXT PRIMARY KEY,
            patient_id TEXT,
            consultation REAL,
            medicine REAL,
            lab REAL,
            total REAL
        )
        """)

        self.conn.commit()


# =========================
# DECORATOR
# =========================

def log_action(func):

    def wrapper(*args, **kwargs):
        print(f"\n[LOG] {func.__name__} running...")
        result = func(*args, **kwargs)
        print(f"[LOG] {func.__name__} done")
        return result

    return wrapper


# =========================
# HOSPITAL CORE SYSTEM
# =========================

class Hospital:

    def __init__(self):
        self.db = Database()

    # -------------------------
    # PATIENT
    # -------------------------

    @log_action
    def register_patient(self, patient):

        self.db.cursor.execute("""
        INSERT INTO patients VALUES (?, ?, ?, ?, ?, ?)
        """, (
            patient.patient_id,
            patient.name,
            patient.age,
            patient.gender,
            patient.phone,
            patient.blood_group
        ))

        self.db.conn.commit()
        print("Patient Added")

    def view_patients(self):

        self.db.cursor.execute("SELECT * FROM patients")
        rows = self.db.cursor.fetchall()

        for r in rows:
            print(r)

    # -------------------------
    # DOCTOR
    # -------------------------

    @log_action
    def add_doctor(self, doctor):

        self.db.cursor.execute("""
        INSERT INTO doctors VALUES (?, ?, ?, ?)
        """, (
            doctor.doctor_id,
            doctor.name,
            doctor.specialization,
            doctor.consultation_fee
        ))

        self.db.conn.commit()
        print("Doctor Added")

    def view_doctors(self):

        self.db.cursor.execute("SELECT * FROM doctors")
        rows = self.db.cursor.fetchall()

        for r in rows:
            print(r)

    # -------------------------
    # NURSE
    # -------------------------

    @log_action
    def add_nurse(self, nurse):

        self.db.cursor.execute("""
        INSERT INTO nurses VALUES (?, ?, ?, ?)
        """, (
            nurse.nurse_id,
            nurse.name,
            nurse.department,
            nurse.shift
        ))

        self.db.conn.commit()
        print("Nurse Added")

    def view_nurses(self):

        self.db.cursor.execute("SELECT * FROM nurses")
        rows = self.db.cursor.fetchall()

        for r in rows:
            print(r)

    # -------------------------
    # APPOINTMENT
    # -------------------------

    @log_action
    def book_appointment(self, appointment_id, patient_id, doctor_id, date, slot):

        self.db.cursor.execute("""
        INSERT INTO appointments VALUES (?, ?, ?, ?, ?, ?)
        """, (
            appointment_id,
            patient_id,
            doctor_id,
            date,
            slot,
            "Booked"
        ))

        self.db.conn.commit()
        print("Appointment Booked")

    def view_appointments(self):

        self.db.cursor.execute("SELECT * FROM appointments")
        rows = self.db.cursor.fetchall()

        for r in rows:
            print(r)

    # -------------------------
    # MEDICINE
    # -------------------------

    @log_action
    def add_medicine(self, medicine):

        self.db.cursor.execute("""
        INSERT INTO medicines VALUES (?, ?, ?, ?, ?)
        """, (
            medicine.medicine_id,
            medicine.medicine_name,
            medicine.stock,
            medicine.price,
            medicine.expiry_date
        ))

        self.db.conn.commit()
        print("Medicine Added")

    def view_medicines(self):

        self.db.cursor.execute("SELECT * FROM medicines")
        rows = self.db.cursor.fetchall()

        for r in rows:
            print(r)

    # -------------------------
    # MEDICAL RECORD
    # -------------------------

    @log_action
    def add_medical_record(self, record_id, patient_id, diagnosis, prescription, notes):

        self.db.cursor.execute("""
        INSERT INTO medical_records VALUES (?, ?, ?, ?, ?)
        """, (
            record_id,
            patient_id,
            diagnosis,
            prescription,
            notes
        ))

        self.db.conn.commit()
        print("Medical Record Added")

    def view_medical_records(self):

        self.db.cursor.execute("SELECT * FROM medical_records")
        rows = self.db.cursor.fetchall()

        for r in rows:
            print(r)

    # -------------------------
    # LAB REPORT
    # -------------------------

    @log_action
    def add_lab_report(self, report_id, patient_id, test_name, result, date):

        self.db.cursor.execute("""
        INSERT INTO lab_reports VALUES (?, ?, ?, ?, ?)
        """, (
            report_id,
            patient_id,
            test_name,
            result,
            date
        ))

        self.db.conn.commit()
        print("Lab Report Added")

    def view_lab_reports(self):

        self.db.cursor.execute("SELECT * FROM lab_reports")
        rows = self.db.cursor.fetchall()

        for r in rows:
            print(r)

    # -------------------------
    # BILLING
    # -------------------------

    @log_action
    def generate_bill(self, bill_id, patient_id, consultation, medicine, lab):

        total = consultation + medicine + lab

        self.db.cursor.execute("""
        INSERT INTO bills VALUES (?, ?, ?, ?, ?, ?)
        """, (
            bill_id,
            patient_id,
            consultation,
            medicine,
            lab,
            total
        ))

        self.db.conn.commit()
        print("Bill Generated:", total)

    def view_bills(self):

        self.db.cursor.execute("SELECT * FROM bills")
        rows = self.db.cursor.fetchall()

        for r in rows:
            print(r)