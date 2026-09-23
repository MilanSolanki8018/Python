fruite = input("Enter a fruit name: ")
color = input("Enter the color of the fruit: ")

if fruite == "Banana":
    if color == "Green":
        print(f"The {fruite} is unripe.")
    elif color == "Yellow":
        print(f"The {fruite} is ripe.")
    elif color == "Brown":
        print(f"The {fruite} is overripe.")
else:
    print(f"The {fruite} is not a banana.")