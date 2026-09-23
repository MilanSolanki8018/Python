def even(limit):
    for i in range(2, limit + 1, 2):
        yield i
        

for num in even(15):
    print(num)

