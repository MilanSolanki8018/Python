items = ["apple", "banana", "orange", "apple", "mango"]

for item in items:
    if items.count(item) > 1:
        print(f"{item} is a duplicate item.")
        break;
    else:
        print(f"{item} is a unique item.")