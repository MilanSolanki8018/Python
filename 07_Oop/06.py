class Car:
    Car_Count = 0
    def __init__(self,brand,model):
        self.__brand = brand # Private
        self._model = model  #Protected
        Car.Car_Count += 1

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

one = Car("Land Rover", "Diffender")
two = Car("Land Rover", "Rang Rover")

print(Car.Car_Count)

