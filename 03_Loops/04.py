name = input("Enter your name: ")

reversed_name = ""

# for i in range(len(name)-1, -1, -1):
#     print(name[i], end="")

for char in name:
    reversed_name = char + reversed_name

print("\nReversed name:", reversed_name)
