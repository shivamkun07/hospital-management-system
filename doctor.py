from person import Person


class Doctor(Person):

    doctor_count = 0

    def __init__(
        self,
        name,
        age,
        gender,
        phone,
        specialization,
        consultation_fee,
        available_slots
    ):

        super().__init__(
            name,
            age,
            gender,
            phone
        )

        Doctor.doctor_count += 1

        self.doctor_id = f"D{Doctor.doctor_count:03}"

        self.specialization = specialization

        self.consultation_fee = consultation_fee

        self.available_slots = available_slots

    def display_details(self):

        print("\n==============================")
        print("Doctor ID       :", self.doctor_id)
        print("Name            :", self.name)
        print("Age             :", self.age)
        print("Gender          :", self.gender)
        print("Phone           :", self.phone)
        print("Specialization  :", self.specialization)
        print("Consultation Fee:", self.consultation_fee)

        print("Available Slots:")
        for slot in self.available_slots:
            print("-", slot)

        print("==============================")
    @classmethod
    def from_dict(cls, data):

        obj = cls(
            data["name"],
            data["age"],
            data["gender"],
            data["phone"],
            data["specialization"],
            data["consultation_fee"],
            data["available_slots"]
        )

        obj.person_id = data.get("person_id")

        return obj
    