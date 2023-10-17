class Car:
    def __init__(self, name, color):
        self.speed = 0
        self.color = color
        self.name = name
        self.is_police = False

    def go(self):
        print(f"{self.color} {self.name} движется.")

    def stop(self):
        print(f"{self.color} {self.name} остановилась.")

    def turn(self, direction):
        print(f"{self.color} {self.name} едет {direction}.")

    def show_speed(self):
        print(f"{self.color} {self.name} движется со скоростью {self.speed} km/h.")

class TownCar(Car):
    def show_speed(self):
        if self.speed > 60:
            print(f"{self.color} {self.name} превысила лимит.")
        else:
            super().show_speed()

class SportCar(Car):
    pass

class WorkCar(Car):
    def show_speed(self):
        if self.speed > 40:
            print(f"{self.color} {self.name} превысила лимит.")
        else:
            super().show_speed()

class PoliceCar(Car):
    def __init__(self, name, color):
        super().__init__(name, color)
        self.is_police = True
car = Car("Машина", "Красная")
car.go()
car.show_speed()
car.speed = 80
car.show_speed()
town_car = TownCar("Городская машина", "Голубая")
town_car.speed = 70
town_car.show_speed()
police_car = PoliceCar("Полицейская машина", "Черно-белая")
police_car.go()
print("Это полицейская машина?", police_car.is_police)