from hospital import Hospital
from patient import Patient
from doctor import Doctor
from nurse import Nurse
from medicine import Medicine

hospital = Hospital()


# =========================
# REUSABLE INPUT FUNCTIONS
# =========================

def select_option(title, options):
    print(f"\nSelect {title}")
    for k, v in options.items():
        print(f"{k}. {v}")
    return options.get(input("Enter Choice: "), list(options.values())[0])


def select_multiple_options(title, options):
    print(f"\nSelect {title} (comma separated like 1,2,3)")
    for k, v in options.items():
        print(f"{k}. {v}")

    choices = input("Enter Choice: ").split(",")
    return [options.get(c.strip(), "") for c in choices if c.strip() in options]


def select_gender():
    genders = {
        "1": "Male",
        "2": "Female",
        "3": "Other"
    }

    print("\nSelect Gender")
    for k, v in genders.items():
        print(f"{k}. {v}")

    return genders.get(input("Enter Choice: "), "Other")


# =========================
# MAIN LOOP
# =========================

while True:

    print("\n" + "=" * 50)
    print(" SMART HOSPITAL MANAGEMENT SYSTEM ")
    print("=" * 50)

    print("1. Patient Management")
    print("2. Doctor Management")
    print("3. Nurse Management")
    print("4. Appointment Management")
    print("5. Pharmacy Management")
    print("6. Medical Records")
    print("7. Laboratory Reports")
    print("8. Billing Management")
    print("9. Exit")

    main_choice = input("\nEnter Choice: ")

    # ==================================================
    # PATIENT MANAGEMENT
    # ==================================================
    if main_choice == "1":

        while True:

            print("\n--- PATIENT MANAGEMENT ---")
            print("1. Register Patient")
            print("2. View Patients")
            print("3. Back")

            choice = input("Enter Choice: ")

            if choice == "1":

                patient_id = input("Enter Patient ID: ")
                name = input("Enter Name: ")
                age = int(input("Enter Age: "))

                gender = select_gender()

                phone = input("Enter Phone Number: ")

                blood_groups = {
                    "1": "A+","2": "A-","3": "B+","4": "B-",
                    "5": "O+","6": "O-","7": "AB+","8": "AB-"
                }

                blood_group = select_option("Blood Group", blood_groups)

                patient = Patient(
                    patient_id,
                    name,
                    age,
                    gender,
                    phone,
                    blood_group
                )

                hospital.register_patient(patient)

            elif choice == "2":
                hospital.view_patients()

            elif choice == "3":
                break

    # ==================================================
    # DOCTOR MANAGEMENT
    # ==================================================
    elif main_choice == "2":

        while True:

            print("\n--- DOCTOR MANAGEMENT ---")
            print("1. Add Doctor")
            print("2. View Doctors")
            print("3. Back")

            choice = input("Enter Choice: ")

            if choice == "1":

                doctor_id = input("Doctor ID: ")
                name = input("Enter Name: ")
                age = int(input("Enter Age: "))

                gender = select_gender()

                phone = input("Enter Phone: ")

                specializations = {
                    "1": "General Physician",
                    "2": "Cardiologist",
                    "3": "Neurologist",
                    "4": "Dermatologist",
                    "5": "Orthopedic",
                    "6": "Pediatrician",
                    "7": "Gynecologist",
                    "8": "ENT Specialist"
                }

                specialization = select_option("Specialization", specializations)

                fee = float(input("Consultation Fee: "))

                slots = {
                    "1": "09:00 AM - 10:00 AM",
                    "2": "10:00 AM - 11:00 AM",
                    "3": "11:00 AM - 12:00 PM",
                    "4": "12:00 PM - 01:00 PM",
                    "5": "02:00 PM - 03:00 PM",
                    "6": "03:00 PM - 04:00 PM",
                    "7": "04:00 PM - 05:00 PM"
                }

                selected_slots = select_multiple_options("Available Slots", slots)

                doctor = Doctor(
                    name,
                    age,
                    gender,
                    phone,
                    specialization,
                    fee,
                    selected_slots
                )

                hospital.add_doctor(doctor)

            elif choice == "2":
                hospital.view_doctors()

            elif choice == "3":
                break

    # ==================================================
    # NURSE MANAGEMENT
    # ==================================================
    elif main_choice == "3":

        while True:

            print("\n--- NURSE MANAGEMENT ---")
            print("1. Add Nurse")
            print("2. View Nurses")
            print("3. Back")

            choice = input("Enter Choice: ")

            if choice == "1":

                nurse_id = input("Nurse ID: ")
                name = input("Enter Name: ")
                age = int(input("Enter Age: "))

                gender = select_gender()

                phone = input("Enter Phone: ")

                departments = {
                    "1": "ICU",
                    "2": "Emergency",
                    "3": "General Ward",
                    "4": "Pediatrics",
                    "5": "Operation Theatre",
                    "6": "Maternity Ward"
                }

                department = select_option("Department", departments)

                shifts = {
                    "1": "Morning (6AM - 2PM)",
                    "2": "Evening (2PM - 10PM)",
                    "3": "Night (10PM - 6AM)",
                    "4": "Rotational"
                }

                shift = select_option("Shift", shifts)

                nurse = Nurse(
                    name,
                    age,
                    gender,
                    phone,
                    department,
                    shift
                )

                hospital.add_nurse(nurse)

            elif choice == "2":
                hospital.view_nurses()

            elif choice == "3":
                break

    # ==================================================
    # APPOINTMENTS
    # ==================================================
    elif main_choice == "4":

        while True:

            print("\n--- APPOINTMENT MANAGEMENT ---")
            print("1. Book Appointment")
            print("2. View Appointments")
            print("3. Cancel Appointment")
            print("4. Back")

            choice = input("Enter Choice: ")

            if choice == "1":

                hospital.book_appointment(
                    input("Appointment ID: "),
                    input("Patient ID: "),
                    input("Doctor ID: "),
                    input("Date (dd-mm-yyyy): "),
                    input("Slot: ")
                )

            elif choice == "2":
                hospital.view_appointments()

            elif choice == "3":
                hospital.cancel_appointment(
                    input("Appointment ID: ")
                )

            elif choice == "4":
                break

    # ==================================================
    # PHARMACY
    # ==================================================
    elif main_choice == "5":

        while True:

            print("\n--- PHARMACY ---")
            print("1. Add Medicine")
            print("2. View Medicines")
            print("3. Back")

            choice = input("Enter Choice: ")

            if choice == "1":

                medicine = Medicine(
                    input("Medicine ID: "),
                    input("Name: "),
                    int(input("Stock: ")),
                    float(input("Price: ")),
                    input("Expiry: ")
                )

                hospital.add_medicine(medicine)

            elif choice == "2":
                hospital.view_medicines()

            elif choice == "3":
                break

    # ==================================================
    # MEDICAL RECORDS
    # ==================================================
    elif main_choice == "6":

        while True:

            print("\n--- MEDICAL RECORDS ---")
            print("1. Add Record")
            print("2. View Records")
            print("3. Patient History")
            print("4. Back")

            choice = input("Enter Choice: ")

            if choice == "1":

                hospital.add_medical_record(
                    input("Record ID: "),
                    input("Patient ID: "),
                    input("Diagnosis: "),
                    input("Prescription: "),
                    input("Notes: ")
                )

            elif choice == "2":
                hospital.view_medical_records()

            elif choice == "3":
                hospital.view_patient_history(
                    input("Patient ID: ")
                )

            elif choice == "4":
                break

    # ==================================================
    # LAB REPORTS
    # ==================================================
    elif main_choice == "7":

        while True:

            print("\n--- LAB REPORTS ---")
            print("1. Add Report")
            print("2. View Reports")
            print("3. Patient Reports")
            print("4. Back")

            choice = input("Enter Choice: ")

            if choice == "1":

                hospital.add_lab_report(
                    input("Report ID: "),
                    input("Patient ID: "),
                    input("Test Name: "),
                    input("Result: "),
                    input("Date: ")
                )

            elif choice == "2":
                hospital.view_lab_reports()

            elif choice == "3":
                hospital.view_patient_lab_reports(
                    input("Patient ID: ")
                )

            elif choice == "4":
                break

    # ==================================================
    # BILLING
    # ==================================================
    elif main_choice == "8":

        while True:

            print("\n--- BILLING ---")
            print("1. Generate Bill")
            print("2. View Bills")
            print("3. Back")

            choice = input("Enter Choice: ")

            if choice == "1":

                hospital.generate_bill(
                    input("Bill ID: "),
                    input("Patient ID: "),
                    float(input("Consultation: ")),
                    float(input("Medicine: ")),
                    float(input("Lab: "))
                )

            elif choice == "2":
                hospital.view_bills()

            elif choice == "3":
                break

    # ==================================================
    # EXIT
    # ==================================================
    elif main_choice == "9":
        print("\nThank you for using Smart Hospital System.")
        break

    else:
        print("\nInvalid Choice.")