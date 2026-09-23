name = "rajendra"

def greet():
    name = "Aryan"
    print("Hello", name)

greet() 
print("Hello", name)


def one(num):
    def two(num2):
        return num + num2
    return two  

result = one(5)  # Return Function defination
print(result(10))  # Output: 15 Using closure to add 5 to 10