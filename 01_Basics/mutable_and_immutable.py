# String is Immutable

name = "Virat" # Memory location 1
type(name)  # <class 'str'>
print(id(name))  # Memory location 1
print(name)  # Virat

# Not Changing a memomy location value but creating a new memory location with new value

name = "Rohit" # Memory location 2
print(id(name))  # Memory location 2    
print(name)  # Rohit

#Int is Immutable
a = 10 # Memory location 1
print(id(a))  # Memory location 1
print(a)  # 10
b = a 
print(id(b))  # Also use Memory location 1
print(b)  # 10

a= 20 # Memory location 2
print(id(a))  # Memory location 2
print(a)  # 20
print(b)  # 10 Reffernece is not changed because int is immutable

