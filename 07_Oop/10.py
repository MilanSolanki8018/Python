class Battery():
    pass

class Engine():
    def details(self):
        print("True, High Recomndent")

class ElectricCar(Battery, Engine):
    def display(self):
        print("Inherite Both Class")

obj = ElectricCar()
obj.details()
