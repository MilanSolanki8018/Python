def number(n):
    if n == 0:
        return 1
    else:
        print("A",n )
        return n * number(n - 1)

print(number(4))