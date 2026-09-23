name = input("Enter your name: ")

for char in name:
    print(char)

    if name.count(char) == 1:
        print("First Non-Repeated Character:", char)
        break
