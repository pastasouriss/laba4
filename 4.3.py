class Car:
    def __init__(self, name, color):
        self.speed = 0
        self.color = color
        self.name = name
        self.is_police = False

    def go(self):
        print(f"{self.color} {self.name} is moving.")

    def stop(self):
        print(f"{self.color} {self.name} has stopped.")

    def turn(self, direction):
        print(f"{self.color} {self.name} turned {direction}.")

    def show_speed(self):
        print(f"{self.color} {self.name} is moving at {self.speed} km/h.")

class TownCar(Car):
    def show_speed(self):
        if self.speed > 60:
            print(f"{self.color} {self.name} is exceeding the speed limit.")
        else:
            super().show_speed()

class SportCar(Car):
    pass

class WorkCar(Car):
    def show_speed(self):
        if self.speed > 40:
            print(f"{self.color} {self.name} is exceeding the speed limit.")
        else:
            super().show_speed()

class PoliceCar(Car):
    def __init__(self, name, color):
        super().__init__(name, color)
        self.is_police = True
car = Car("Car", "Red")
car.go()
car.show_speed()
car.speed = 80
car.show_speed()
town_car = TownCar("TownCar", "Blue")
town_car.speed = 70
town_car.show_speed()
police_car = PoliceCar("PoliceCar", "Black and White")
police_car.go()
print("Is it a police car?", police_car.is_police)