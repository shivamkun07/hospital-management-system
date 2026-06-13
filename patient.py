from person import Person


class Patient(Person):

    def __init__(self, patient_id, name, age, gender, phone, blood_group):

        self.patient_id = patient_id
        self.name = name
        self.age = age
        self.gender = gender
        self.phone = phone
        self.blood_group = blood_group

    def display_details(self):

        print("\n==============================")
        print("Patient ID :", self.patient_id)
        print("Name       :", self.name)
        print("Age        :", self.age)
        print("Gender     :", self.gender)
        print("Phone      :", self.phone)
        print("Blood Group:", self.blood_group)
        print("==============================")
    @classmethod
    def from_dict(cls, data):

        obj = cls(
            data["name"],
            data["age"],
            data["gender"],
            data["phone"],
            data["blood_group"]
        )

        obj.person_id = data.get("person_id")

        return obj