class Vehicle:
    def __init__(self, brand, year):
        self.brand = brand
        self.year = year

    def start(self):
        print(f"{self.brand} is starting.")

class Car(Vehicle):
    def __init__(self, brand, year, model):
        super().__init__(brand, year)
        self.model = model

    def start(self):  # Method overriding
        print(f"{self.brand} {self.model} car is starting.")

    def drive(self):
        print(f"Driving the {self.brand} {self.model} car.")

# Creating an object of the Car class
car = Car("Toyota", 2022, "Corolla")

car = Car('toyota', 2002, 'corolla')
vehicle = Vehicle("maruti",2002)

vehicle.start()
car.start()
car.drive()
