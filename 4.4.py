class Smartphone:
    total_count = 0

    def __init__(self, brand, model, price):
        self.brand = brand
        self.model = model
        self.price = price
        Smartphone.total_count += 1

    def make_call(self, number):
        print(f"Звонит номер {number} с телефона  {self.brand} {self.model}")

    def send_message(self, number, message):
        print(f"Отправляется сообщение с номера {number} с телефона {self.brand} {self.model}: {message}")
    def get_total_count():
        return Smartphone.total_count
    def get_brand(cls):
        return cls.brand
phone1 = Smartphone("Samsung", "Galaxy S8", 400)
phone1.make_call("1234567890")
phone1.send_message("1234567890", "Приветики!")

phone2 = Smartphone("Apple", "iPhone 12", 1099)
phone2.make_call("9876543210")
phone2.send_message("9876543210", "Как делишки?")

print("Всего смартфонов:", Smartphone.get_total_count())
print("Бренд первого:", phone1.get_brand())
print("Бренд второго:", phone2.get_brand())