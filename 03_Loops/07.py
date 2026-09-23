while True:
    number = int(input("Enter a number: "))

    if number > 0 and number < 10:
        print("You entered a valid number:", number)
        break
    else:
        print("Invalid input. Please enter a number between 1 and 9.")
