class Appointment:

    appointment_count = 0

    def __init__(
        self,
        patient_id,
        doctor_id,
        appointment_date,
        slot
    ):

        Appointment.appointment_count += 1

        self.appointment_id = (
            f"A{Appointment.appointment_count:03}"
        )

        self.patient_id = patient_id
        self.doctor_id = doctor_id

        self.appointment_date = appointment_date

        self.slot = slot

        self.status = "Booked"

    def cancel(self):

        self.status = "Cancelled"

    def reschedule(
        self,
        new_date,
        new_slot
    ):

        self.appointment_date = new_date

        self.slot = new_slot

        self.status = "Rescheduled"

    def display_details(self):

        print("\n==============================")

        print(
            "Appointment ID:",
            self.appointment_id
        )

        print(
            "Patient ID:",
            self.patient_id
        )

        print(
            "Doctor ID:",
            self.doctor_id
        )

        print(
            "Date:",
            self.appointment_date
        )

        print(
            "Slot:",
            self.slot
        )

        print(
            "Status:",
            self.status
        )

        print("==============================")