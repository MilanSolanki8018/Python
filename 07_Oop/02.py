class Car:
    def __init__(self,brand,model):
        self.brand = brand
        self.model = model

    def display(self):
        return f"{self.brand} {self.model}"


form = Car("Land Rover","Range Rover")
print(form.display())