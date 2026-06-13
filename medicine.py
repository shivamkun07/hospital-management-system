from datetime import datetime


class Medicine:

    medicine_count = 0

    def __init__(self, medicine_name, stock, price, expiry_date):

        Medicine.medicine_count += 1

        self.medicine_id = f"M{Medicine.medicine_count:03}"

        self.medicine_name = medicine_name
        self.stock = stock
        self.price = price
        self.expiry_date = expiry_date

    def add_stock(self, quantity):
        self.stock += quantity

    def reduce_stock(self, quantity):

        if quantity <= self.stock:
            self.stock -= quantity
        else:
            print("Insufficient Stock")

    def check_expiry(self):

        today = datetime.today()

        expiry = datetime.strptime(self.expiry_date, "%d-%m-%Y")

        if expiry < today:
            return "Expired"

        return "Valid"

    def display_details(self):

        print("\n==============================")
        print("Medicine ID:", self.medicine_id)
        print("Name:", self.medicine_name)
        print("Stock:", self.stock)
        print("Price:", self.price)
        print("Expiry:", self.expiry_date)
        print("Status:", self.check_expiry())
        print("==============================")

    @classmethod
    def from_dict(cls, data):

        obj = cls(
            data["medicine_name"],
            data["stock"],
            data["price"],
            data["expiry_date"]
        )

        obj.medicine_id = data.get("medicine_id")

        return obj
    
    