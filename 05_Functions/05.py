def greet(name="Aryan"):
    print("Hello", name)


name = input("Enter your name: ")
greet(name) 
greet()  # Calling the function without an argument, will use the default value
