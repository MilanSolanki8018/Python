class Car:
    def __init__(self,brand,model):
        self.brand = brand 
        self._model = model  

    def get_brand(self):
        return f"{self.__brand}"

class ElectricCar(Car):
    def __init__(self,brand,model,battery_size):
        super().__init__(brand,model)
        self.battery_size = battery_size

    def display(self):
        print(self._model)
        return f"{self.battery_size}"
    


my_car = ElectricCar("Hyundai","Creata","55kwh")
print(my_car.display())
