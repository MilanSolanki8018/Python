class Car:
    def __init__(self,brand,model):
        self.__brand = brand # Private
        self._model = model  #Protected

    def display(self):
        return f"{self.brand} {self.model}"

    def fuel_type(self):
        print("Petrol and Gas")

class ElectricCar(Car):
    def __init__(self,brand,model,battery_size):
        super().__init__(brand,model)
        self.battery_size = battery_size

    def display(self):
        print(self._model)
        return f"{self.battery_size}"

    def fuel_type(self):
            print("Electric Charge")
    


my_car = ElectricCar("Hyundai","Creata","55kwh")
# print(my_car.display())
print(my_car.fuel_type())