class Car:

    def __init__(self,brand,model):
        self.__brand = brand 
        self._model = model  

    def display(self):
        return f"{self.brand} {self.model}"
    
   
class ElectricCar(Car):
    def __init__(self,brand,model,battery_size):
        super().__init__(brand,model)
        self.battery_size = battery_size

    def display(self):
        print(self._model)
        return f"{self.battery_size}"

    


my_tesla = ElectricCar("Hyundai","Creata","55kwh")

print(isinstance(my_tesla, Car))
print(isinstance(my_tesla, ElectricCar))
print(issubclass(ElectricCar, Car))