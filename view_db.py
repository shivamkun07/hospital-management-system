import sqlite3

conn = sqlite3.connect("hospital.db")
cursor = conn.cursor()

tables = [
    "patients",
    "doctors",
    "nurses",
    "appointments",
    "medicines",
    "medical_records",
    "lab_reports",
    "bills"
]

for table in tables:

    print("\n====================")
    print("TABLE:", table)
    print("====================")

    try:
        cursor.execute(f"SELECT * FROM {table}")
        rows = cursor.fetchall()

        for row in rows:
            print(row)

    except Exception as e:
        print("Error:", e)