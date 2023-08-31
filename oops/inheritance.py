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




# multi level inheritance

class Grandparent:
    def __init__(self):
        self.grandparent_property = "Grandparent's property"

    def grandparent_method(self):
        print("Grandparent's method")

class Parent(Grandparent):
    def __init__(self):
        super().__init__()
        self.parent_property = "Parent's property"

    def parent_method(self):
        print("Parent's method")

class Child(Parent):
    def __init__(self):
        super().__init__()
        self.child_property = "Child's property"

    def child_method(self):
        print("Child's method")

# Creating an object of Child class
child_obj = Child()

# Accessing attributes and methods
print(child_obj.child_property)      # Output: Child's property
print(child_obj.parent_property)     # Output: Parent's property
print(child_obj.grandparent_property) # Output: Grandparent's property

child_obj.child_method()      # Output: Child's method
child_obj.parent_method()     # Output: Parent's method
child_obj.grandparent_method() # Output: Grandparent's method



# hierarchical inheritance
class Animal:
    def __init__(self, name):
        self.name = name

    def speak(self):
        pass

class Dog(Animal):
    def speak(self):
        return "Woof!"

class Cat(Animal):
    def speak(self):
        return "Meow!"

class Cow(Animal):
    def speak(self):
        return "Moo!"

# Creating objects of different subclasses
dog = Dog("Buddy")
cat = Cat("Whiskers")
cow = Cow("Molly")

# Accessing common method from the base class
print(dog.name)  # Output: Buddy

# Calling overridden method from each subclass
print(dog.speak())  # Output: Woof!
print(cat.speak())  # Output: Meow!
print(cow.speak())  # Output: Moo!
