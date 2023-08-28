class Hero:
    def __init__(self,name,age):
        self.name = name
        self.age = age
        print(f"{name} is {age} years old")

    def adult(self):
        if(self.age>18):
            print("legal adult")
        else:
            print("not adult")


ramesh = Hero('ramesh',22)
ramesh.adult()
    