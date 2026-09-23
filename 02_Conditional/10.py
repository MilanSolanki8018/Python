species = input("Enter the species of the animal (dog, cat): ").lower()
age = int(input("Enter the age of the animal: "))

if species == "dog":
    if age < 2:
        print("puppy food")
    else:
        print("adult food")

elif species == "cat":
    if age > 5:
        print("senior cat food")
    else:
        print("regular cat food")
else:
    print("Unknown species")
