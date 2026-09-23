age = int(input("Enter your age: "))
day = input("Enter the day of the week: ")

price = 8 if age < 18 else 12

if day == "Wednesday":
    price -= 2

print("Ticket Price For You: $" + str(price))