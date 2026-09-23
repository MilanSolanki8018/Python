class Car:
    Car_Count = 0
    def __init__(self,brand,model):
        self.__brand = brand # Private
        self._model = model  #Protected
        Car.Car_Count += 1

    def display(self):
        return f"{self.brand} {self.model}"
    
    @staticmethod
    def general():
        print("This All Cars is High Demand Cars")

class ElectricCar(Car):
    def __init__(self,brand,model,battery_size):
        super().__init__(brand,model)
        self.battery_size = battery_size

    def display(self):
        print(self._model)
        return f"{self.battery_size}"

    


my_car = ElectricCar("Hyundai","Creata","55kwh")
print(Car.general())




