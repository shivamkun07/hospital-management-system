class MedicalRecord:

    record_count = 0

    def __init__(
        self,
        patient_id,
        diagnosis,
        prescription,
        notes
    ):

        MedicalRecord.record_count += 1

        self.record_id = (
            f"R{MedicalRecord.record_count:03}"
        )

        self.patient_id = patient_id

        self.diagnosis = diagnosis

        self.prescription = prescription

        self.notes = notes

    def display_details(self):

        print("\n==============================")

        print(
            "Record ID:",
            self.record_id
        )

        print(
            "Patient ID:",
            self.patient_id
        )

        print(
            "Diagnosis:",
            self.diagnosis
        )

        print(
            "Prescription:",
            self.prescription
        )

        print(
            "Notes:",
            self.notes
        )

        print("==============================")