class Car:
    def __init__(self,brand,model):
        self.brand = brand
        self.model = model
        # self.brand = "AS"
        # print(self.brand)
        # print(brand)
        # print(self.brand is brand)


form = Car("Land Rover","Range Rover")

print(form.brand)
print(form.model)
