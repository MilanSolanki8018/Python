number = int(input("Enter a number: "))
sum = 0
for i in range(1, number + 1):
    if i % 2 == 0:
        sum += i

print("Sum of even numbers from 1 to", number, "is:", sum)