order_size = input("Enter the order size (small, medium, large): ").lower()
extra_shot = input("Do you want an extra shot? (yes/no): ").lower()

if extra_shot == "yes":
    coffee = order_size + " coffee with an extra shot"
else:
    coffee = order_size + " coffee"

print("Your order is: " + coffee)