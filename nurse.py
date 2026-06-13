from person import Person


class Nurse(Person):

    nurse_count = 0

    def __init__(
        self,
        name,
        age,
        gender,
        phone,
        department,
        shift
    ):

        super().__init__(
            name,
            age,
            gender,
            phone
        )

        Nurse.nurse_count += 1

        self.nurse_id = f"N{Nurse.nurse_count:03}"

        self.department = department
        self.shift = shift

    def display_details(self):

        print("\n==============================")
        print("Nurse ID   :", self.nurse_id)
        print("Name       :", self.name)
        print("Age        :", self.age)
        print("Gender     :", self.gender)
        print("Phone      :", self.phone)
        print("Department :", self.department)
        print("Shift      :", self.shift)
        print("==============================")

    @classmethod
    def from_dict(cls, data):

        obj = cls(
            data["name"],
            data["age"],
            data["gender"],
            data["phone"],
            data["department"],
            data["shift"]
        )

        obj.person_id = data.get("person_id")

        return obj