class Bill:

    bill_count = 0

    def __init__(
        self,
        patient_id,
        consultation_charge,
        medicine_charge,
        lab_charge
    ):

        Bill.bill_count += 1

        self.bill_id = (
            f"B{Bill.bill_count:03}"
        )

        self.patient_id = patient_id

        self.consultation_charge = consultation_charge

        self.medicine_charge = medicine_charge

        self.lab_charge = lab_charge

        self.total_amount = (
            consultation_charge
            +
            medicine_charge
            +
            lab_charge
        )

    def display_details(self):

        print("\n==============================")

        print(
            "Bill ID:",
            self.bill_id
        )

        print(
            "Patient ID:",
            self.patient_id
        )

        print(
            "Consultation Charge:",
            self.consultation_charge
        )

        print(
            "Medicine Charge:",
            self.medicine_charge
        )

        print(
            "Lab Charge:",
            self.lab_charge
        )

        print(
            "Total Amount:",
            self.total_amount
        )

        print("==============================")